(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };
  var criando = false;
  var voltar = new URL(location.href).searchParams.get('voltar') || '/';
  if (!voltar.startsWith('/') || voltar.startsWith('//')) voltar = '/';  // só caminhos deste site

  function status(texto, erro) {
    $('entrar-status').textContent = texto;
    if (erro) $('entrar-status').dataset.tone = 'error'; else delete $('entrar-status').dataset.tone;
  }
  function traduzir(msg) {
    var m = (msg || '').toLowerCase();
    if (m.includes('invalid login')) return 'E-mail ou senha incorretos.';
    if (m.includes('email not confirmed')) return 'Confirme seu e-mail pelo link que enviamos antes de entrar.';
    if (m.includes('already registered')) return 'Esse e-mail já tem conta. Use "Entrar".';
    if (m.includes('password')) return 'Senha fraca: use pelo menos 8 caracteres.';
    if (m.includes('rate limit')) return 'Muitas tentativas. Aguarde alguns minutos.';
    return msg || 'Não foi possível concluir. Tente de novo.';
  }
  function modo(criar) {
    criando = criar;
    $('aba-entrar').setAttribute('aria-selected', String(!criar));
    $('aba-criar').setAttribute('aria-selected', String(criar));
    $('enviar-email').textContent = criar ? 'Criar conta' : 'Entrar';
    $('senha').autocomplete = criar ? 'new-password' : 'current-password';
    $('senha-dica').hidden = !criar;
    $('nome').hidden = $('nome-rotulo').hidden = !criar;
    $('nome').required = criar;
    $('esqueci').hidden = criar;
    $('entrar-titulo').textContent = criar ? 'Crie sua conta grátis' : 'Bem-vindo de volta';
    status('');
  }
  $('aba-entrar').addEventListener('click', function () { modo(false); });
  if (new URL(location.href).searchParams.get('criar')) {
    modo(true);
    status('Crie sua conta grátis para continuar: nome, e-mail e senha.');
  }
  $('aba-criar').addEventListener('click', function () { modo(true); });

  window.TutorConta.pronto.then(async function (p) {
    if (!p.cliente) { $('entrar-opcoes').hidden = true; $('entrar-indisponivel').hidden = false; return; }
    var auth = p.cliente.auth;
    var recuperando = location.hash.includes('type=recovery') || location.search.includes('type=recovery');
    auth.onAuthStateChange(async function (evento, sessao) {
      if (evento === 'PASSWORD_RECOVERY') {
        recuperando = true;
        var nova = window.prompt('Digite a nova senha (pelo menos 8 caracteres):') || '';
        if (nova.length < 8) { status('Senha não alterada: use pelo menos 8 caracteres.', true); return; }
        var r = await auth.updateUser({ password: nova });
        if (r.error) { status(traduzir(r.error.message), true); return; }
        location.replace(voltar);
      } else if (sessao && evento === 'SIGNED_IN' && !recuperando) location.replace(voltar);
    });
    if (!recuperando && (await auth.getSession()).data.session) { location.replace(voltar); return; }

    $('form-email').addEventListener('submit', async function (e) {
      e.preventDefault();
      var email = $('email').value.trim(), senha = $('senha').value, nome = $('nome').value.trim().replace(/\s+/g, ' ');
      if (criando && (nome.length < 2 || nome.includes('@'))) { status('Digite seu nome de usuário (pelo menos 2 letras).', true); $('nome').focus(); return; }
      if (!email || !$('email').checkValidity()) { status('Digite um e-mail válido.', true); $('email').focus(); return; }
      if (senha.length < 8) { status('A senha precisa ter pelo menos 8 caracteres.', true); $('senha').focus(); return; }
      $('enviar-email').disabled = true;
      status(criando ? 'Criando sua conta…' : 'Entrando…');
      try {
        if (criando) {
          // A conta é criada pelo servidor, já confirmada (sem e-mail e sem o limite de envios do Supabase).
          var c = await fetch('/api/conta/criar', { method: 'POST', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: email, senha: senha, nome: nome }) });
          if (!c.ok) { var j = await c.json().catch(function () { return {}; }); throw new Error(j.erro || 'Não foi possível criar a conta.'); }
          status('Conta criada. Entrando…');
        }
        var r = await auth.signInWithPassword({ email: email, password: senha });
        if (r.error) throw r.error;
      } catch (erro) { status(traduzir(erro.message), true); }
      finally { $('enviar-email').disabled = false; }
    });

    $('esqueci').addEventListener('click', async function () {
      var email = $('email').value.trim();
      if (!email) { status('Digite seu e-mail acima e clique de novo.', true); $('email').focus(); return; }
      var r = await auth.resetPasswordForEmail(email, { redirectTo: location.origin + '/entrar' });
      status(r.error ? traduzir(r.error.message) : 'Se houver conta com esse e-mail, enviamos um link para criar uma nova senha.', !!r.error);
    });
  });
})();
