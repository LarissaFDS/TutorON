/* Partes comuns do layout do chat nas páginas secundárias (desenhos, uso, planos):
 * barra lateral no celular e cartão do limite de hoje. A página do chat (app.js) tem a sua versão. */
(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };

  function abrirLateral(abrir) {
    if (!$('lateral')) return;
    $('lateral').classList.toggle('aberta', abrir);
    $('veu').hidden = !abrir;
  }
  if ($('abrir-lateral')) $('abrir-lateral').addEventListener('click', function () { abrirLateral(true); });
  if ($('fechar-lateral')) $('fechar-lateral').addEventListener('click', function () { abrirLateral(false); });
  if ($('veu')) $('veu').addEventListener('click', function () { abrirLateral(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') abrirLateral(false); });

  async function atualizarCota() {
    if (!$('cota')) return;
    try {
      var c = await (await fetch('/api/cota', { cache: 'no-store' })).json();
      if (c.admin) {
        $('cota-plano').textContent = 'Administrador';
        $('cota-texto').textContent = 'Sem limite · modo completo';
        $('cota-barra').style.width = '100%';
        return;
      }
      $('cota-plano').textContent = 'Plano ' + (c.plano_nome || 'Grátis');
      $('cota-acao').textContent = c.plano === 'gratis' ? 'Fazer upgrade' : 'Gerenciar';
      if (c.ilimitado) { $('cota-texto').textContent = 'Sem limite neste servidor'; $('cota-barra').style.width = '100%'; return; }
      var pct = Math.max(0, Math.round(100 * c.restantes / c.limite));
      $('cota-barra').style.width = pct + '%';
      $('cota').classList.toggle('esgotado', c.restantes <= 0);
      $('cota-texto').textContent = c.restantes > 0 ? pct + '% do limite de hoje' : 'Limite de hoje esgotado';
    } catch (e) { $('cota-texto').textContent = 'Limite indisponível agora'; }
  }
  atualizarCota();

  window.TutorShell = { fecharLateral: function () { abrirLateral(false); }, atualizarCota: atualizarCota };
})();
