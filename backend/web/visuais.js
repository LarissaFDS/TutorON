(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };
  var atual, versao = 0, disponivel = false;
  var video = $('video');
  function status(id, texto, tom) {
    $(id).textContent = texto;
    if (tom) $(id).dataset.tone = tom; else delete $(id).dataset.tone;
  }
  function mostrarVideo(url) {
    video.src = url;
    video.setAttribute('aria-label', 'Pista visual: ' + atual.titulo);
    video.hidden = false;
    $('video-vazio').hidden = true;
    $('preparar').textContent = 'Reproduzir desde o início';
    $('pausar-pergunta').disabled = false;
  }
  function escolher(e) {
    atual = e;
    versao++;
    video.pause();
    video.removeAttribute('src');
    video.removeAttribute('poster');
    video.load();
    video.hidden = true;
    $('video-vazio').hidden = false;
    $('pausar-pergunta').disabled = true;
    $('exemplo-titulo').textContent = e.titulo;
    $('exemplo-disciplina').textContent = e.disciplina === 'paa' ? 'Projeto e Análise de Algoritmos' : 'Sistemas Digitais';
    $('exemplo-resumo').textContent = e.resumo;
    $('observar').textContent = e.observar;
    $('tarefa').textContent = e.tarefa;
    $('tentativa').value = '';
    $('preparar').textContent = e.video ? 'Reproduzir desde o início' : 'Preparar animação';
    $('preparar').disabled = !disponivel && !e.video;
    status('video-status', e.video ? 'Pause o vídeo quando quiser e tente continuar no papel.' :
      (disponivel ? 'Na primeira vez, preparar o desenho pode levar até 90 segundos.' : 'As animações estão indisponíveis neste servidor.'), disponivel ? '' : 'error');
    document.querySelectorAll('.visual-tema').forEach(function (b) {
      var selecionado = b.dataset.id === e.id;
      b.setAttribute('aria-current', String(selecionado));
      if (selecionado && window.matchMedia('(max-width: 760px)').matches) {
        var lista = $('exemplos');
        lista.scrollLeft = Math.max(0, b.offsetLeft - lista.offsetLeft - (lista.clientWidth - b.clientWidth) / 2);
      }
    });
    if (e.poster) video.poster = e.poster;
    if (e.video) mostrarVideo(e.video);
    var url = new URL(location.href);
    url.searchParams.set('exemplo', e.id);
    history.replaceState(null, '', url);
  }
  $('preparar').addEventListener('click', async function () {
    if (atual.video) { video.currentTime = 0; video.play().catch(function () {}); return; }
    var e = atual, v = versao;
    $('preparar').disabled = true;
    status('video-status', 'Preparando o desenho… você pode escolher outro tema enquanto espera.', 'busy');
    try {
      var r = await fetch('/api/visuais/' + encodeURIComponent(e.id), { method: 'POST' });
      var t = await r.json();
      if (!r.ok) throw new Error(t.erro || 'Não foi possível preparar o desenho.');
      while (t.status !== 'pronta' && t.status !== 'erro') {
        await new Promise(function (resolve) { setTimeout(resolve, 900); });
        r = await fetch('/api/tarefas/' + encodeURIComponent(t.id), { cache: 'no-store' });
        t = await r.json();
        if (!r.ok) throw new Error(t.erro || 'O pedido expirou. Tente novamente.');
      }
      if (t.status !== 'pronta') throw new Error(t.mensagem || 'O desenho não ficou pronto.');
      e.video = t.video;
      e.poster = t.poster;
      if (v === versao) {
        if (e.poster) video.poster = e.poster;
        mostrarVideo(e.video);
        status('video-status', 'Desenho pronto. Reproduza e pause antes de tentar o próximo passo.');
      }
    } catch (erro) {
      if (v === versao) status('video-status', erro.message, 'error');
    } finally { if (v === versao) $('preparar').disabled = false; }
  });
  $('pausar-pergunta').addEventListener('click', function () {
    if (Number.isFinite(video.duration)) {
      video.pause();
      video.currentTime = Math.max(0, video.duration - 1.5);
      status('video-status', 'Sua vez: ' + atual.pergunta_final);
      $('tentativa').focus({ preventScroll: true });
    }
  });
  video.addEventListener('error', function () {
    if (video.getAttribute('src')) {
      status('video-status', 'Não foi possível abrir o vídeo. Prepare o desenho novamente.', 'error');
      atual.video = null;
      $('preparar').textContent = 'Preparar novamente';
      $('preparar').disabled = !disponivel;
      $('pausar-pergunta').disabled = true;
    }
  });
  $('tentativa-form').addEventListener('submit', function (evento) {
    evento.preventDefault();
    var tentativa = $('tentativa').value.trim();
    if (!tentativa) { $('tentativa').focus(); return; }
    try {
      sessionStorage.setItem('tutoron-tentativa-visual', JSON.stringify({ pergunta: atual.pergunta,
        contexto: 'Minha tentativa após o exemplo visual:\n' + tentativa, disciplina: atual.disciplina }));
      location.href = '/?disciplina=' + encodeURIComponent(atual.disciplina);
    } catch (e) { status('video-status', 'Não consegui guardar a tentativa nesta aba. Copie seu texto e abra o tutor.', 'error'); }
  });
  (async function carregar() {
    try {
      var r = await fetch('/api/visuais', { cache: 'no-store' });
      if (!r.ok) throw new Error('Não foi possível carregar os exemplos. Recarregue a página.');
      var dados = await r.json();
      disponivel = dados.disponivel;
      if (!dados.exemplos.length) { status('catalogo-status', 'Ainda não há exemplos disponíveis para as disciplinas liberadas.'); return; }
      dados.exemplos.forEach(function (e) {
        var b = document.createElement('button');
        b.type = 'button'; b.className = 'visual-tema'; b.dataset.id = e.id;
        b.append(document.createTextNode(e.titulo));
        var disciplina = document.createElement('small');
        disciplina.textContent = e.disciplina === 'paa' ? 'PAA' : 'Sistemas Digitais';
        b.append(disciplina);
        b.addEventListener('click', function () { escolher(e); });
        $('exemplos').append(b);
      });
      $('visual-layout').hidden = false;
      status('catalogo-status', '');
      var id = new URL(location.href).searchParams.get('exemplo');
      escolher(dados.exemplos.find(function (e) { return e.id === id; }) || dados.exemplos[0]);
    } catch (e) { status('catalogo-status', e.message || 'Sem conexão. Recarregue a página para tentar novamente.', 'error'); }
  })();
})();
