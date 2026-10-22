/* Demonstração do tutor socrático: só mostra respostas reais gravadas (demo/demo.json). Nenhuma IA é chamada. */
(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };
  var R = window.TutorONRender;
  // Versão offline (scripts/demo_offline.py): dados e arquivos vêm embutidos no próprio HTML.
  var EMBUTIDOS = window.TUTORON_DEMO_ARQUIVOS || {};
  function arquivo(nome) { return EMBUTIDOS[nome] || '/static/demo/' + nome; }
  var NOMES = { auto: 'O tutor escolhe', pista: 'Uma pista', perguntas: 'Perguntas-guia', conceito: 'Explicar o conceito',
    exemplo: 'Exemplo parecido', conferir: 'Conferir meu raciocínio', visual: 'Desenho/esquema' };

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text !== undefined) n.textContent = text;
    return n;
  }

  function resposta(texto) {
    var d = el('div', 'prose resposta');
    R.render(d, texto);
    return d;
  }

  function pergunta(texto, extra) {
    var q = el('div', 'question prose');
    R.renderPlain(q, texto);
    if (extra) q.append(el('pre', 'demo__contexto', extra));
    return q;
  }

  // ------------------------------------------------------------------ 1. formas de ajuda
  function mostrarCard(c) {
    var card = $('demo-card');
    card.replaceChildren(
      el('p', 'caption', c.disciplina + ' · tipo de ajuda pedido: ' + NOMES[c.ajuda]),
      pergunta(c.pergunta, c.contexto),
      resposta(c.texto),
      el('p', 'caption', 'Resposta real, sem edição · ' + c.modelo + ' · ' + c.data.split('-').reverse().join('/')));
  }

  function montarAjudas(cards) {
    var box = $('demo-escolha');
    cards.forEach(function (c, i) {
      var label = el('label', 'pick');
      var input = document.createElement('input');
      input.type = 'radio';
      input.name = 'demo';
      input.checked = i === 0;
      input.addEventListener('change', function () { mostrarCard(c); });
      label.append(input, el('span', null, c.titulo));
      box.append(label);
    });
    mostrarCard(cards[0]);
  }

  // ------------------------------------------------------------------ 2. foto + ciclo
  function montarCiclo(ciclo) {
    $('ciclo-foto').src = arquivo(ciclo.foto);
    var l = ciclo.leitura;
    var leitura = $('ciclo-leitura');
    leitura.append(el('h3', 'foto__titulo', 'O que o TutorON leu (o aluno confere e confirma)'),
      el('p', 'caption', 'Confiança da leitura: ' + l.confianca + ' · tipo: ' + l.tipo.replace(/_/g, ' ')));
    var enun = el('details', 'disclosure');
    enun.append(el('summary', null, 'Enunciado lido (inclui a resolução impressa na folha)'), resposta(l.enunciado));
    leitura.append(enun, el('p', 'field__label', 'Tentativa do aluno, escrita à mão:'), resposta(l.tentativa));

    var conversa = $('ciclo-conversa');
    var proxima = 0;
    function mostrar() {
      var r = ciclo.rodadas[proxima];
      var item = el('article', 'troca');
      var rotulo = proxima === 0 ? 'Aluno: “' + ciclo.pergunta + '” · ajuda pedida: ' + NOMES[r.ajuda]
        : 'Aluno: “Ainda não consegui” · onde travou: “' + r.travou + '” → o tutor muda para: ' + NOMES[r.ajuda];
      item.append(el('p', 'demo__aluno', rotulo), resposta(r.texto), el('p', 'caption', 'Rodada ' + (proxima + 1) + ' · ' + r.modelo));
      conversa.append(item);
      proxima++;
      if (proxima >= ciclo.rodadas.length) {
        $('ciclo-proximo').hidden = true;
        conversa.append(el('p', 'caption', 'Três rodadas, três formas diferentes de explicar, e nenhuma escreveu a fórmula final. No site, o ciclo continua enquanto o aluno precisar.'));
      }
      if (proxima > 1) item.scrollIntoView({ block: 'start', behavior: 'smooth' });
    }
    $('ciclo-proximo').addEventListener('click', mostrar);
    mostrar();
  }

  // ------------------------------------------------------------------ 3. animações
  function montarVideos(videos) {
    var box = $('demo-videos');
    videos.forEach(function (v) {
      var fig = el('figure', 'animacao');
      var video = document.createElement('video');
      // WebM (VP9) primeiro: toca em qualquer navegador no Linux, mesmo sem codec H.264.
      var webm = v.arquivo.replace(/\.mp4$/, '.webm');
      if (EMBUTIDOS[webm]) {
        var s = document.createElement('source');
        s.src = EMBUTIDOS[webm];
        s.type = 'video/webm';
        video.append(s);
      }
      var mp4 = document.createElement('source');
      mp4.src = arquivo(v.arquivo);
      mp4.type = 'video/mp4';
      video.append(mp4);
      var poster = v.arquivo.replace(/\.mp4$/, '.png');
      if (EMBUTIDOS[poster]) video.poster = EMBUTIDOS[poster];
      video.controls = true;
      video.muted = true;
      video.playsInline = true;
      video.preload = 'metadata';
      video.setAttribute('aria-label', 'Animação: ' + v.titulo);
      var legenda = el('figcaption', 'caption');
      legenda.append(el('strong', null, v.disciplina + ' · “' + v.pergunta + '”'), document.createElement('br'),
        document.createTextNode('Sua vez: ' + v.pergunta_final));
      fig.append(video, legenda);
      box.append(fig);
    });
  }

  var dados = window.TUTORON_DEMO ? Promise.resolve(window.TUTORON_DEMO)
    : fetch('/static/demo/demo.json', { cache: 'no-cache' }).then(function (r) { return r.json(); });
  dados.then(function (demo) {
    $('sobre').textContent = demo.sobre;
    montarAjudas(demo.ajudas);
    montarCiclo(demo.ciclo);
    montarVideos(demo.animacoes);
  }).catch(function () {
    $('sobre').textContent = 'Não foi possível carregar a demonstração.';
  });
})();
