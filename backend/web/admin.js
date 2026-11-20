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
})();
