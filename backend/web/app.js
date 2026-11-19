(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };
  var R = window.TutorONRender;
  var LOGO = '/static/marca/logo.svg';

  var SUGESTOES = [
    'Resolva T(n) = 2T(n/2) + n log n. O Teorema Mestre se aplica?',
    'Como simplifico S(A,B,C) = Σm(0,1,3,5,7) com mapa de Karnaugh?',
    'Qual a diferença entre O, Ω e Θ? Dê um exemplo com 3n² + 5n.',
    'Por que lw x9, 32(x22) acessa A[8]?'
  ];

  // ------------------------------------------------------------------ utilidades
  function setStatus(node, text, tone) {
    node.textContent = text || '';
    if (tone) node.dataset.tone = tone; else delete node.dataset.tone;
  }
  function esperar(ms) { return new Promise(function (r) { setTimeout(r, ms); }); }
  function el(tag, cls, text) {
    var node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text !== undefined) node.textContent = text;
    return node;
  }
  function svg(path) {
    // O parser de HTML cria o <svg> no namespace certo (os caminhos são constantes deste arquivo).
    var t = document.createElement('template');
    t.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="' + path + '"/></svg>';
    return t.content.firstChild;
  }
  var ICONES = {
    copiar: 'M9 9h10v12H9zM5 15V3h10',
    ok: 'M7 11v9H4v-9zM7 11l4-8a2 2 0 0 1 3 2l-1 5h6a2 2 0 0 1 2 2.3l-1.4 7A2 2 0 0 1 17.6 21H7',
    nao: 'M17 13V4h3v9zM17 13l-4 8a2 2 0 0 1-3-2l1-5H5a2 2 0 0 1-2-2.3l1.4-7A2 2 0 0 1 6.4 3H17',
    erro: 'M12 3l10 18H2zM12 10v4M12 17.5v.5',
    olho: 'M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12zM12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6z',
    outra: 'M4 4v6h6M20 20v-6h-6M5.5 15a7 7 0 0 0 12.2 2M18.5 9A7 7 0 0 0 6.3 7',
    feito: 'M5 12l4 4 10-10'
  };

  // Navegador → servidor. Erro 402 = limite do dia acabou: abre os planos.
  async function postJSON(path, data) {
    var res;
    for (var i = 0; i < 3; i++) {  // falhas de rede (celular trocando de antena, Wi-Fi da sala…)
      try {
        res = await fetch(path, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
        break;
      } catch (e) { await esperar(1500 * (i + 1)); }
    }
    if (!res) throw new Error('Sem conexão com o TutorON. Verifique sua internet e tente de novo.');
    var payload = {};
    try { payload = await res.json(); } catch (e) { /* sem JSON */ }
    atualizarCota();
    if (res.status === 402) abrirPlanos(payload.erro);
    if (res.status === 401) location.href = '/entrar?voltar=' + encodeURIComponent(location.pathname + location.search);
    if (!res.ok) throw new Error(payload.erro || mensagemHttp(res.status));
    return payload;
  }
  function mensagemHttp(status) {
    if (status === 429) return 'Muitas perguntas em pouco tempo. Aguarde um minuto e tente de novo.';
    if (status >= 500) return 'O TutorON está reiniciando. Aguarde alguns segundos e tente de novo.';
    return 'Não foi possível enviar. Tente de novo.';
  }

  /* Acompanha uma tarefa até terminar. A resposta é gerada no servidor; aqui só consultamos o
   * andamento com requisições curtas. Quedas de rede não perdem a resposta. */
  async function acompanhar(id, aoAtualizar) {
    var falhasSeguidas = 0;
    for (;;) {
      var t = null;
      try {
        var res = await fetch('/api/tarefas/' + encodeURIComponent(id), { cache: 'no-store' });
        if (res.status === 404) return { status: 'perdida', mensagem: 'O TutorON foi reiniciado. Envie a pergunta de novo.' };
        if (res.ok) t = await res.json();
      } catch (e) { /* rede oscilando: tenta de novo */ }
      if (t) {
        falhasSeguidas = 0;
        aoAtualizar(t);
        if (t.status === 'pronta' || t.status === 'erro') return t;
      } else if (++falhasSeguidas >= 120) {
        return { status: 'erro', mensagem: 'A conexão com o TutorON caiu. Verifique sua internet e envie de novo.' };
      }
      await esperar(t && t.status !== 'fila' ? 700 : 1200);
    }
  }

  // Tarefa em andamento guardada na aba: recarregar a página retoma a resposta em vez de perdê-la.
  var PENDENTE = 'tutoron-pendente';
  function guardarPendente(dados) { try { sessionStorage.setItem(PENDENTE, JSON.stringify(dados)); } catch (e) { /* sem storage */ } }
  function lerPendente() { try { return JSON.parse(sessionStorage.getItem(PENDENTE) || 'null'); } catch (e) { return null; } }
  function limparPendente() { try { sessionStorage.removeItem(PENDENTE); } catch (e) { /* sem storage */ } }

  var gerando = 0;
  window.addEventListener('beforeunload', function (e) { if (gerando > 0) { e.preventDefault(); e.returnValue = ''; } });

  function rolarFim() {
    var r = $('rolagem');
    r.scrollTop = r.scrollHeight;
  }

  // ------------------------------------------------------------------ barra lateral (celular)
  function abrirLateral(abrir) {
    $('lateral').classList.toggle('aberta', abrir);
    $('veu').hidden = !abrir;
  }
  $('abrir-lateral').addEventListener('click', function () { abrirLateral(true); });
  $('fechar-lateral').addEventListener('click', function () { abrirLateral(false); });
  $('veu').addEventListener('click', function () { abrirLateral(false); });

  // ------------------------------------------------------------------ modos
  function mostrarModo(modo) {
    var validacao = modo === 'validacao';
    $('modo-tutor').hidden = validacao;
    $('modo-validacao').hidden = !validacao;
    if (validacao) { $('tab-validacao').setAttribute('aria-current', 'page'); $('tab-tutor').removeAttribute('aria-current'); }
    else { $('tab-tutor').setAttribute('aria-current', 'page'); $('tab-validacao').removeAttribute('aria-current'); }
    var url = new URL(location.href);
    if (validacao) url.searchParams.set('modo', 'validacao'); else url.searchParams.delete('modo');
    history.replaceState(null, '', url);
    abrirLateral(false);
  }
  $('tab-tutor').addEventListener('click', function () { mostrarModo('tutor'); });
  $('tab-validacao').addEventListener('click', function () { mostrarModo('validacao'); });
  mostrarModo(new URL(location.href).searchParams.get('modo') === 'validacao' ? 'validacao' : 'tutor');

  // ================================================================== COTA E PLANOS
  var cotaAtual = null;
  function fmt(n) { return Number(n).toLocaleString('pt-BR'); }
  async function atualizarCota() {
    try {
      var c = await (await fetch('/api/cota', { cache: 'no-store' })).json();
      cotaAtual = c;
      var card = $('cota');
      var selo = $('selo-modo');
      card.classList.toggle('pago', c.plano !== 'gratis' && c.plano !== 'dev');
      selo.classList.toggle('admin', !!c.admin);
      if (c.admin) {
        $('cota-plano').textContent = 'Administrador';
        $('cota-acao').textContent = 'Planos';
        $('cota-texto').textContent = 'Sem limite · modo completo';
        $('cota-barra').style.width = '100%';
        selo.textContent = 'ADM · modo completo';
        selo.hidden = false;
        card.classList.remove('esgotado');
        return;
      }
      $('cota-plano').textContent = 'Plano ' + (c.plano_nome || 'Grátis');
      $('cota-acao').textContent = c.plano === 'gratis' ? 'Fazer upgrade' : 'Gerenciar';
      selo.hidden = c.modo !== 'completo';
      selo.textContent = 'Modo completo';
      if (c.ilimitado) { $('cota-texto').textContent = 'Sem limite neste servidor'; $('cota-barra').style.width = '100%'; return; }
      var pct = Math.max(0, Math.round(100 * c.restantes / c.limite));
      $('cota-barra').style.width = pct + '%';
      var quando = c.diaria ? 'renova à meia-noite' : 'renova às ' +
        new Date(c.renova_em * 1000).toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
      $('cota-texto').textContent = c.restantes > 0 ? (pct + '% do limite de hoje · ' + quando) : ('Limite de hoje esgotado · ' + quando);
      card.classList.toggle('esgotado', c.restantes <= 0);
    } catch (e) { /* sem cota: segue normal */ }
  }
  window.TutorONCota = atualizarCota;
  atualizarCota();
  setInterval(atualizarCota, 30000);

  function fecharJanelas(e) {
    var j = e.target.closest('dialog');
    if (j) j.close();
  }
  document.querySelectorAll('[data-fechar]').forEach(function (b) { b.addEventListener('click', fecharJanelas); });

  function preco(p) {
    if (p.preco_mes === null) return 'Sob consulta';
    if (p.preco_mes === 0) return 'R$ 0';
    return 'R$ ' + p.preco_mes.toFixed(2).replace('.', ',');
  }

  async function abrirPlanos(motivo) {
    await atualizarCota();
    var c = cotaAtual || { planos: [], plano: 'gratis' };
    $('planos-motivo').textContent = motivo || (c.admin ? 'Você está no modo administrador: sem limite. Os planos abaixo são para os alunos.' :
      'Escolha o plano que combina com a sua rotina de estudos.');
    var grade = $('planos-grade');
    grade.replaceChildren();
    (c.planos || []).forEach(function (p) {
      var atual = c.plano === p.id;
      var card = el('article', 'plano' + (p.destaque ? ' destaque' : '') + (atual ? ' atual' : ''));
      if (p.destaque) card.append(el('span', 'plano__selo', 'MAIS ESCOLHIDO'));
      card.append(el('h3', null, p.nome));
      var pr = el('div', 'plano__preco', preco(p));
      if (p.preco_mes) pr.append(el('small', null, ' /mês'));
      card.append(pr, el('p', 'plano__desc', p.descricao));
      var ul = el('ul');
      if (p.tokens_dia) ul.append(el('li', null, fmt(p.tokens_dia) + ' tokens por dia'));
      (p.recursos || []).forEach(function (r) { ul.append(el('li', null, r)); });
      card.append(ul);
      var b = el('button', 'botao' + (atual || !p.preco_mes ? ' botao--leve' : ''));
      b.type = 'button';
      if (atual && p.preco_mes) {
        b.textContent = 'Cancelar plano';
        b.addEventListener('click', async function () {
          b.disabled = true;
          try { await postJSON('/api/planos/cancelar', {}); abrirPlanos('Plano cancelado. Você voltou para o Grátis.'); }
          catch (e) { b.disabled = false; }
        });
      } else if (atual) {
        b.textContent = 'Seu plano atual'; b.disabled = true;
      } else if (p.preco_mes === null) {
        b.textContent = 'Falar com a equipe'; b.disabled = true;
      } else if (!p.preco_mes) {
        b.textContent = 'Incluído'; b.disabled = true;
      } else {
        b.textContent = 'Assinar ' + p.nome;
        b.addEventListener('click', function () { abrirCheckout(p); });
      }
      card.append(b);
      grade.append(card);
    });
    abrirLateral(false);
    if (!$('janela-planos').open) $('janela-planos').showModal();
  }
  document.querySelectorAll('[data-abrir-planos]').forEach(function (a) {
    a.addEventListener('click', function (e) { e.preventDefault(); abrirPlanos(); });
  });
  if (location.hash === '#planos') abrirPlanos();

  /* Checkout SIMULADO: o número do cartão é validado aqui (Luhn) e nunca é enviado; o servidor
   * recebe só o plano e os 4 últimos dígitos. Nenhum valor é cobrado. */
  var planoEscolhido = null;
  function luhn(num) {
    var soma = 0, dobra = false;
    for (var i = num.length - 1; i >= 0; i--) {
      var d = Number(num[i]);
      if (dobra) { d *= 2; if (d > 9) d -= 9; }
      soma += d; dobra = !dobra;
    }
    return num.length >= 13 && soma % 10 === 0;
  }
  function bandeira(num) {
    if (/^4/.test(num)) return 'VISA';
    if (/^(5[1-5]|2[2-7])/.test(num)) return 'mastercard';
    if (/^3[47]/.test(num)) return 'AMEX';
    if (/^(4011|4312|4389|5041|5066|5067|509|6277|6362|6363|650|6516|6550)/.test(num)) return 'elo';
    return '';
  }
  function abrirCheckout(p) {
    planoEscolhido = p;
    $('form-checkout').reset();
    $('checkout-titulo').textContent = 'Assinar o plano ' + p.nome;
    $('checkout-resumo').textContent = preco(p) + ' por mês · ' + fmt(p.tokens_dia) + ' tokens por dia · modo completo. Cancele quando quiser.';
    ['cv-numero', 'cv-nome', 'cv-validade', 'cv-bandeira'].forEach(function (id) { $(id).textContent = ''; });
    $('cv-numero').textContent = '•••• •••• •••• ••••';
    $('cv-nome').textContent = 'NOME NO CARTÃO';
    $('cv-validade').textContent = 'MM/AA';
    setStatus($('checkout-status'), '');
    $('checkout-pagar').disabled = false;
    $('checkout-pagar').textContent = 'Pagar ' + preco(p) + ' (simulado)';
    $('janela-checkout').showModal();
    $('cc-numero').focus();
  }
  $('cc-numero').addEventListener('input', function () {
    var n = this.value.replace(/\D/g, '').slice(0, 19);
    this.value = n.replace(/(.{4})/g, '$1 ').trim();
    $('cv-numero').textContent = (n + '•'.repeat(Math.max(0, 16 - n.length))).replace(/(.{4})/g, '$1 ').trim();
    $('cv-bandeira').textContent = bandeira(n);
  });
  $('cc-nome').addEventListener('input', function () { $('cv-nome').textContent = this.value.toUpperCase() || 'NOME NO CARTÃO'; });
  $('cc-validade').addEventListener('input', function () {
    var v = this.value.replace(/\D/g, '').slice(0, 4);
    this.value = v.length > 2 ? v.slice(0, 2) + '/' + v.slice(2) : v;
    $('cv-validade').textContent = this.value || 'MM/AA';
  });
  $('cc-cvv').addEventListener('input', function () { this.value = this.value.replace(/\D/g, '').slice(0, 4); });
  $('form-checkout').addEventListener('submit', async function (e) {
    e.preventDefault();
    var num = $('cc-numero').value.replace(/\D/g, '');
    var val = $('cc-validade').value.split('/');
    var mes = Number(val[0]), ano = 2000 + Number(val[1]);
    var hoje = new Date();
    var erro = !luhn(num) ? 'Número de cartão inválido. Para testar, use 4242 4242 4242 4242.' :
      $('cc-nome').value.trim().length < 3 ? 'Escreva o nome impresso no cartão.' :
      !(mes >= 1 && mes <= 12 && val[1] && val[1].length === 2) ? 'Validade inválida (use MM/AA).' :
      (ano < hoje.getFullYear() || (ano === hoje.getFullYear() && mes < hoje.getMonth() + 1)) ? 'Este cartão está vencido.' :
      !/^\d{3,4}$/.test($('cc-cvv').value) ? 'CVV inválido.' : '';
    if (erro) { setStatus($('checkout-status'), erro, 'error'); return; }
    $('checkout-pagar').disabled = true;
    setStatus($('checkout-status'), 'Processando pagamento (simulado)…', 'busy');
    await esperar(1400);
    try {
      await postJSON('/api/planos/ativar', { plano: planoEscolhido.id, final_cartao: num.slice(-4) });
      var corpo = $('form-checkout');
      var ok = el('div', 'sucesso');
      ok.append(el('div', 'sucesso__icone', '✓'), el('h2', null, 'Plano ' + planoEscolhido.nome + ' ativado!'),
        el('p', 'dica', 'Cartão final ' + num.slice(-4) + ' · pagamento simulado, nada foi cobrado. O modo completo já está valendo nesta conversa.'));
      var fechar = el('button', 'botao', 'Começar a estudar');
      fechar.type = 'button';
      fechar.addEventListener('click', function () { $('janela-checkout').close(); $('janela-planos').close(); $('pergunta').focus(); });
      ok.append(fechar);
      corpo.hidden = true;
      corpo.parentNode.append(ok);
      $('janela-checkout').addEventListener('close', function limpar() {
        ok.remove(); corpo.hidden = false; $('janela-checkout').removeEventListener('close', limpar);
      });
    } catch (err) {
      setStatus($('checkout-status'), err.message, 'error');
      $('checkout-pagar').disabled = false;
    }
  });

  // ================================================================== CURSO E PERÍODO
  /* Guardado num cookie simples (não é dado pessoal): curso:período. */
  var cursos = { cursos: [] };
  var perfil = lerPerfil();
  function lerPerfil() {
    var m = document.cookie.match(/(?:^|; )tutoron_perfil=([a-z]+):(\d+)/);
    return m ? { curso: m[1], periodo: Number(m[2]) } : null;
  }
  function salvarPerfil(p) {
    perfil = p;
    document.cookie = 'tutoron_perfil=' + (p ? p.curso + ':' + p.periodo : '') + '; path=/; max-age=' +
      (p ? 400 * 86400 : 0) + '; samesite=lax';
    mostrarPerfil();
  }
  function cursoAtual() { return perfil && cursos.cursos.find(function (c) { return c.id === perfil.curso; }); }
  function disciplinasDoPeriodo() {
    var c = cursoAtual();
    if (!c) return [];
    var p = c.periodos.find(function (x) { return x.numero === perfil.periodo; });
    return p ? p.disciplinas : [];
  }
  function mostrarPerfil() {
    var c = cursoAtual();
    $('perfil-curso').textContent = c ? c.nome : 'Escolha seu curso';
    $('perfil-periodo').textContent = c ? perfil.periodo + 'º período' : 'e o período';
    $('contexto-rotulo').textContent = c ? 'TutorON · ' + c.sigla + ' ' + perfil.periodo + 'º período' : 'TutorON · escolher curso';
    montarSugestoes();
  }
  var rascunho = null;
  function desenharJanelaPerfil() {
    var box = $('cursos');
    box.replaceChildren();
    cursos.cursos.forEach(function (c) {
      var b = el('button', 'curso');
      b.type = 'button';
      b.setAttribute('role', 'radio');
      b.setAttribute('aria-checked', String(rascunho.curso === c.id));
      b.append(el('strong', null, c.nome), el('small', null, 'PPC ' + c.ppc + ' · ' + c.periodos.length + ' períodos'));
      b.addEventListener('click', function () {
        rascunho.curso = c.id;
        if (!c.periodos.some(function (p) { return p.numero === rascunho.periodo; })) rascunho.periodo = 1;
        desenharJanelaPerfil();
      });
      box.append(b);
    });
    var c = cursos.cursos.find(function (x) { return x.id === rascunho.curso; });
    var per = $('periodos');
    per.replaceChildren();
    (c ? c.periodos : []).forEach(function (p) {
      var b = el('button', 'periodo-btn', p.numero + 'º');
      b.type = 'button';
      b.setAttribute('role', 'radio');
      b.setAttribute('aria-checked', String(rascunho.periodo === p.numero));
      b.setAttribute('aria-label', p.numero + 'º período');
      b.addEventListener('click', function () { rascunho.periodo = p.numero; desenharJanelaPerfil(); });
      per.append(b);
    });
    var grade = $('grade-disc');
    grade.replaceChildren();
    var p = c && c.periodos.find(function (x) { return x.numero === rascunho.periodo; });
    if (p) {
      if (!p.disciplinas.length) grade.append(el('p', null, 'Neste período a matriz só tem eletivas, estágio ou TCC. O TutorON continua atendendo todas as disciplinas com material.'));
      p.disciplinas.forEach(function (d) {
        var s = el('span', d.acervo ? 'tem' : '', d.nome + (d.acervo ? ' ✓' : ''));
        s.title = d.acervo ? 'O TutorON tem material curado desta disciplina' : 'Sem material curado ainda: o tutor responde com conhecimento geral';
        grade.append(s);
      });
      if (p.disciplinas.some(function (d) { return d.acervo; })) grade.append(el('p', null, '✓ = disciplina com material do curso no TutorON.'));
    }
  }
  function abrirPerfil() {
    rascunho = { curso: perfil ? perfil.curso : (cursos.padrao || 'ecom'), periodo: perfil ? perfil.periodo : 1 };
    desenharJanelaPerfil();
    abrirLateral(false);
    $('janela-perfil').showModal();
  }
  $('perfil-botao').addEventListener('click', abrirPerfil);
  $('contexto-botao').addEventListener('click', abrirPerfil);
  $('janela-perfil').addEventListener('close', function () {
    if ($('janela-perfil').returnValue === 'ok' && rascunho) salvarPerfil({ curso: rascunho.curso, periodo: rascunho.periodo });
    else if (!perfil) { try { sessionStorage.setItem('tutoron-perfil-pulado', '1'); } catch (e) { /* sem storage */ } }
  });
  (async function carregarCursos() {
    try {
      var res = await fetch('/api/cursos');
      if (!res.ok) return;
      cursos = await res.json();
      $('fonte-matriz').textContent = 'Fonte: matrizes obrigatórias dos projetos pedagógicos do Instituto de Computação (sem eletivas).';
      mostrarPerfil();
      var pulou = false;
      try { pulou = !!sessionStorage.getItem('tutoron-perfil-pulado'); } catch (e) { /* sem storage */ }
      if (!perfil && !pulou && !lerPendente()) abrirPerfil();
    } catch (e) { /* servidor antigo: segue sem perfil */ }
  })();

  // ================================================================== MODO TUTOR
  /* Sugestões: do período escolhido (disciplinas com material) ou da disciplina selecionada. */
  function montarSugestoes() {
    var box = $('sugestoes-tutor');
    var lista = [];
    var escolhida = disciplinas[$('disciplina').value];
    if (escolhida) {
      lista = escolhida.exemplos.slice(0, 4).map(function (s) { return [escolhida.sigla, s]; });
    } else {
      // Uma sugestão de cada disciplina do período, em rodízio.
      var doPeriodo = disciplinasDoPeriodo().filter(function (d) { return d.acervo && disciplinas[d.acervo]; })
        .map(function (d) { return disciplinas[d.acervo]; });
      for (var i = 0; i < 4 && doPeriodo.length; i++) {
        doPeriodo.forEach(function (D) { if (D.exemplos[i]) lista.push([D.sigla, D.exemplos[i]]); });
      }
      if (!lista.length) lista = SUGESTOES.map(function (s) { return ['', s]; });
    }
    box.replaceChildren();
    lista.slice(0, 4).forEach(function (par) {
      var b = el('button', 'sugestao');
      b.type = 'button';
      if (par[0]) b.append(el('small', null, par[0]));
      b.append(document.createTextNode(par[1]));
      b.addEventListener('click', function () { $('pergunta').value = par[1]; ajustarAltura(); $('pergunta').focus(); });
      box.append(b);
    });
  }

  /* Menus dos chips (tipo de ajuda e disciplina). */
  function ligarMenu(botaoId, menuId) {
    var b = $(botaoId), m = $(menuId);
    b.addEventListener('click', function (e) {
      e.stopPropagation();
      var abrir = m.hidden;
      fecharMenus();
      m.hidden = !abrir;
      b.setAttribute('aria-expanded', String(abrir));
    });
    m.addEventListener('click', function (e) { e.stopPropagation(); });
  }
  function fecharMenus() {
    [['ajuda-botao', 'ajudas'], ['disciplina-chip', 'disciplina-menu']].forEach(function (par) {
      $(par[1]).hidden = true;
      $(par[0]).setAttribute('aria-expanded', 'false');
    });
  }
  ligarMenu('ajuda-botao', 'ajudas');
  ligarMenu('disciplina-chip', 'disciplina-menu');
  document.addEventListener('click', fecharMenus);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') fecharMenus(); });

  /* Tipo de ajuda: o TutorON não entrega a resposta; o aluno escolhe COMO quer ser ajudado. */
  var AJUDAS_PADRAO = [['auto', 'O tutor escolhe'], ['pista', 'Uma pista'], ['perguntas', 'Perguntas-guia'],
    ['conceito', 'Explicar o conceito'], ['exemplo', 'Exemplo parecido'], ['conferir', 'Conferir meu raciocínio'],
    ['visual', 'Desenho/esquema']];
  var animacaoDisponivel = null;
  function montarAjudas(lista) {
    lista = lista.filter(function (a) { return a[0] !== 'animacao'; }).concat([['animacao', 'Só animação']]);
    var box = $('ajudas-opcoes');
    var anterior = document.querySelector('input[name="ajuda"]:checked');
    var escolhida = anterior ? anterior.value : null;
    box.replaceChildren();
    lista.forEach(function (a, i) {
      var label = el('label', 'opcao');
      var input = document.createElement('input');
      input.type = 'radio';
      input.name = 'ajuda';
      input.value = a[0];
      input.checked = escolhida ? a[0] === escolhida : i === 0;
      input.addEventListener('change', function () { mostrarAjuda(); fecharMenus(); });
      label.append(input, el('span', null, a[1]));
      box.append(label);
    });
    mostrarAjuda();
  }
  function mostrarAjuda() {
    var marcado = document.querySelector('input[name="ajuda"]:checked');
    var nome = marcado ? marcado.parentNode.textContent : 'O tutor escolhe';
    $('ajuda-rotulo').textContent = nome;
    $('ajuda-botao').classList.toggle('ativo', !!marcado && marcado.value !== 'auto');
  }
  montarAjudas(AJUDAS_PADRAO);
  (async function carregarAjudas() {
    try {
      var res = await fetch('/api/ajudas', { cache: 'no-store' });
      if (!res.ok) return;
      var dados = await res.json();
      montarAjudas(dados.ajudas.map(function (a) { return [a.id, a.nome]; }));
      animacaoDisponivel = !!dados.animacao;
    } catch (e) { /* servidor antigo: fica a lista padrão */ }
  })();
  function ajudaEscolhida() {
    var marcado = document.querySelector('input[name="ajuda"]:checked');
    return marcado ? marcado.value : 'auto';
  }

  /* Código ou enunciado colado (opcional). */
  $('codigo-botao').addEventListener('click', function () {
    var abrir = $('contexto-box').hidden;
    $('contexto-box').hidden = !abrir;
    this.setAttribute('aria-pressed', String(abrir));
    if (abrir) $('contexto').focus();
  });

  /* Caixa de texto que cresce com o conteúdo; Enter envia, Shift+Enter quebra a linha. */
  function ajustarAltura() {
    var t = $('pergunta');
    t.style.height = 'auto';
    t.style.height = Math.min(t.scrollHeight, 220) + 'px';
  }
  $('pergunta').addEventListener('input', ajustarAltura);
  $('pergunta').addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey && !e.isComposing) {
      e.preventDefault();
      $('form-tutor').requestSubmit();
    }
  });

  /* Foto do papel: a IA transcreve, o aluno CONFERE e corrige, e só então a leitura vai para o tutor. */
  var fotoConfirmada = null;
  var versaoFoto = 0;
  var lendoFoto = false;

  // Reduz no celular antes de enviar (fotos de 12 MP passam de 5 MB); 2400 px mantém a letra legível.
  function comprimir(arquivo) {
    return new Promise(function (ok, falha) {
      var url = URL.createObjectURL(arquivo);
      var img = new Image();
      img.onload = function () {
        var escala = Math.min(1, 2400 / Math.max(img.naturalWidth, img.naturalHeight));
        var c = document.createElement('canvas');
        c.width = Math.round(img.naturalWidth * escala);
        c.height = Math.round(img.naturalHeight * escala);
        try {
          var ctx = c.getContext('2d');
          ctx.fillStyle = '#fff';  // PNG transparente vira JPEG com fundo branco
          ctx.fillRect(0, 0, c.width, c.height);
          ctx.drawImage(img, 0, 0, c.width, c.height);
          ok(c.toDataURL('image/jpeg', 0.9));
        } catch (e) {
          falha(new Error('Não consegui preparar esta imagem. Tente outra foto.'));
        } finally {
          URL.revokeObjectURL(url);
        }
      };
      img.onerror = function () { URL.revokeObjectURL(url); falha(new Error('Não consegui abrir esta imagem.')); };
      img.src = url;
    });
  }

  function mostrarLeitura(leitura, dataUrl) {
    $('foto-previa').src = dataUrl;
    var conf = $('foto-confianca');
    var nomes = { alta: 'alta', media: 'média', baixa: 'baixa' };
    conf.textContent = 'Confiança da leitura: ' + (nomes[leitura.confianca] || 'baixa') +
      (leitura.legivel ? '' : ' — a foto parece ilegível; tente outra com mais luz e o papel inteiro no quadro.');
    conf.className = 'dica' + (leitura.confianca === 'baixa' ? ' confianca--baixa' : '');
    $('foto-enunciado').value = leitura.enunciado || '';
    $('foto-tentativa').value = leitura.tentativa || '';
    var duvidas = $('foto-duvidas-lista');
    duvidas.replaceChildren.apply(duvidas, (leitura.duvidas || []).map(function (d) { return el('li', null, d); }));
    $('foto-duvidas').hidden = !(leitura.duvidas || []).length;
    var subs = $('foto-subtopicos');
    subs.replaceChildren();
    (leitura.subtopicos || []).forEach(function (s, i) {
      var label = el('label', 'check');
      var cb = document.createElement('input');
      cb.type = 'checkbox';
      cb.checked = true;
      cb.value = s;
      cb.id = 'sub-' + i;
      label.append(cb, el('span', null, s));
      subs.append(label);
    });
    $('foto-subtopicos-box').hidden = !(leitura.subtopicos || []).length;
    var reg = $('foto-regioes');
    reg.replaceChildren.apply(reg, (leitura.regioes || []).map(function (r) {
      var li = el('li');
      li.append(el('strong', null, r.onde + ': '), document.createTextNode(r.conteudo));
      return li;
    }));
    $('foto-regioes-box').hidden = !(leitura.regioes || []).length;
    $('foto-conferir').hidden = false;
    $('foto-conferir').focus({ preventScroll: true });
  }

  function textoDaFoto() {
    var subs = Array.prototype.map.call(document.querySelectorAll('#foto-subtopicos input:checked'), function (cb) { return cb.value; });
    var partes = [];
    var enunciado = $('foto-enunciado').value.trim();
    var tentativa = $('foto-tentativa').value.trim();
    if (enunciado) partes.push('Enunciado (lido da foto e conferido pelo aluno):', enunciado);
    if (subs.length) partes.push('Subtópicos:', subs.map(function (s) { return '- ' + s; }).join('\n'));
    if (tentativa) partes.push('Tentativa do aluno no papel:', tentativa);
    return partes.join('\n').slice(0, 8000);
  }

  function limparFoto() {
    versaoFoto++;
    lendoFoto = false;
    fotoConfirmada = null;
    $('foto-conferir').hidden = true;
    $('foto-confirmada').hidden = true;
    $('foto-arquivo').value = '';
    setStatus($('foto-status'), '');
  }

  $('foto-arquivo').addEventListener('change', async function () {
    var arquivo = this.files && this.files[0];
    if (!arquivo) return;
    limparFoto();
    var versao = versaoFoto;
    lendoFoto = true;
    gerando++;
    setStatus($('foto-status'), 'Preparando a foto…', 'busy');
    try {
      var dataUrl = await comprimir(arquivo);
      if (versao !== versaoFoto) return;
      var criada = await postJSON('/api/foto', { imagem: dataUrl, disciplina: $('disciplina').value || null });
      var t = await acompanhar(criada.id, function (x) {
        if (versao === versaoFoto && x.status !== 'pronta' && x.status !== 'erro') setStatus($('foto-status'), x.mensagem || 'Lendo a foto…', 'busy');
      });
      if (versao !== versaoFoto) return;
      if (t.status !== 'pronta') throw new Error(t.mensagem || 'Não consegui ler a foto.');
      setStatus($('foto-status'), '');
      mostrarLeitura(t.leitura, dataUrl);
    } catch (e) {
      if (versao === versaoFoto) setStatus($('foto-status'), e.message, 'error');
    } finally {
      if (versao === versaoFoto) lendoFoto = false;
      gerando--;
    }
  });

  $('foto-ok').addEventListener('click', function () {
    var texto = textoDaFoto();
    if (!texto) { setStatus($('foto-status'), 'A leitura está vazia. Escreva o enunciado ou descarte a foto.', 'error'); return; }
    fotoConfirmada = texto;
    $('foto-conferir').hidden = true;
    var aviso = $('foto-confirmada');
    aviso.replaceChildren(document.createTextNode('📎 Foto conferida: vai junto com a sua próxima mensagem.'));
    var editar = el('button', null, 'Rever leitura');
    editar.type = 'button';
    editar.addEventListener('click', function () { $('foto-conferir').hidden = false; aviso.hidden = true; fotoConfirmada = null; });
    var remover = el('button', null, 'Remover');
    remover.type = 'button';
    remover.addEventListener('click', limparFoto);
    aviso.append(editar, remover);
    aviso.hidden = false;
    setStatus($('foto-status'), '');
    $('pergunta').focus();
  });
  $('foto-descartar').addEventListener('click', limparFoto);

  /* Disciplinas: a mesma IA atende todas; a escolha só decide qual acervo é consultado. */
  // "geral": dúvida de disciplina sem acervo (ex.: Controle). O servidor orienta com conhecimento geral.
  var disciplinas = { geral: { id: 'geral', sigla: 'Sem material cadastrado',
    aviso: 'Ainda não há material do professor desta disciplina no TutorON: a orientação usa conhecimento geral, sem citações.' } };
  function escolherDisciplina(id) {
    if (id === 'auto' || id === 'geral' || !disciplinas[id]) {
      $('disciplina').value = 'auto';
      $('disciplina-beta').hidden = true;
      $('disciplina-rotulo').textContent = 'Disciplina: automática';
      $('disciplina-chip').classList.remove('ativo');
      $('pergunta').placeholder = 'Pergunte ao TutorON… (diga o assunto e onde travou)';
      montarSugestoes();
      return;
    }
    var d = disciplinas[id];
    $('disciplina').value = id;
    // Aviso do cadastro (ex.: versão beta): some ao trocar para uma disciplina sem aviso.
    var beta = $('disciplina-beta');
    beta.textContent = d.aviso || '';
    beta.hidden = !d.aviso;
    $('disciplina-rotulo').textContent = d.sigla;
    $('disciplina-chip').classList.add('ativo');
    if (d.exemplos.length) $('pergunta').placeholder = 'Ex.: ' + d.exemplos[0];
    montarSugestoes();
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
      var pedida = new URL(location.href).searchParams.get('disciplina');
      var aviso = $('disciplina-aviso');
      if (disciplinas[pedida] && disciplinas[pedida].disponivel === false) {
        aviso.textContent = disciplinas[pedida].nome + ' ainda está em validação e não está disponível para uso normal.';
        aviso.hidden = false;
        pedida = null;
      }
      escolherDisciplina(disciplinas[pedida] ? pedida : 'auto');
    } catch (e) { /* servidor antigo ou fora do ar: segue com a identificação automática */ }
  })();
  $('disciplina').addEventListener('change', function () {
    escolherDisciplina($('disciplina').value);
    var url = new URL(location.href);
    url.searchParams.set('disciplina', $('disciplina').value);
    history.replaceState(null, '', url);
    fecharMenus();
  });

  // ------------------------------------------------------------------ conversas (só nesta aba)
  /* As conversas ficam só na memória da página: recarregar ou fechar a aba zera. */
  var conversas = [];   // { id, titulo, trocas: [{pergunta, texto, ...}], nodo }
  var conversaAtual = null;

  function novaConversa() {
    conversaAtual = null;
    $('conversa').replaceChildren();
    $('boas-vindas').hidden = false;
    desenharConversas();
    abrirLateral(false);
    $('pergunta').focus();
  }
  $('nova-conversa').addEventListener('click', function () { if (!enviando) novaConversa(); });

  function garantirConversa(pergunta) {
    if (conversaAtual) return conversaAtual;
    conversaAtual = { id: Date.now(), titulo: pergunta.length > 60 ? pergunta.slice(0, 57).trimEnd() + '…' : pergunta, trocas: [] };
    conversas.unshift(conversaAtual);
    $('boas-vindas').hidden = true;
    desenharConversas();
    return conversaAtual;
  }

  function abrirHistorico(abrir) {
    $('historico').hidden = !abrir;
    $('historico-botao').setAttribute('aria-expanded', String(abrir));
    $('historico-botao').textContent = abrir ? 'Conversas (' + conversas.length + ')' : 'Mostrar conversas (' + conversas.length + ')';
  }
  $('historico-botao').addEventListener('click', function () { abrirHistorico($('historico').hidden); });

  function desenharConversas() {
    var lista = $('historico');
    lista.replaceChildren.apply(lista, conversas.map(function (c) {
      var li = el('li');
      var b = el('button');
      b.type = 'button';
      b.append(el('span', null, c.titulo));
      if (c === conversaAtual) b.setAttribute('aria-current', 'true');
      b.append(el('small', null, c.trocas.length + (c.trocas.length === 1 ? ' pergunta' : ' perguntas')));
      b.addEventListener('click', function () { if (!enviando) abrirConversa(c); });
      li.append(b);
      return li;
    }));
    $('historico-vazio').hidden = conversas.length > 0;
    abrirHistorico(conversas.length > 0);
  }

  function abrirConversa(c) {
    conversaAtual = c;
    $('boas-vindas').hidden = true;
    $('conversa').replaceChildren.apply($('conversa'), c.trocas.map(function (t) { return t.nodo; }).filter(Boolean)
      .reduce(function (a, n) { return a.concat(n); }, []));
    desenharConversas();
    abrirLateral(false);
    rolarFim();
  }

  /* Resumo das últimas trocas da conversa, para a próxima pergunta não perder o fio. */
  function contextoDaConversa() {
    if (!conversaAtual || !conversaAtual.trocas.length) return '';
    var partes = conversaAtual.trocas.filter(function (t) { return t.pronta; }).slice(-2).map(function (t) {
      return 'Aluno: ' + t.pergunta.slice(0, 600) + '\nTutorON: ' + t.texto.slice(0, 1200);
    });
    return partes.length ? 'CONVERSA ANTERIOR (para manter o fio, não repita):\n' + partes.join('\n---\n') : '';
  }

  function msgAluno(pergunta, extras) {
    var m = el('div', 'msg msg--aluno');
    var b = el('div', 'bolha');
    if (extras) b.append(el('span', 'msg__anexo', extras));
    b.append(document.createTextNode(pergunta));
    m.append(b);
    return m;
  }
  function msgTutor() {
    var m = el('div', 'msg msg--tutor');
    var av = el('img', 'avatar');
    av.src = LOGO;
    av.alt = '';
    var corpo = el('div', 'corpo');
    var resposta = el('div', 'prose resposta');
    var estado = el('p', 'estado');
    var pontos = el('span', 'digitando');
    pontos.append(el('i'), el('i'), el('i'));
    var txt = el('span', null, 'Pensando…');
    estado.append(pontos, txt);
    corpo.append(resposta, estado);
    m.append(av, corpo);
    return { nodo: m, corpo: corpo, resposta: resposta, estado: estado, estadoTexto: txt, pontos: pontos };
  }
  function estadoErro(v, msg) {
    v.pontos.hidden = true;
    v.estadoTexto.textContent = msg;
    v.estado.dataset.tone = 'error';
  }

  function fontesDetalhe(fontes) {
    var d = el('details', 'fontes');
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

  function botaoIcone(icone, rotulo) {
    var b = el('button', 'icone-btn');
    b.type = 'button';
    b.title = rotulo;
    b.setAttribute('aria-label', rotulo);
    b.append(svg(ICONES[icone]));
    return b;
  }

  /* Copiar e avaliar a resposta (Ajudou / Não ajudou / Tem erro de conta). */
  function barraAcoes(id, registro, texto) {
    var box = el('div', 'barra-acoes');
    var status = el('span', 'barra-acoes__status');
    var copiar = botaoIcone('copiar', 'Copiar resposta');
    copiar.addEventListener('click', async function () {
      try { await navigator.clipboard.writeText(texto); status.textContent = 'Copiado.'; }
      catch (e) { status.textContent = 'Não consegui copiar.'; }
    });
    box.append(copiar);
    var votos = [];
    function voto(icone, rotulo, dados) {
      var b = botaoIcone(icone, rotulo);
      b.setAttribute('aria-pressed', 'false');
      b.addEventListener('click', async function () {
        votos.forEach(function (x) { x.disabled = true; });
        try {
          await postJSON('/api/feedback', Object.assign({ id: id }, dados));
          registro.voto = rotulo;
          b.setAttribute('aria-pressed', 'true');
          status.textContent = 'Obrigado pelo retorno.';
        } catch (e) {
          status.textContent = e.message;
          votos.forEach(function (x) { x.disabled = false; });
        }
      });
      votos.push(b);
      box.append(b);
    }
    voto('ok', 'Ajudou', { util: true });
    voto('nao', 'Não ajudou', { util: false });
    voto('erro', 'Tem erro de conta', { util: false, erro_matematico: true });
    box.append(status);
    return box;
  }

  /* Animação (Manim): pista visual da dúvida, gerada sob demanda. */
  function painelAnimacao(pergunta, resposta, disciplina, contexto, foto, opcoes) {
    opcoes = opcoes || {};
    var box = el('div', 'animacao');
    var status = el('p', 'status');
    box.iniciar = async function (retomarId) {
      gerando++;
      var id;
      setStatus(status, 'Preparando uma pista visual para esta dúvida…', 'busy');
      try {
        var criada = retomarId ? { id: retomarId } : await postJSON('/api/animar', {
          pergunta: pergunta, resposta: resposta || null, disciplina: disciplina || 'auto',
          contexto: contexto || null, foto: foto || null });
        id = criada.id;
        if (opcoes.pendente) guardarPendente({ tipo: 'animacao', id: id, pergunta: pergunta,
          contexto: contexto || '', disciplina: disciplina || 'auto', foto: foto || '' });
        var t = await acompanhar(id, function (x) {
          if (x.status !== 'pronta' && x.status !== 'erro') setStatus(status, x.mensagem || 'Gerando…', 'busy');
        });
        if (t.status !== 'pronta') throw new Error(t.mensagem || 'Não foi possível gerar a animação.');
        var video = document.createElement('video');
        video.src = t.video;
        video.controls = true;
        video.autoplay = true;
        video.muted = true;
        video.playsInline = true;
        if (t.poster) video.poster = t.poster;
        video.setAttribute('aria-label', 'Animação: ' + (t.titulo || 'pista visual'));
        box.prepend(video);
        var materia = disciplinas[t.disciplina];
        setStatus(status, (materia ? materia.sigla + ' · ' : '') + (t.pergunta_final ? 'Sua vez: ' + t.pergunta_final : ''));
        if (opcoes.aoConcluir) opcoes.aoConcluir(t);
        return true;
      } catch (e) {
        setStatus(status, e.message, 'error');
        return false;
      } finally {
        gerando--;
        if (opcoes.pendente) { var p = lerPendente(); if (p && p.id === id) limparPendente(); }
      }
    };
    box.append(status);
    return box;
  }

  var enviando = false;
  function travar(sim) {
    enviando = sim;
    $('enviar').disabled = sim;
  }

  /* Depois da resposta: entender visualmente, "ainda não consegui" (outra forma) e "consegui". */
  function pilulasDepois(registro, pergunta, contexto, disciplina, foto, historicoNovo, final, corpo) {
    var box = el('div', 'pilulas');
    function pilula(icone, texto, forte) {
      var b = el('button', 'pilula-acao' + (forte ? ' pilula-acao--forte' : ''));
      b.type = 'button';
      b.append(svg(ICONES[icone]), document.createTextNode(texto));
      box.append(b);
      return b;
    }
    var visual = pilula('olho', 'Quer entender visualmente?');
    visual.disabled = animacaoDisponivel === false;
    if (visual.disabled) visual.title = 'As animações estão indisponíveis neste servidor.';
    visual.addEventListener('click', function () {
      visual.disabled = true;
      var painel = painelAnimacao(pergunta, final.texto, disciplina, contexto, foto);
      box.after(painel);
      painel.iniciar().then(function (ok) { if (!ok) visual.disabled = false; });
    });
    var outra = pilula('outra', 'Ainda não consegui');
    var consegui = pilula('feito', 'Consegui!');
    outra.addEventListener('click', function () {
      if (enviando) return;
      var ciclo = el('div', 'ciclo');
      ciclo.append(el('p', 'ciclo__titulo', 'Tentou no papel? Conte onde travou (opcional) e eu explico de outro jeito.'));
      var campo = el('textarea', 'campo');
      campo.rows = 2;
      campo.maxLength = 1500;
      campo.placeholder = 'Ex.: não sei achar o log de 4 na base 2.';
      campo.setAttribute('aria-label', 'O que você tentou ou onde travou (opcional)');
      var ir = el('button', 'botao', 'Explica de outro jeito');
      ir.type = 'button';
      ir.addEventListener('click', async function () {
        if (enviando) return;
        ciclo.remove();
        box.remove();
        travar(true); gerando++;
        try {
          await perguntar(pergunta, contexto, null, disciplina, 'auto', foto, { historico: historicoNovo, travou: campo.value.trim() });
        } finally { travar(false); gerando--; }
      });
      var acoes = el('div', 'acoes');
      acoes.append(ir);
      ciclo.append(campo, acoes);
      box.after(ciclo);
      campo.focus();
    });
    consegui.addEventListener('click', function () {
      box.replaceWith(el('p', 'ciclo__ok', 'Boa! Você chegou lá pelo próprio raciocínio. 🎉 Mande a próxima dúvida quando quiser.'));
    });
    return box;
  }

  async function perguntar(pergunta, contexto, retomarId, disciplina, ajuda, foto, ciclo) {
    ciclo = ciclo || { historico: [], travou: '' };
    var conversa = garantirConversa(pergunta);
    var registro = { pergunta: pergunta, texto: '', fontes: [], voto: null, pronta: false, nodo: [] };
    conversa.trocas.push(registro);
    var anexos = [foto ? '📎 foto conferida' : '', contexto ? '</> código/enunciado' : '',
      ciclo.historico.length ? '↻ outra forma de explicar (tentativa ' + (ciclo.historico.length + 1) + ')' : ''].filter(Boolean).join(' · ');
    var textoAluno = ciclo.historico.length ? (ciclo.travou || 'Ainda não consegui. Explica de outro jeito?') : pergunta;
    var aluno = msgAluno(textoAluno, anexos);
    var v = msgTutor();
    registro.nodo = [aluno, v.nodo];
    $('conversa').append(aluno, v.nodo);
    desenharConversas();
    rolarFim();

    var contextoEnvio = [contexto, ciclo.historico.length ? '' : contextoDaConversa()].filter(Boolean).join('\n\n').slice(0, 6000);
    var desenhado = '';
    var final;
    var inicio = Date.now();
    for (var envio = 0; envio < 3; envio++) {
      var tarefa;
      if (retomarId && envio === 0) {
        tarefa = { id: retomarId };
      } else {
        try {
          tarefa = await postJSON('/api/perguntar', { pergunta: pergunta, contexto: contextoEnvio || null,
            disciplina: disciplina || null, ajuda: ajuda || 'auto', foto: foto || null,
            historico: ciclo.historico, travou: ciclo.travou || null,
            curso: perfil ? perfil.curso : null, periodo: perfil ? perfil.periodo : null });
        } catch (e) {
          estadoErro(v, e.message);
          return false;
        }
      }
      guardarPendente({ tipo: 'tutor', id: tarefa.id, pergunta: pergunta, contexto: contexto || '', disciplina: disciplina || '',
        ajuda: ajuda || 'auto', foto: foto || '', historico: ciclo.historico, travou: ciclo.travou || '' });
      final = await acompanhar(tarefa.id, function (t) {
        if (t.texto && t.texto !== desenhado) {
          desenhado = t.texto;
          R.render(v.resposta, t.texto);
          v.pontos.hidden = true;
          rolarFim();
        }
        if (t.status !== 'pronta' && t.status !== 'erro') v.estadoTexto.textContent = t.mensagem || 'Escrevendo…';
      });
      if (final.status !== 'perdida') break;
      v.estadoTexto.textContent = 'Reenviando a pergunta…';
      await esperar(3000);
    }

    limparPendente();
    if (final.status === 'pronta') {
      R.render(v.resposta, final.texto);
      v.estado.remove();
      var materia = disciplinas[final.disciplina];
      if (materia && materia.aviso) v.corpo.append(el('p', 'aviso-beta', materia.aviso));
      var meta = el('p', 'meta', (materia ? materia.sigla + ' · ' : '') + 'respondido em ' +
        Math.max(1, Math.round((Date.now() - inicio) / 1000)) + ' s' + (final.rotulo ? ' · ' + final.rotulo : ''));
      // Mantém só as últimas ajudas (o servidor aceita até 8) para o prompt não crescer sem limite.
      var historicoNovo = ciclo.historico.concat([{ ajuda: final.ajuda || ajuda || 'auto', texto: final.texto.slice(0, 6000) }]).slice(-6);
      var disciplinaDaPergunta = final.disciplina || disciplina;
      v.corpo.append(barraAcoes(final.id_resposta, registro, final.texto));
      if (final.fontes && final.fontes.length) v.corpo.append(fontesDetalhe(final.fontes));
      v.corpo.append(meta, pilulasDepois(registro, pergunta, contexto, disciplinaDaPergunta, foto, historicoNovo, final, v.corpo));
      registro.texto = final.texto;
      registro.fontes = final.fontes || [];
      registro.pronta = true;
      desenharConversas();
      return true;
    }
    estadoErro(v, final.mensagem || 'Não foi possível gerar a resposta. Tente de novo.');
    return false;
  }

  async function perguntarVisual(pergunta, contexto, disciplina, foto, retomarId) {
    var conversa = garantirConversa(pergunta);
    var registro = { pergunta: pergunta, texto: '', fontes: [], voto: null, pronta: false, nodo: [] };
    conversa.trocas.push(registro);
    var aluno = msgAluno(pergunta, '🎬 só animação');
    var v = msgTutor();
    v.estado.remove();
    var painel = painelAnimacao(pergunta, null, disciplina, contexto, foto, { pendente: true, aoConcluir: function (t) {
      registro.texto = 'Sua vez: ' + (t.pergunta_final || 'Tente o próximo passo no papel.');
      registro.pronta = true;
    } });
    v.corpo.append(painel);
    registro.nodo = [aluno, v.nodo];
    $('conversa').append(aluno, v.nodo);
    desenharConversas();
    rolarFim();
    return await painel.iniciar(retomarId);
  }

  $('form-tutor').addEventListener('submit', async function (e) {
    e.preventDefault();
    if (enviando) return;
    if (lendoFoto) { setStatus($('status-tutor'), 'Aguarde a leitura da foto terminar e confira o texto antes de enviar.', 'error'); return; }
    var pergunta = $('pergunta').value.trim();
    var foto = fotoConfirmada;
    var versaoEnviada = versaoFoto;
    if (pergunta.length < 3 && foto) pergunta = 'Me ajude com o exercício da foto, sem me dar a resposta.';
    if (!foto && !$('foto-conferir').hidden) {
      setStatus($('status-tutor'), 'Confira a leitura da foto (botão “Está certo”) ou descarte-a antes de enviar.', 'error');
      $('foto-conferir').focus();
      return;
    }
    if (pergunta.length < 3) { setStatus($('status-tutor'), 'Escreva sua dúvida antes de enviar.', 'error'); $('pergunta').focus(); return; }
    travar(true);
    gerando++;
    setStatus($('status-tutor'), '');
    var contexto = $('contexto').value.trim();
    var disciplina = $('disciplina').value || 'auto';
    $('pergunta').value = '';
    $('contexto').value = '';
    $('contexto-box').hidden = true;
    $('codigo-botao').setAttribute('aria-pressed', 'false');
    ajustarAltura();
    var ajuda = ajudaEscolhida();
    try {
      var ok = ajuda === 'animacao' ? await perguntarVisual(pergunta, contexto, disciplina, foto) :
        await perguntar(pergunta, contexto, null, disciplina, ajuda, foto);
      if (ok && foto && versaoEnviada === versaoFoto) limparFoto();
      if (!ok && !$('pergunta').value) { $('pergunta').value = pergunta; $('contexto').value = contexto; ajustarAltura(); }
    } finally {
      travar(false);
      gerando--;
    }
  });

  async function retomarTutor(p) {
    travar(true); gerando++;
    try {
      await perguntar(p.pergunta, p.contexto, p.id, p.disciplina, p.ajuda, p.foto, { historico: p.historico || [], travou: p.travou || '' });
    } finally { travar(false); gerando--; }
  }
  async function retomarVisual(p) {
    travar(true);
    try { await perguntarVisual(p.pergunta, p.contexto, p.disciplina, p.foto, p.id); }
    finally { travar(false); }
  }

  // ================================================================== MODO VALIDAÇÃO
  (function sugestoesValidacao() {
    var box = $('sugestoes-validacao');
    SUGESTOES.slice(0, 3).forEach(function (s) {
      var b = el('button', 'sugestao', s);
      b.type = 'button';
      b.addEventListener('click', function () { $('v-pergunta').value = s; $('v-pergunta').focus(); });
      box.append(b);
    });
  })();

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
      var hint = el('span', 'scale__hint dica', c[2]);
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
    if (pergunta.length < 3) { setStatus($('v-status'), 'Escreva sua dúvida antes de gerar as respostas.', 'error'); $('v-pergunta').focus(); return; }
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
      if (dados.status !== 'pronta') { limparPendente(); throw new Error(dados.mensagem || 'Não foi possível gerar as respostas. Tente de novo.'); }
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
    if (!form.querySelector('input[name="preferida"]:checked')) return { nome: 'preferida', msg: 'Escolha a resposta que você prefere, ou empate.' };
    return null;
  }

  $('v-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    if (!sessao) return;
    var form = e.currentTarget;
    var falta = faltando(form);
    if (falta) { setStatus($('v-status-envio'), falta.msg, 'error'); form.querySelector('input[name="' + falta.nome + '"]').focus(); return; }
    var fd = new FormData(form);
    var lado = function (L) {
      return { clareza: Number(fd.get('clareza_' + L)), confianca: Number(fd.get('confianca_' + L)),
        utilidade: Number(fd.get('utilidade_' + L)), erro_matematico: fd.get('erro_' + L) === 'on' };
    };
    var dados = { sessao: sessao, preferida: fd.get('preferida'), A: lado('A'), B: lado('B'),
      comentario: $('v-comentario').value, curso: $('v-curso').value, periodo: $('v-periodo').value };
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
  $('v-outra').addEventListener('click', function () {
    $('v-feito').hidden = true;
    $('v-pergunta').value = '';
    $('v-passo1').scrollIntoView({ block: 'start' });
    $('v-pergunta').focus({ preventScroll: true });
  });
  (function preencherPerfilValidacao() {
    // Curso e período da validação vêm do perfil escolhido (o aluno ainda pode editar).
    if (!perfil) return;
    var nomes = { ecom: 'Engenharia de Computação', cc: 'Ciência da Computação' };
    $('v-curso').value = nomes[perfil.curso] || '';
    $('v-periodo').value = perfil.periodo + 'º';
  })();

  // ================================================================== RETOMADA
  // Página recarregada no meio de uma geração (ou antes de votar): retoma de onde parou.
  var pendente = lerPendente();
  if (!pendente) {
    try {
      var tentativaVisual = JSON.parse(sessionStorage.getItem('tutoron-tentativa-visual') || 'null');
      if (tentativaVisual && typeof tentativaVisual.pergunta === 'string' && typeof tentativaVisual.contexto === 'string') {
        mostrarModo('tutor');
        $('pergunta').value = tentativaVisual.pergunta.slice(0, 4000);
        $('contexto').value = tentativaVisual.contexto.slice(0, 6000);
        $('contexto-box').hidden = !$('contexto').value;
        $('codigo-botao').setAttribute('aria-pressed', String(!!$('contexto').value));
        sessionStorage.removeItem('tutoron-tentativa-visual');
        ajustarAltura();
        $('pergunta').focus({ preventScroll: true });
      }
    } catch (e) { /* Sem storage, a pergunta continua podendo ser escrita manualmente. */ }
  }
  if (pendente && pendente.id) {
    if (pendente.tipo === 'validacao') {
      mostrarModo('validacao');
      $('v-pergunta').value = pendente.pergunta || '';
      gerarPar(pendente.id);
    } else if (pendente.tipo === 'tutor') {
      mostrarModo('tutor');
      retomarTutor(pendente);
    } else if (pendente.tipo === 'animacao') {
      mostrarModo('tutor');
      retomarVisual(pendente);
    }
  }
  if (!pendente) $('pergunta').focus({ preventScroll: true });
})();
