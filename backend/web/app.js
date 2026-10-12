(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };
  var R = window.TutorONRender;

  var SUGESTOES = [
    'Resolva T(n) = 2T(n/2) + n log n. O Teorema Mestre se aplica?',
    'Qual a diferença entre O, Ω e Θ? Dê um exemplo com 3n² + 5n.',
    'Por que o guloso de troco falha para moedas {1, 3, 4} e valor 6?',
    'Como montar a recorrência da mochila 0/1 em programação dinâmica?',
    'Como provar que um problema é NP-completo por redução?'
  ];

  // ------------------------------------------------------------------ utilidades
  function setStatus(el, text, tone) {
    el.textContent = text || '';
    if (tone) el.dataset.tone = tone; else delete el.dataset.tone;
  }

  async function postJSON(path, data) {
    var res;
    try {
      res = await fetch(path, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
    } catch (e) {
      throw new Error('Sem conexão com o servidor do TutorON. Verifique sua internet e tente de novo.');
    }
    var payload = {};
    try { payload = await res.json(); } catch (e) { /* sem JSON */ }
    if (!res.ok) throw new Error(payload.erro || 'O servidor respondeu com erro ' + res.status + '. Tente de novo.');
    return payload;
  }

  function el(tag, cls, text) {
    var node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text !== undefined) node.textContent = text;
    return node;
  }

  function sugestoes(boxId, textareaId) {
    var box = $(boxId);
    SUGESTOES.forEach(function (s) {
      var b = el('button', 'sugestao', s);
      b.type = 'button';
      b.addEventListener('click', function () { $(textareaId).value = s; $(textareaId).focus(); });
      box.append(b);
    });
  }

  // ------------------------------------------------------------------ modos
  function mostrarModo(modo) {
    var validacao = modo === 'validacao';
    $('modo-tutor').hidden = validacao;
    $('modo-validacao').hidden = !validacao;
    $('tab-tutor').setAttribute('aria-selected', String(!validacao));
    $('tab-validacao').setAttribute('aria-selected', String(validacao));
    var url = new URL(location.href);
    if (validacao) url.searchParams.set('modo', 'validacao'); else url.searchParams.delete('modo');
    history.replaceState(null, '', url);
  }
  $('tab-tutor').addEventListener('click', function () { mostrarModo('tutor'); });
  $('tab-validacao').addEventListener('click', function () { mostrarModo('validacao'); });
  mostrarModo(new URL(location.href).searchParams.get('modo') === 'validacao' ? 'validacao' : 'tutor');

  // ------------------------------------------------------------------ status dos modelos
  async function atualizarStatus() {
    try {
      var s = await (await fetch('/api/status')).json();
      var gemini = s.gemini && s.gemini.habilitado;
      var pausados = Object.keys(s.pausados || {}).filter(function (k) { return k.indexOf('gemini:') === 0; }).length;
      var total = gemini ? s.gemini.modelos.length : 0;
      var partes = [];
      if (gemini) partes.push('Gemini: ' + (total - pausados) + ' de ' + total + ' modelos disponíveis');
      partes.push('TutorON local: ' + (s.local && s.local.online ? 'ligado' : 'desligado'));
      $('model-status').textContent = partes.join(' · ');
    } catch (e) {
      $('model-status').textContent = '';
    }
  }
  atualizarStatus();
  setInterval(atualizarStatus, 30000);

  // ================================================================== MODO TUTOR
  sugestoes('sugestoes-tutor', 'pergunta');

  function fontesDetalhe(fontes) {
    var d = el('details', 'fontes disclosure');
    d.append(el('summary', null, 'Material consultado (' + fontes.length + ')'));
    var ul = el('ul', 'fontes__lista');
    fontes.forEach(function (f) {
      var li = el('li');
      li.append(el('strong', null, '[' + f.rotulo + '] '), document.createTextNode(f.titulo + ' — ' + f.referencia));
      ul.append(li);
    });
    d.append(ul);
    return d;
  }

  function botoesFeedback(id) {
    var box = el('div', 'feedback');
    box.append(el('span', 'caption', 'Esta resposta ajudou?'));
    var status = el('span', 'caption feedback__status');
    function botao(texto, dados) {
      var b = el('button', 'button button--secondary button--small', texto);
      b.type = 'button';
      b.addEventListener('click', async function () {
        box.querySelectorAll('button').forEach(function (x) { x.disabled = true; });
        try {
          await postJSON('/api/feedback', Object.assign({ id: id }, dados));
          status.textContent = 'Obrigado pelo retorno.';
        } catch (e) {
          status.textContent = e.message;
          box.querySelectorAll('button').forEach(function (x) { x.disabled = false; });
        }
      });
      return b;
    }
    box.append(botao('Ajudou', { util: true }), botao('Não ajudou', { util: false }),
      botao('Tem erro de conta', { util: false, erro_matematico: true }), status);
    return box;
  }

  var enviando = false;

  async function perguntar(pergunta, contexto) {
    var item = el('article', 'troca');
    var q = el('div', 'question prose');
    R.renderPlain(q, pergunta);
    var resposta = el('div', 'prose resposta');
    var meta = el('p', 'caption troca__meta', 'Procurando no material da disciplina…');
    item.append(q, resposta, meta);
    $('conversa').append(item);
    item.scrollIntoView({ block: 'start', behavior: 'smooth' });

    var texto = '';
    var agendado = false;
    var fontes = [];
    function desenhar() {
      agendado = false;
      R.render(resposta, texto);
    }
    function agendar() {
      if (!agendado) { agendado = true; setTimeout(desenhar, 120); }
    }

    var res;
    try {
      res = await fetch('/api/perguntar', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pergunta: pergunta, contexto: contexto || null })
      });
    } catch (e) {
      meta.textContent = 'Sem conexão com o servidor do TutorON. Tente de novo.';
      meta.dataset.tone = 'error';
      return false;
    }
    if (!res.ok) {
      var erro = {};
      try { erro = await res.json(); } catch (e) { /* sem JSON */ }
      meta.textContent = erro.erro || ('Erro ' + res.status + '. Tente de novo.');
      meta.dataset.tone = 'error';
      return false;
    }

    var reader = res.body.getReader();
    var decoder = new TextDecoder();
    var buffer = '';
    var fim = null;
    var modelo = '';
    for (;;) {
      var lido = await reader.read();
      if (lido.done) break;
      buffer += decoder.decode(lido.value, { stream: true });
      var blocos = buffer.split('\n\n');
      buffer = blocos.pop();
      blocos.forEach(function (bloco) {
        if (bloco.indexOf('data: ') !== 0) return;
        var ev;
        try { ev = JSON.parse(bloco.slice(6)); } catch (e) { return; }
        if (ev.tipo === 'fontes') {
          fontes = ev.fontes || [];
          meta.textContent = 'Escrevendo a resposta…';
        } else if (ev.tipo === 'aguarde') {
          meta.textContent = 'Os servidores do Gemini estão ocupados agora. O TutorON local está raciocinando sobre a resposta; pode levar cerca de um minuto.';
        } else if (ev.tipo === 'modelo') {
          modelo = ev.rotulo;
          meta.textContent = 'Respondendo com ' + modelo + '…';
        } else if (ev.tipo === 'texto') {
          texto += ev.texto;
          agendar();
        } else if (ev.tipo === 'reiniciar') {
          texto = '';
          agendar();
          meta.textContent = 'O modelo caiu no meio da resposta; tentando outro…';
        } else if (ev.tipo === 'fim') {
          fim = ev;
        } else if (ev.tipo === 'erro') {
          meta.textContent = ev.mensagem;
          meta.dataset.tone = 'error';
        }
      });
    }
    desenhar();
    if (fim) {
      meta.textContent = 'Respondido por ' + modelo + ' em ' + Math.round(fim.segundos) + ' s.';
      if (fontes.length) item.append(fontesDetalhe(fontes));
      item.append(botoesFeedback(fim.id));
      return true;
    }
    if (!meta.dataset.tone) {
      meta.textContent = 'A conexão caiu antes do fim da resposta. Tente de novo.';
      meta.dataset.tone = 'error';
    }
    return false;
  }

  $('form-tutor').addEventListener('submit', async function (e) {
    e.preventDefault();
    if (enviando) return;
    var pergunta = $('pergunta').value.trim();
    if (pergunta.length < 3) {
      setStatus($('status-tutor'), 'Escreva sua dúvida antes de enviar.', 'error');
      $('pergunta').focus();
      return;
    }
    enviando = true;
    $('enviar').disabled = true;
    setStatus($('status-tutor'), '');
    var contexto = $('contexto').value.trim();
    $('pergunta').value = '';
    $('contexto').value = '';
    try {
      var ok = await perguntar(pergunta, contexto);
      if (ok === false) { $('pergunta').value = pergunta; $('contexto').value = contexto; }
    } finally {
      enviando = false;
      $('enviar').disabled = false;
    }
  });
  $('pergunta').addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) $('form-tutor').requestSubmit();
  });

  // ================================================================== MODO VALIDAÇÃO
  sugestoes('sugestoes-validacao', 'v-pergunta');

  var CRITERIOS = [
    ['clareza', 'Clareza', 'Consigo acompanhar o raciocínio.'],
    ['confianca', 'Confiança', 'Parece correta, sem inventar nada.'],
    ['utilidade', 'Utilidade para a prova', 'Me ajudaria numa questão parecida.']
  ];
  var sessao = null;

  function montarNotas(lado) {
    var box = $('notas' + lado);
    CRITERIOS.forEach(function (c) {
      var nome = c[0] + '_' + lado;
      var fs = el('fieldset', 'scale');
      var legend = el('legend', 'scale__legend', c[1]);
      var hint = el('span', 'scale__hint caption', c[2]);
      hint.id = nome + '-dica';
      fs.setAttribute('aria-describedby', hint.id);
      var opts = el('div', 'scale__options');
      for (var n = 1; n <= 5; n++) {
        var label = el('label', 'pick');
        var input = document.createElement('input');
        input.type = 'radio';
        input.name = nome;
        input.value = String(n);
        input.setAttribute('aria-label', c[1] + ': ' + n + ' de 5');
        var face = el('span', null, String(n));
        face.setAttribute('aria-hidden', 'true');
        label.append(input, face);
        opts.append(label);
      }
      fs.append(legend, hint, opts);
      box.append(fs);
    });
    var erro = el('label', 'check');
    var cb = document.createElement('input');
    cb.type = 'checkbox';
    cb.name = 'erro_' + lado;
    erro.append(cb, el('span', null, 'Encontrei erro de conta ou de matemática nesta resposta'));
    box.append(erro);
  }
  montarNotas('A');
  montarNotas('B');

  $('v-gerar').addEventListener('click', async function () {
    var pergunta = $('v-pergunta').value.trim();
    if (pergunta.length < 3) {
      setStatus($('v-status'), 'Escreva sua dúvida antes de gerar as respostas.', 'error');
      $('v-pergunta').focus();
      return;
    }
    sessao = null;
    $('v-form').hidden = true;
    $('v-feito').hidden = true;
    var botao = $('v-gerar');
    botao.disabled = true;
    botao.textContent = 'Gerando…';
    setStatus($('v-status'), 'Gerando as duas respostas. Pode levar até um minuto; mantenha esta aba aberta.', 'busy');
    try {
      var dados = await postJSON('/api/comparar', { pergunta: pergunta });
      sessao = dados.sessao;
      $('v-form').reset();
      R.renderPlain($('v-escolhida'), dados.pergunta);
      R.render($('respostaA'), dados.A);
      R.render($('respostaB'), dados.B);
      setStatus($('v-status-envio'), '');
      $('v-enviar').disabled = false;
      $('v-form').hidden = false;
      setStatus($('v-status'), '');
      $('v-passo2-titulo').focus({ preventScroll: true });
      $('v-passo2').scrollIntoView({ behavior: 'smooth', block: 'start' });
    } catch (e) {
      setStatus($('v-status'), e.message, 'error');
    } finally {
      botao.disabled = false;
      botao.textContent = 'Gerar as duas respostas';
    }
  });

  function faltando(form) {
    for (var lado of ['A', 'B']) {
      for (var c of CRITERIOS) {
        if (!form.querySelector('input[name="' + c[0] + '_' + lado + '"]:checked')) {
          return { nome: c[0] + '_' + lado, msg: 'Falta a nota de ' + c[1].toLowerCase() + ' da resposta ' + lado + '.' };
        }
      }
    }
    if (!form.querySelector('input[name="preferida"]:checked')) {
      return { nome: 'preferida', msg: 'Escolha a resposta que você prefere, ou empate.' };
    }
    return null;
  }

  $('v-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    if (!sessao) return;
    var form = e.currentTarget;
    var falta = faltando(form);
    if (falta) {
      setStatus($('v-status-envio'), falta.msg, 'error');
      form.querySelector('input[name="' + falta.nome + '"]').focus();
      return;
    }
    var fd = new FormData(form);
    var lado = function (L) {
      return {
        clareza: Number(fd.get('clareza_' + L)), confianca: Number(fd.get('confianca_' + L)),
        utilidade: Number(fd.get('utilidade_' + L)), erro_matematico: fd.get('erro_' + L) === 'on'
      };
    };
    var dados = {
      sessao: sessao, preferida: fd.get('preferida'), A: lado('A'), B: lado('B'),
      comentario: $('v-comentario').value, curso: $('v-curso').value, periodo: $('v-periodo').value
    };
    $('v-enviar').disabled = true;
    setStatus($('v-status-envio'), 'Enviando…', 'busy');
    try {
      await postJSON('/api/avaliar', dados);
      sessao = null;
      form.hidden = true;
      setStatus($('v-status-envio'), '');
      $('v-feito').hidden = false;
      $('v-feito').focus({ preventScroll: true });
      $('v-feito').scrollIntoView({ block: 'center' });
    } catch (err) {
      setStatus($('v-status-envio'), err.message, 'error');
      $('v-enviar').disabled = false;
    }
  });

  $('v-outra').addEventListener('click', function () {
    $('v-feito').hidden = true;
    $('v-pergunta').value = '';
    $('v-passo1').scrollIntoView({ block: 'start' });
    $('v-pergunta').focus({ preventScroll: true });
  });
})();
