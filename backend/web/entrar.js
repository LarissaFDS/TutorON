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
    $('esqueci').hidden = criar;
    status('');
  }
  $('aba-entrar').addEventListener('click', function () { modo(false); });
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

    $('google').addEventListener('click', async function () {
      status('Abrindo o Google…');
      var r = await auth.signInWithOAuth({ provider: 'google',
        options: { redirectTo: location.origin + '/entrar?voltar=' + encodeURIComponent(voltar) } });
      if (r.error) status(traduzir(r.error.message), true);
    });

    $('form-email').addEventListener('submit', async function (e) {
      e.preventDefault();
      var email = $('email').value.trim(), senha = $('senha').value;
      if (!email || !$('email').checkValidity()) { status('Digite um e-mail válido.', true); $('email').focus(); return; }
      if (senha.length < 8) { status('A senha precisa ter pelo menos 8 caracteres.', true); $('senha').focus(); return; }
      $('enviar-email').disabled = true;
      status(criando ? 'Criando sua conta…' : 'Entrando…');
      try {
        var r = criando
          ? await auth.signUp({ email: email, password: senha, options: { emailRedirectTo: location.origin + '/entrar' } })
          : await auth.signInWithPassword({ email: email, password: senha });
        if (r.error) throw r.error;
        if (criando && !r.data.session) status('Conta criada. Abra o link que enviamos para ' + email + ' para confirmar.');
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
