/* Conta do aluno (Supabase Auth): mantém o token de sessão no cookie `tutoron_sessao` para o
 * servidor saber quem é (limite por conta) e mostra "Entrar"/a conta na barra lateral.
 * Sem Supabase configurado no servidor, não faz nada e o site segue como convidado. */
(function () {
  'use strict';
  var SDK = 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.min.js';
  var $ = function (id) { return document.getElementById(id); };
  var pronto;

  function carregarScript(src) {
    return new Promise(function (ok, falha) {
      var s = document.createElement('script');
      s.src = src; s.onload = ok; s.onerror = function () { falha(new Error('Não consegui carregar o login.')); };
      document.head.append(s);
    });
  }

  function gravarCookie(sessao) {
    var seguro = location.protocol === 'https:' ? '; secure' : '';
    if (sessao && sessao.access_token) {
      var segundos = Math.max(60, (sessao.expires_at || 0) - Math.floor(Date.now() / 1000));
      document.cookie = 'tutoron_sessao=' + sessao.access_token + '; path=/; max-age=' + segundos + '; samesite=lax' + seguro;
    } else {
      document.cookie = 'tutoron_sessao=; path=/; max-age=0; samesite=lax' + seguro;
    }
  }

  async function iniciar() {
    var cfg = await (await fetch('/api/config', { cache: 'no-store' })).json();
    if (!cfg.contas) return { cfg: cfg, cliente: null };
    await carregarScript(SDK);
    var cliente = window.supabase.createClient(cfg.supabase_url, cfg.supabase_anon_key, {
      auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: true, flowType: 'pkce' }
    });
    var atual = (await cliente.auth.getSession()).data.session;
    gravarCookie(atual);
    cliente.auth.onAuthStateChange(function (_evento, sessao) {
      gravarCookie(sessao);
      desenharChip();
    });
    return { cfg: cfg, cliente: cliente };
  }

  /* Pergunta antes de sair da conta. Usa a janela do site (.janela, em chat.css); sem suporte a
   * <dialog>, cai no confirm() do navegador. Resolve true só se a pessoa confirmar. */
  function confirmarSaida() {
    var janela = $('janela-sair');
    if (!janela) {
      janela = document.createElement('dialog');
      janela.className = 'janela';
      janela.id = 'janela-sair';
      janela.setAttribute('aria-labelledby', 'sair-titulo');
      janela.innerHTML =
        '<form method="dialog" class="janela__corpo">' +
        '<h2 id="sair-titulo">Sair da conta?</h2>' +
        '<p class="dica">Você vai voltar a usar o TutorON como convidado, com o limite de perguntas de convidado. ' +
        'Para continuar com sua conta depois, é só entrar de novo.</p>' +
        '<div class="acoes acoes--fim">' +
        '<button class="botao botao--leve" value="cancelar" type="submit">Cancelar</button>' +
        '<button class="botao" value="sair" type="submit" id="sair-confirmar">Sair</button>' +
        '</div></form>';
      document.body.append(janela);
    }
    if (typeof janela.showModal !== 'function') {
      return Promise.resolve(window.confirm('Sair da conta?'));
    }
    return new Promise(function (ok) {
      janela.returnValue = '';
      janela.addEventListener('close', function () { ok(janela.returnValue === 'sair'); }, { once: true });
      janela.showModal();
      $('sair-confirmar').focus();
    });
  }

  async function desenharChip() {
    var chip = $('conta-chip');
    if (!chip) return;
    var eu;
    try { eu = await (await fetch('/api/eu', { cache: 'no-store' })).json(); } catch (e) { return; }
    var cfg = (await pronto).cfg;
    if (!cfg.contas) { chip.hidden = true; return; }
    chip.hidden = false;
    var nome = chip.querySelector('[data-nome]'), sub = chip.querySelector('[data-sub]');
    if (eu.logado) {
      nome.textContent = eu.conta.nome || eu.conta.email;
      sub.textContent = eu.admin ? 'Administrador · sair' : 'Sair da conta';
      chip.href = '#sair';
      chip.onclick = async function (e) {
        e.preventDefault();
        if (!(await confirmarSaida())) return;
        await window.TutorConta.sair();
        location.reload();
      };
      if ($('admin-link')) $('admin-link').hidden = !eu.admin;
    } else {
      nome.textContent = 'Entrar ou criar conta';
      var aviso = $('aviso-conta');
      if (aviso && eu.cota && eu.cota.convidado) {
        var vezes = Math.max(2, Math.round((eu.cota.limite_conta || 0) / (eu.cota.limite || 1)));
        aviso.replaceChildren();
        var link = document.createElement('a');
        link.href = '/entrar?criar=1&voltar=' + encodeURIComponent(location.pathname + location.search);
        link.textContent = 'Criar conta grátis';
        aviso.append(document.createTextNode(eu.cota.restantes > 0
          ? 'Você está como convidado, com poucas perguntas por dia. Com uma conta (só e-mail e senha) o limite é ' + vezes + 'x maior. '
          : 'Seu limite de convidado acabou por hoje. Crie uma conta para continuar. '), link);
        aviso.hidden = false;
      }
      sub.textContent = cfg.exigir_login ? 'Necessário para perguntar' : 'Com e-mail · limite próprio';
      chip.href = '/entrar?voltar=' + encodeURIComponent(location.pathname + location.search);
      chip.onclick = null;
    }
    if (window.TutorShell) window.TutorShell.atualizarCota();
  }

  pronto = iniciar().catch(function (e) { console.warn(e); return { cfg: { contas: false }, cliente: null }; });
  pronto.then(desenharChip);

  window.TutorConta = {
    pronto: pronto,
    sair: async function () {
      var p = await pronto;
      if (p.cliente) await p.cliente.auth.signOut();
      gravarCookie(null);
    }
  };
})();
