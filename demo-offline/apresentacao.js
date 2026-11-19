/* Apenas reprodução de registros embutidos: sem rede, armazenamento ou geração de IA. */
(function () {
  'use strict';
  var dados = window.TUTORON_DEMO;
  var arquivos = window.TUTORON_DEMO_ARQUIVOS;
  var R = window.TutorONRender;
  var $ = function (id) { return document.getElementById(id); };
  var nomes = { auto: 'O tutor escolhe', pista: 'Uma pista', perguntas: 'Perguntas-guia', conceito: 'Explicar o conceito', exemplo: 'Exemplo parecido', conferir: 'Conferir meu raciocínio', visual: 'Desenho/esquema' };
  var selecionado;
  var rodada = 0;

  function painel(nome) {
    document.querySelectorAll('[data-panel]').forEach(function (b) {
      var ativo = b.dataset.panel === nome;
      b.setAttribute('aria-pressed', String(ativo));
      $('painel-' + b.dataset.panel).hidden = !ativo;
    });
    if (nome !== 'visual') $('video').pause();
  }
  document.querySelectorAll('[data-panel]').forEach(function (b) {
    b.addEventListener('click', function () { painel(b.dataset.panel); });
  });

  function escolher() {
    selecionado = dados.ajudas[Number($('exemplo').value)];
    $('pergunta').value = selecionado.pergunta;
    $('contexto').textContent = selecionado.contexto || '';
    $('contexto').hidden = !selecionado.contexto;
    $('tipo-ajuda').textContent = 'Tipo de ajuda neste exemplo: ' + nomes[selecionado.ajuda];
    $('resultado').hidden = true;
    $('feedback-status').textContent = '';
  }
  function disciplina() {
    $('exemplo').replaceChildren();
    dados.ajudas.forEach(function (c, i) {
      if (c.disciplina !== $('disciplina').value) return;
      $('exemplo').add(new Option(c.titulo, String(i)));
    });
    escolher();
  }
  $('disciplina').addEventListener('change', disciplina);
  $('exemplo').addEventListener('change', escolher);
  $('pedir-ajuda').addEventListener('click', function () {
    R.renderPlain($('pergunta-enviada'), selecionado.pergunta + (selecionado.contexto ? '\n\n' + selecionado.contexto : ''));
    R.render($('resposta'), selecionado.texto);
    $('origem').textContent = 'Resposta real gravada, sem edição · ' + selecionado.modelo + ' · ' + selecionado.data.split('-').reverse().join('/');
    $('feedback-status').textContent = '';
    $('resultado').hidden = false;
    $('titulo-resposta').focus();
  });
  document.querySelectorAll('[data-feedback]').forEach(function (b) {
    b.addEventListener('click', function () {
      $('feedback-status').textContent = 'Você marcou “' + b.dataset.feedback + '”. Nesta demonstração, a avaliação é apenas visual e não é salva nem enviada.';
    });
  });
  $('ver-ciclo').addEventListener('click', function () { painel('foto'); });
  $('ver-desenhos').addEventListener('click', function () { painel('visual'); });

  // Foto: o aluno vê e confirma a transcrição antes de receber a primeira ajuda.
  $('foto').src = arquivos[dados.ciclo.foto];
  R.render($('tentativa'), dados.ciclo.leitura.tentativa);
  R.render($('enunciado'), dados.ciclo.leitura.enunciado);
  function limparFoto() {
    rodada = 0;
    $('ciclo').replaceChildren();
    $('foto-leitura').hidden = true;
    $('mostrar-foto').hidden = false;
    $('confirmar-foto').hidden = false;
    $('outra-pista').hidden = true;
    $('reiniciar-foto').hidden = true;
    $('fim-ciclo').textContent = '';
  }
  function proximaPista() {
    var r = dados.ciclo.rodadas[rodada];
    if (!r) return;
    var article = document.createElement('article');
    article.className = 'troca';
    var h = document.createElement('h3');
    h.textContent = 'Rodada ' + (rodada + 1) + ' · ' + nomes[r.ajuda];
    h.tabIndex = -1;
    var q = document.createElement('p');
    q.className = 'question';
    q.textContent = rodada ? 'Aluno: Ainda não consegui. ' + r.travou : 'Aluno: ' + dados.ciclo.pergunta;
    var answer = document.createElement('div');
    answer.className = 'prose resposta';
    R.render(answer, r.texto);
    var caption = document.createElement('p');
    caption.className = 'caption';
    caption.textContent = 'Resposta real gravada · ' + r.modelo;
    article.append(h, q, answer, caption);
    $('ciclo').append(article);
    rodada++;
    $('confirmar-foto').hidden = true;
    $('outra-pista').hidden = rodada >= dados.ciclo.rodadas.length;
    $('reiniciar-foto').hidden = false;
    if (rodada >= dados.ciclo.rodadas.length) $('fim-ciclo').textContent = 'Fim das três rodadas gravadas. No TutorON conectado, o aluno pode continuar pedindo ajuda.';
    h.focus();
  }
  $('mostrar-foto').addEventListener('click', function () { $('foto-leitura').hidden = false; $('mostrar-foto').hidden = true; });
  $('confirmar-foto').addEventListener('click', proximaPista);
  $('outra-pista').addEventListener('click', proximaPista);
  $('reiniciar-foto').addEventListener('click', limparFoto);

  // WebM e MP4 embutidos; o quadro final pode ser aberto mesmo sem codec de vídeo.
  dados.animacoes.forEach(function (v, i) { $('animacao').add(new Option(v.disciplina + ' · ' + v.titulo, String(i))); });
  function animacao() {
    var v = dados.animacoes[Number($('animacao').value)];
    var video = $('video');
    video.pause();
    video.replaceChildren();
    ['webm', 'mp4'].forEach(function (ext) {
      var source = document.createElement('source');
      source.src = arquivos[v.arquivo.replace(/\.mp4$/, '.' + ext)];
      source.type = 'video/' + ext;
      video.append(source);
    });
    video.poster = arquivos[v.arquivo.replace(/\.mp4$/, '.png')];
    $('video-capa').src = video.poster;
    $('video-titulo').textContent = v.titulo;
    $('video-pergunta').textContent = v.pergunta;
    $('video-tarefa').textContent = 'Sua vez: ' + v.pergunta_final;
    $('video-status').textContent = 'Use os controles do vídeo para reproduzir, pausar ou ampliar.';
    video.load();
  }
  $('animacao').addEventListener('change', animacao);
  $('video').addEventListener('error', function () { $('video-status').textContent = 'O navegador não conseguiu reproduzir o vídeo. Abra “Ver quadro final como imagem” abaixo.'; });
  $('reiniciar').addEventListener('click', function () {
    $('disciplina').value = 'PAA';
    disciplina(); limparFoto(); $('animacao').value = '0'; animacao(); painel('tutor');
  });
  disciplina(); limparFoto(); animacao();
})();
