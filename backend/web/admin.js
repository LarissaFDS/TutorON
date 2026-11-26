(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };
  var fmt = function (n) { return n == null ? '—' : Number(n).toLocaleString('pt-BR'); };

  function el(tag, cls, texto) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (texto !== undefined) n.textContent = texto;
    return n;
  }

  async function postar(url, corpo) {
    var r = await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(corpo || {}) });
    if (!r.ok) throw new Error((await r.json()).erro || 'Falhou.');
  }

  function linha(u) {
    var tr = el('tr');
    var conta = el('td');
    conta.append(document.createTextNode(u.nome || u.email || (u.conta ? 'Conta' : 'Convidado')));
    conta.append(el('small', null, u.email || u.quem));
    var hoje = el('td', 'n', fmt(u.usados_hoje));
    if (u.limite) {
      var m = el('span', 'medidor'), b = el('span');
      b.style.width = Math.min(100, Math.round(100 * (u.usados_hoje || 0) / u.limite)) + '%';
      m.append(b); hoje.append(m);
    }
    var lim = el('td');
    var input = el('input', 'campo');
    input.type = 'number'; input.min = '0'; input.step = '1000'; input.placeholder = fmt(u.limite);
    input.value = u.limite_proprio == null ? '' : u.limite_proprio;
    input.disabled = !u.conta;
    input.title = u.conta ? 'Limite próprio desta conta' : 'Só contas logadas têm limite próprio';
    input.setAttribute('aria-label', 'Limite diário de ' + (u.email || u.quem));
    var salvar = el('button', 'botao botao--leve', 'Salvar');
    salvar.type = 'button'; salvar.disabled = !u.conta;
    salvar.addEventListener('click', async function () {
      try {
        await postar('/api/admin/usuarios/' + encodeURIComponent(u.quem) + '/limite',
          { limite: input.value === '' ? null : Number(input.value) });
        carregar('Limite salvo.');
      } catch (e) { $('admin-status').textContent = e.message; }
    });
    lim.append(input, document.createTextNode(' '), salvar);
    var zerar = el('button', 'botao botao--leve', 'Zerar hoje');
    zerar.type = 'button';
    zerar.addEventListener('click', async function () {
      try { await postar('/api/admin/usuarios/' + encodeURIComponent(u.quem) + '/zerar'); carregar('Limite de hoje devolvido.'); }
      catch (e) { $('admin-status').textContent = e.message; }
    });
    var acao = el('td'); acao.append(zerar);
    tr.append(conta, hoje, lim, el('td', 'n', fmt(u.tokens_total)), el('td', 'n', fmt(u.perguntas)),
      el('td', null, u.ultimo ? new Date(u.ultimo).toLocaleString('pt-BR') : '—'), acao);
    return tr;
  }

  async function carregar(msg) {
    var r = await fetch('/api/admin/usuarios', { cache: 'no-store' });
    var d = await r.json();
    if (!r.ok) {
      $('admin-status').textContent = r.status === 403 ? 'Só administradores. Entre com uma conta listada em TUTORON_ADMINS.' : (d.erro || 'Erro.');
      return;
    }
    var contas = d.usuarios.filter(function (u) { return u.conta; });
    var resumo = $('admin-resumo');
    resumo.replaceChildren();
    [[contas.length, 'contas'], [d.usuarios.length - contas.length, 'convidados'],
     [d.usuarios.reduce(function (s, u) { return s + (u.tokens_total || 0); }, 0), 'tokens no total'],
     [d.limite_padrao, 'limite padrão/dia']].forEach(function (x) {
      var c = el('div'); c.append(el('strong', null, fmt(x[0])), el('span', null, x[1])); resumo.append(c);
    });
    $('admin-linhas').replaceChildren.apply($('admin-linhas'), d.usuarios.map(linha));
    $('admin-tabela-box').hidden = false;
    $('admin-status').textContent = msg || (d.banco ? '' : 'Banco não configurado: mostrando só o uso deste PC.');
  }
  carregar();

  /* ---------------------------------------------------------------- coleta (feedbacks, erros, perguntas, conversas) */
  var COLETA = null, ABA = 'geral', MOSTRAR = { feedbacks: 40, erros: 40, perguntas: 40, conversas: 30 };
  var NOMES_CAT = { erro: 'Erro de cálculo', negativo: 'Não ajudou', positivo: 'Ajudou', escrito: 'Feedback escrito',
    disciplina: 'Disciplina errada', leitura: 'Leitura da foto errada' };
  var data = function (d) { return d ? new Date(d).toLocaleString('pt-BR', { dateStyle: 'short', timeStyle: 'short' }) : '—'; };

  function selo(texto, tipo) { return el('span', 'selo' + (tipo ? ' selo--' + tipo : ''), texto); }
  function quem(x) {
    var h = [];
    h.push(el('strong', null, x.nome || x.email || (x.usuario ? (x.usuario.indexOf('u:') === 0 ? 'Conta' : 'Convidado') : 'Sem conta')));
    if (x.email && x.nome) h.push(el('span', null, x.email));
    if (x.ic === 'email') h.push(selo('IC · e-mail institucional', 'ic'));
    else if (x.ic === 'declarado') h.push(selo('IC · declarado', 'ic'));
    return h;
  }
  function texto(rotulo, valor) {
    if (!valor) return null;
    var box = el('div'); box.append(el('span', 'rotulo', rotulo), el('p', null, valor)); return box;
  }
  function respostaBox(r, titulo) {
    if (!r) return null;
    var det = el('details'); det.append(el('summary', null, titulo || 'Ver a resposta do tutor'));
    var div = el('div', 'resposta');
    if (window.TutorONRender) window.TutorONRender.render(div, r); else div.textContent = r;
    det.append(div); return det;
  }

  function filtrar(lista) {
    var busca = $('f-busca').value.trim().toLowerCase(), disc = $('f-disciplina').value, ic = $('f-ic').value,
        testes = $('f-testes').checked;
    return lista.filter(function (x) {
      if (!testes && x.teste) return false;
      if (disc && x.disciplina !== disc) return false;
      if (ic === 'ic' && !x.ic) return false;
      if (ic === 'email' && x.ic !== 'email') return false;
      if (ic === 'fora' && x.ic) return false;
      if (busca && JSON.stringify(x).toLowerCase().indexOf(busca) < 0) return false;
      return true;
    });
  }
  // IC primeiro (peso maior), depois os mais recentes.
  function ordenar(lista) {
    return lista.slice().sort(function (a, b) {
      var pa = a.ic === 'email' ? 2 : a.ic ? 1 : 0, pb = b.ic === 'email' ? 2 : b.ic ? 1 : 0;
      return pb - pa || String(b.data || '').localeCompare(String(a.data || ''));
    });
  }

  function itemFeedback(f) {
    var box = el('article', 'admin__item');
    var h = el('header');
    h.append(selo(NOMES_CAT[f.categoria] || f.categoria, f.categoria));
    if (f.nota) h.append(selo('Nota ' + f.nota + '/5'));
    if (f.disciplina) h.append(selo(f.disciplina));
    if (f.rodadas) h.append(selo(f.rodadas + 'x "ainda não consegui"'));
    if (f.teste) h.append(selo('teste', 'teste'));
    h.append.apply(h, quem(f)); h.append(el('span', null, data(f.data)));
    box.append(h);
    [texto('Pergunta do aluno', f.pergunta), texto('Em que o tutor ajudou', f.ajudou_em),
     texto('Sugestão para melhorar', f.sugestao), texto('Comentário', f.comentario),
     respostaBox(f.resposta)].forEach(function (n) { if (n) box.append(n); });
    return box;
  }
  function itemPergunta(p) {
    var box = el('article', 'admin__item');
    var h = el('header');
    if (p.disciplina) h.append(selo(p.disciplina));
    if (p.ajuda && p.ajuda !== 'auto') h.append(selo(p.ajuda));
    if (p.foto) h.append(selo('com foto/anexo'));
    if (p.rodada) h.append(selo('rodada ' + p.rodada));
    (p.votos || []).forEach(function (v) { h.append(selo(NOMES_CAT[v] || v, v)); });
    if (p.erro) h.append(selo('sem resposta: ' + p.erro, 'erro'));
    if (p.teste) h.append(selo('teste', 'teste'));
    h.append.apply(h, quem(p));
    h.append(el('span', null, data(p.data) + (p.modelo ? ' · ' + p.modelo : '') + (p.segundos ? ' · ' + p.segundos + ' s' : '')));
    box.append(h);
    [texto('Pergunta', p.pergunta), texto('Onde travou', p.travou), texto('Contexto enviado', p.contexto),
     respostaBox(p.resposta)].forEach(function (n) { if (n) box.append(n); });
    return box;
  }
  function itemConversa(c) {
    var box = el('article', 'admin__item');
    var h = el('header');
    h.append(el('strong', null, c.titulo || 'Conversa'), selo(c.trocas.length + ' trocas'));
    h.append.apply(h, quem(c)); h.append(el('span', null, data(c.data)));
    box.append(h);
    var det = el('details'); det.append(el('summary', null, 'Abrir a conversa'));
    c.trocas.forEach(function (t, i) {
      det.append(texto('Aluno (' + (i + 1) + ')', t.p));
      var r = el('div', 'resposta');
      if (window.TutorONRender) window.TutorONRender.render(r, t.r || ''); else r.textContent = t.r || '';
      det.append(r);
    });
    box.append(det);
    return box;
  }

  function lista(alvo, itens, chave, montar, vazio) {
    alvo.replaceChildren();
    if (!itens.length) { alvo.append(el('p', 'dica', vazio)); return; }
    var box = el('div', 'admin__lista');
    itens.slice(0, MOSTRAR[chave]).forEach(function (x) { box.append(montar(x)); });
    alvo.append(box);
    if (itens.length > MOSTRAR[chave]) {
      var mais = el('button', 'botao botao--leve admin__mais', 'Mostrar mais (' + (itens.length - MOSTRAR[chave]) + ')');
      mais.type = 'button';
      mais.addEventListener('click', function () { MOSTRAR[chave] += 60; desenhar(); });
      alvo.append(mais);
    }
  }

  function contagem(itens, campo) {
    var c = {};
    itens.forEach(function (x) { var k = x[campo] || '(sem)'; c[k] = (c[k] || 0) + 1; });
    return Object.keys(c).map(function (k) { return [k, c[k]]; }).sort(function (a, b) { return b[1] - a[1]; });
  }
  function barras(titulo, pares, nomes) {
    var box = el('div', 'admin__barras');
    box.append(el('h3', null, titulo));
    var max = pares.length ? pares[0][1] : 1;
    pares.slice(0, 12).forEach(function (p) {
      var linha = el('div', 'admin__barra'), b = el('span'), i = el('i');
      i.style.width = Math.max(1, Math.round(100 * p[1] / max)) + '%'; b.append(i);
      linha.append(el('span', null, (nomes && nomes[p[0]]) || p[0]), b, el('em', null, fmt(p[1])));
      box.append(linha);
    });
    if (!pares.length) box.append(el('p', 'dica', 'Nada ainda.'));
    return box;
  }

  function desenhar() {
    if (!COLETA) return;
    var fb = ordenar(filtrar(COLETA.feedbacks)), pg = ordenar(filtrar(COLETA.perguntas)), cv = ordenar(filtrar(COLETA.conversas));
    var erros = fb.filter(function (f) { return f.categoria === 'erro' || f.categoria === 'leitura' || f.categoria === 'disciplina'; });
    var opinioes = fb.filter(function (f) { return erros.indexOf(f) < 0; });
    var n = { feedbacks: opinioes.length, erros: erros.length, perguntas: pg.length, conversas: cv.length };
    document.querySelectorAll('[data-n]').forEach(function (b) { b.textContent = n[b.dataset.n]; });
    $('admin-filtros').hidden = ABA === 'contas';

    if (ABA === 'geral') {
      var g = $('p-geral'); g.replaceChildren();
      var pessoas = {};
      pg.concat(fb).forEach(function (x) { if (x.usuario) pessoas[x.usuario] = x.ic || pessoas[x.usuario] || ''; });
      var ids = Object.keys(pessoas);
      var notas = fb.filter(function (f) { return f.nota; });
      var media = notas.length ? (notas.reduce(function (s, f) { return s + f.nota; }, 0) / notas.length).toFixed(1).replace('.', ',') : '—';
      var util = fb.filter(function (f) { return f.util === true; }).length, inutil = fb.filter(function (f) { return f.util === false; }).length;
      var cards = el('div', 'admin__cartoes');
      [[pg.length, 'perguntas respondidas'], [ids.length, 'pessoas diferentes'],
       [ids.filter(function (k) { return pessoas[k]; }).length, 'pessoas do IC'],
       [fb.length, 'feedbacks'], [util + inutil ? Math.round(100 * util / (util + inutil)) + '%' : '—', 'disseram "ajudou"'],
       [media, 'nota média (1 a 5)'], [erros.length, 'erros reportados'], [cv.length, 'conversas salvas']].forEach(function (x) {
        var c = el('div'); c.append(el('strong', null, typeof x[0] === 'number' ? fmt(x[0]) : x[0]), el('span', null, x[1])); cards.append(c);
      });
      g.append(cards);
      var dias = {};
      pg.forEach(function (p) { var d = (p.data || '').slice(0, 10); if (d) dias[d] = (dias[d] || 0) + 1; });
      var porDia = Object.keys(dias).sort().reverse().slice(0, 14).map(function (d) { return [d.split('-').reverse().join('/'), dias[d]]; });
      g.append(barras('Assuntos mais perguntados (disciplina)', contagem(pg, 'disciplina')),
        barras('Tipo de ajuda pedida', contagem(pg, 'ajuda')),
        barras('Feedbacks por tipo', contagem(fb, 'categoria'), NOMES_CAT),
        barras('Perguntas por dia (últimos 14 dias com uso)', porDia));
      g.append(el('p', 'dica', 'Fonte: ' + (COLETA.fonte === 'banco' ? 'banco de dados (Supabase)' : 'arquivos deste PC (dados/)') +
        '. Pessoas do IC: e-mail ' + COLETA.dominios_ic.map(function (d) { return '@' + d; }).join(', ') +
        ' ou quem marcou "sou do IC" no feedback. Linhas de teste ficam escondidas.'));
    }
    if (ABA === 'feedbacks') lista($('p-feedbacks'), opinioes, 'feedbacks', itemFeedback, 'Nenhum feedback com esses filtros.');
    if (ABA === 'erros') lista($('p-erros'), erros, 'erros', itemFeedback, 'Nenhum erro reportado com esses filtros.');
    if (ABA === 'perguntas') lista($('p-perguntas'), pg, 'perguntas', itemPergunta, 'Nenhuma pergunta com esses filtros.');
    if (ABA === 'conversas') lista($('p-conversas'), cv, 'conversas', itemConversa,
      COLETA.fonte === 'banco' ? 'Nenhuma conversa salva com esses filtros.' : 'Conversas salvas só existem com o banco (Supabase) ligado.');
  }

  function csv(linhas) {
    if (!linhas.length) return '';
    var cols = Object.keys(linhas[0]).filter(function (k) { return k !== 'trocas'; });
    var esc = function (v) { v = v == null ? '' : typeof v === 'object' ? JSON.stringify(v) : String(v); return '"' + v.replace(/"/g, '""') + '"'; };
    return '\ufeff' + [cols.join(';')].concat(linhas.map(function (l) { return cols.map(function (c) { return esc(l[c]); }).join(';'); })).join('\n');
  }
  $('exportar').addEventListener('click', function () {
    if (!COLETA) return;
    var base = ABA === 'perguntas' || ABA === 'geral' ? COLETA.perguntas : ABA === 'conversas' ? COLETA.conversas : COLETA.feedbacks;
    var linhas = ordenar(filtrar(base));
    if (ABA === 'conversas') linhas = linhas.map(function (c) { return Object.assign({}, c, { conversa: c.trocas.map(function (t) { return 'ALUNO: ' + t.p + '\nTUTOR: ' + t.r; }).join('\n\n') }); });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([csv(linhas)], { type: 'text/csv;charset=utf-8' }));
    a.download = 'tutoron-' + (ABA === 'geral' ? 'perguntas' : ABA) + '-' + new Date().toISOString().slice(0, 10) + '.csv';
    a.click();
  });

  document.querySelectorAll('#admin-abas [data-aba]').forEach(function (b) {
    b.addEventListener('click', function () {
      ABA = b.dataset.aba;
      document.querySelectorAll('#admin-abas [data-aba]').forEach(function (x) { x.setAttribute('aria-selected', String(x === b)); });
      document.querySelectorAll('[data-painel]').forEach(function (p) { p.hidden = p.dataset.painel !== ABA; });
      desenhar();
    });
  });
  ['f-busca', 'f-disciplina', 'f-ic', 'f-testes'].forEach(function (id) { $(id).addEventListener('input', desenhar); });

  (async function carregarColeta() {
    try {
      var r = await fetch('/api/admin/coleta', { cache: 'no-store' });
      if (!r.ok) return;
      COLETA = await r.json();
      var discs = {};
      COLETA.perguntas.concat(COLETA.feedbacks).forEach(function (x) { if (x.disciplina) discs[x.disciplina] = 1; });
      Object.keys(discs).sort().forEach(function (d) { var o = el('option', null, d); o.value = d; $('f-disciplina').append(o); });
      desenhar();
    } catch (e) { $('admin-status').textContent = 'Não consegui carregar a coleta: ' + e.message; }
  })();
})();
