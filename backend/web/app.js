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

  function esperar(ms) { return new Promise(function (r) { setTimeout(r, ms); }); }

  async function postJSON(path, data) {
    var res, ultimoErro;
    // Até 3 tentativas para falhas de rede (celular trocando de antena, Wi-Fi da sala…).
    for (var i = 0; i < 3; i++) {
      try {
        res = await fetch(path, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
        break;
      } catch (e) {
        ultimoErro = e;
        await esperar(1500 * (i + 1));
      }
    }
    if (!res) throw new Error('Sem conexão com o TutorON. Verifique sua internet e tente de novo.');
    var payload = {};
    try { payload = await res.json(); } catch (e) { /* sem JSON */ }
    if (!res.ok) throw new Error(payload.erro || mensagemHttp(res.status));
    return payload;
  }

  function mensagemHttp(status) {
    if (status === 429) return 'Muitas perguntas em pouco tempo. Aguarde um minuto e tente de novo.';
    if (status >= 500) return 'O TutorON está reiniciando. Aguarde alguns segundos e tente de novo.';
    return 'Não foi possível enviar. Tente de novo.';
  }

  /* Acompanha uma tarefa até terminar. A resposta é gerada no servidor; aqui só
   * consultamos o andamento a cada segundo, com requisições curtas. Quedas de
   * rede não perdem a resposta: a consulta seguinte continua de onde parou. */
  async function acompanhar(id, aoAtualizar) {
    var falhasSeguidas = 0;
    for (;;) {
      var t = null;
      try {
        var res = await fetch('/api/tarefas/' + encodeURIComponent(id), { cache: 'no-store' });
        if (res.status === 404) {
          // O servidor foi reiniciado e a tarefa se perdeu: quem chamou reenvia a pergunta.
          return { status: 'perdida', mensagem: 'O TutorON foi reiniciado. Envie a pergunta de novo.' };
        }
        if (res.ok) t = await res.json();
      } catch (e) { /* rede oscilando: tenta de novo */ }
      if (t) {
        falhasSeguidas = 0;
        aoAtualizar(t);
        if (t.status === 'pronta' || t.status === 'erro') return t;
      } else if (++falhasSeguidas >= 120) {
        return { status: 'erro', mensagem: 'A conexão com o TutorON caiu. Verifique sua internet e envie de novo.' };
      }
      await esperar(t && t.status !== 'fila' ? 900 : 1200);
    }
  }

  function el(tag, cls, text) {
    var node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text !== undefined) node.textContent = text;
    return node;
  }

  function sugestoes(boxId, textareaId, lista) {
    var box = $(boxId);
    box.replaceChildren();
    (lista || SUGESTOES).forEach(function (s) {
      var b = el('button', 'sugestao', s);
      b.type = 'button';
      b.addEventListener('click', function () { $(textareaId).value = s; $(textareaId).focus(); });
      box.append(b);
    });
  }

  // Tarefa em andamento guardada na aba: recarregar a página retoma a resposta em vez de perdê-la.
  var PENDENTE = 'tutoron-pendente';
  function guardarPendente(dados) { try { sessionStorage.setItem(PENDENTE, JSON.stringify(dados)); } catch (e) { /* sem storage */ } }
  function lerPendente() { try { return JSON.parse(sessionStorage.getItem(PENDENTE) || 'null'); } catch (e) { return null; } }
  function limparPendente() { try { sessionStorage.removeItem(PENDENTE); } catch (e) { /* sem storage */ } }

  // Avisa antes de sair da página no meio de uma geração.
  var gerando = 0;
  window.addEventListener('beforeunload', function (e) {
    if (gerando > 0) { e.preventDefault(); e.returnValue = ''; }
  });

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

  // ================================================================== MODO TUTOR
  sugestoes('sugestoes-tutor', 'pergunta');

  /* Disciplinas: a mesma IA atende todas; a escolha só decide qual acervo é consultado.
   * Sem resposta do servidor, o seletor fica oculto e vale a disciplina padrão (PAA). */
  var disciplinas = {};
  function escolherDisciplina(id) {
    var d = disciplinas[id];
    if (!d) return;
    $('disciplina').value = id;
    sugestoes('sugestoes-tutor', 'pergunta', d.exemplos.length ? d.exemplos : null);
    if (d.exemplos.length) $('pergunta').placeholder = 'Ex.: ' + d.exemplos[0];
  }
  (async function carregarDisciplinas() {
    try {
      var res = await fetch('/api/disciplinas', { cache: 'no-store' });
      if (!res.ok) return;
      var dados = await res.json();
      dados.disciplinas.forEach(function (d) {
        disciplinas[d.id] = d;
        var indisponivel = d.disponivel === false;
        var nome = d.nome + ' (' + d.sigla + ')' + (indisponivel ? ' · em validação, indisponível'
          : (d.situacao && d.situacao !== 'MVP' ? ' · ' + d.situacao : ''));
        var opcao = el('option', null, nome);
        opcao.value = d.id;
        opcao.disabled = indisponivel;  // o servidor também recusa (403): isto só evita o clique
        $('disciplina').append(opcao);
      });
      $('disciplina-campo').hidden = dados.disciplinas.length < 2;
      var pedida = new URL(location.href).searchParams.get('disciplina');
      var aviso = $('disciplina-aviso');
      if (disciplinas[pedida] && disciplinas[pedida].disponivel === false) {
        aviso.textContent = disciplinas[pedida].nome + ' ainda está em validação e não está disponível para uso normal.';
        aviso.hidden = false;
        pedida = null;
      }
      escolherDisciplina(disciplinas[pedida] ? pedida : dados.padrao);
    } catch (e) { /* servidor antigo ou fora do ar: segue com a padrão */ }
  })();
  $('disciplina').addEventListener('change', function () {
    escolherDisciplina($('disciplina').value);
    var url = new URL(location.href);
    url.searchParams.set('disciplina', $('disciplina').value);
    history.replaceState(null, '', url);
  });

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

  function botoesFeedback(id, registro) {
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
          registro.voto = texto;
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

  /* Perguntas anteriores: ficam só na memória da página (recarregar zera).
   * A tela principal mostra apenas a pergunta atual; as anteriores vão para
   * uma lista recolhida, sem botões de retorno, para não votar na resposta errada. */
  var historico = [];  // da mais antiga para a mais recente
  var atual = null;    // { pergunta, texto, meta, fontes, voto, pronta }

  function rolarPara(node) {
    var reduzir = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    node.scrollIntoView({ block: 'start', behavior: reduzir ? 'auto' : 'smooth' });
  }

  function abrirHistorico(abrir) {
    $('historico').hidden = !abrir;
    $('historico-botao').setAttribute('aria-expanded', String(abrir));
    $('historico-botao').textContent = abrir ? 'Ocultar perguntas anteriores'
      : 'Ver perguntas anteriores (' + historico.length + ')';
  }
  $('historico-botao').addEventListener('click', function () { abrirHistorico($('historico').hidden); });

  function itemHistorico(r) {
    var li = el('li', 'historico__item');
    var d = el('details', 'disclosure');
    var resumo = r.pergunta.length > 160 ? r.pergunta.slice(0, 157).trimEnd() + '…' : r.pergunta;
    d.append(el('summary', null, resumo));
    var corpo = el('div', 'troca');
    // A resposta só é desenhada na primeira vez que o item é aberto.
    d.addEventListener('toggle', function () {
      if (!d.open || corpo.childElementCount) return;
      var q = el('div', 'question prose');
      R.renderPlain(q, r.pergunta);
      var resposta = el('div', 'prose resposta');
      R.render(resposta, r.texto);
      corpo.append(q, resposta, el('p', 'caption', r.meta));
      if (r.fontes && r.fontes.length) corpo.append(fontesDetalhe(r.fontes));
      if (r.voto) corpo.append(el('p', 'caption', 'Seu retorno: ' + r.voto + '.'));
    });
    d.append(corpo);
    li.append(d);
    return li;
  }

  // Tira a pergunta atual da tela principal. Só respostas prontas entram no histórico.
  function guardarAtualNoHistorico() {
    if (atual && atual.pronta) historico.push(atual);
    atual = null;
    var lista = $('historico');
    lista.replaceChildren.apply(lista, historico.slice().reverse().map(itemHistorico));
    $('historico-box').hidden = historico.length === 0;
    abrirHistorico(false);
  }

  var enviando = false;

  async function perguntar(pergunta, contexto, retomarId, disciplina) {
    guardarAtualNoHistorico();
    var registro = { pergunta: pergunta, texto: '', meta: '', fontes: [], voto: null, pronta: false };
    atual = registro;

    var item = el('article', 'troca');
    item.tabIndex = -1;
    item.setAttribute('aria-label', 'Sua dúvida e a resposta');
    var q = el('div', 'question prose');
    R.renderPlain(q, pergunta);
    var resposta = el('div', 'prose resposta');
    var meta = el('p', 'caption troca__meta status', 'Enviando…');
    meta.dataset.tone = 'busy';
    item.append(q, resposta, meta);
    $('conversa').replaceChildren(item);
    item.focus({ preventScroll: true });
    rolarPara(item);

    var desenhado = '';
    var final;
    var inicio = Date.now();
    for (var envio = 0; envio < 3; envio++) {
      var tarefa;
      if (retomarId && envio === 0) {
        tarefa = { id: retomarId };
      } else {
        try {
          tarefa = await postJSON('/api/perguntar', { pergunta: pergunta, contexto: contexto || null, disciplina: disciplina || null });
        } catch (e) {
          setStatus(meta, e.message, 'error');
          return false;
        }
      }
      guardarPendente({ tipo: 'tutor', id: tarefa.id, pergunta: pergunta, contexto: contexto || '', disciplina: disciplina || '' });
      final = await acompanhar(tarefa.id, function (t) {
        if (t.texto !== desenhado) {
          desenhado = t.texto;
          R.render(resposta, t.texto);
        }
        if (t.status !== 'pronta' && t.status !== 'erro') {
          setStatus(meta, t.mensagem || 'Escrevendo a resposta…', 'busy');
        }
      });
      if (final.status !== 'perdida') break;
      setStatus(meta, 'Reenviando a pergunta…', 'busy');
      await esperar(3000);
    }

    limparPendente();
    if (final.status === 'pronta') {
      R.render(resposta, final.texto);
      setStatus(meta, 'Respondido em ' + Math.max(1, Math.round((Date.now() - inicio) / 1000)) + ' s' +
        (final.rotulo ? ' · ' + final.rotulo : '') + '.');
      if (final.fontes && final.fontes.length) item.append(fontesDetalhe(final.fontes));
      item.append(botoesFeedback(final.id_resposta, registro));
      registro.texto = final.texto;
      registro.meta = meta.textContent;
      registro.fontes = final.fontes || [];
      registro.pronta = true;
      return true;
    }
    setStatus(meta, final.mensagem || 'Não foi possível gerar a resposta. Tente de novo.', 'error');
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
    gerando++;
    $('enviar').disabled = true;
    setStatus($('status-tutor'), '');
    var contexto = $('contexto').value.trim();
    var disciplina = $('disciplina').value;
    $('pergunta').value = '';
    $('contexto').value = '';
    try {
      var ok = await perguntar(pergunta, contexto, null, disciplina);
      if (!ok) { $('pergunta').value = pergunta; $('contexto').value = contexto; }
    } finally {
      enviando = false;
      gerando--;
      $('enviar').disabled = false;
    }
  });
  async function retomarTutor(p) {
    enviando = true;
    gerando++;
    $('enviar').disabled = true;
    try { await perguntar(p.pergunta, p.contexto, p.id, p.disciplina); } finally {
      enviando = false;
      gerando--;
      $('enviar').disabled = false;
    }
  }

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
  var gerandoPar = false;

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

  $('v-gerar').addEventListener('click', function () { gerarPar(null); });

  async function gerarPar(retomarId) {
    if (gerandoPar) return;
    var pergunta = $('v-pergunta').value.trim();
    if (pergunta.length < 3) {
      setStatus($('v-status'), 'Escreva sua dúvida antes de gerar as respostas.', 'error');
      $('v-pergunta').focus();
      return;
    }
    gerandoPar = true;
    gerando++;
    sessao = null;
    $('v-form').hidden = true;
    $('v-feito').hidden = true;
    var botao = $('v-gerar');
    botao.disabled = true;
    botao.textContent = 'Gerando…';
    setStatus($('v-status'), 'Gerando as duas respostas. Mantenha esta aba aberta.', 'busy');
    try {
      var inicio = Date.now();
      var dados;
      for (var envio = 0; envio < 3; envio++) {
        var tarefa = (retomarId && envio === 0) ? { id: retomarId } : await postJSON('/api/comparar', { pergunta: pergunta });
        guardarPendente({ tipo: 'validacao', id: tarefa.id, pergunta: pergunta });
        dados = await acompanhar(tarefa.id, function (t) {
          if (t.status === 'pronta' || t.status === 'erro') return;
          var s = Math.round((Date.now() - inicio) / 1000);
          setStatus($('v-status'), (t.mensagem || 'Gerando as duas respostas…') + ' (' + s + ' s)', 'busy');
        });
        if (dados.status !== 'perdida') break;
        setStatus($('v-status'), 'Reenviando a pergunta…', 'busy');
        await esperar(3000);
      }
      if (dados.status !== 'pronta') {
        limparPendente();
        throw new Error(dados.mensagem || 'Não foi possível gerar as respostas. Tente de novo.');
      }
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
      gerandoPar = false;
      gerando--;
      botao.disabled = false;
      botao.textContent = 'Gerar as duas respostas';
    }
  }

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
      limparPendente();
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

  // Página recarregada no meio de uma geração (ou antes de votar): retoma de onde parou.
  var pendente = lerPendente();
  if (pendente && pendente.id) {
    if (pendente.tipo === 'validacao') {
      mostrarModo('validacao');
      $('v-pergunta').value = pendente.pergunta || '';
      gerarPar(pendente.id);
    } else if (pendente.tipo === 'tutor') {
      mostrarModo('tutor');
      retomarTutor(pendente);
    }
  }

  $('v-outra').addEventListener('click', function () {
    $('v-feito').hidden = true;
    $('v-pergunta').value = '';
    $('v-passo1').scrollIntoView({ block: 'start' });
    $('v-pergunta').focus({ preventScroll: true });
  });
})();
