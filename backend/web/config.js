/* Configurações do aluno: tema, tamanho da letra, foto de perfil, sobre/créditos e sair.
 * Tudo fica neste navegador (localStorage); nada disso vai para o servidor.
 * O tema é aplicado assim que o script carrega (no <head>) para a página não "piscar". */
(function () {
  'use strict';
  function ler(chave) { try { return localStorage.getItem(chave); } catch (e) { return null; } }
  function gravar(chave, valor) {
    try { if (valor === null) localStorage.removeItem(chave); else localStorage.setItem(chave, valor); } catch (e) { /* modo privado */ }
  }

  function aplicarTema() {
    var tema = ler('tutoron-tema');
    if (tema === 'claro') document.documentElement.dataset.theme = 'light';
    else if (tema === 'escuro') document.documentElement.dataset.theme = 'dark';
    else delete document.documentElement.dataset.theme;
    document.documentElement.classList.toggle('letra-grande', ler('tutoron-letra') === 'grande');
  }
  aplicarTema();

  var EQUIPE = ['Matheus Pedro', 'Otávio Menezes', 'Larissa Ferreira', 'Cleverson'];

  function el(tag, cls, texto) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (texto != null) n.textContent = texto;
    return n;
  }

  function fotoPerfil() { return ler('tutoron-foto'); }
  function aplicarFoto() {
    var foto = fotoPerfil();
    document.querySelectorAll('.conta-chip .perfil__avatar').forEach(function (av) {
      av.replaceChildren();
      if (foto) { var img = el('img'); img.src = foto; img.alt = ''; av.append(img); }
      else av.textContent = '👤';
    });
  }

  // Reduz a foto para 128 px (JPEG ~6 KB) antes de guardar.
  function reduzir(arquivo) {
    return new Promise(function (ok, falha) {
      var url = URL.createObjectURL(arquivo);
      var img = new Image();
      img.onload = function () {
        var lado = 128, c = document.createElement('canvas');
        c.width = c.height = lado;
        var menor = Math.min(img.naturalWidth, img.naturalHeight);
        c.getContext('2d').drawImage(img, (img.naturalWidth - menor) / 2, (img.naturalHeight - menor) / 2, menor, menor, 0, 0, lado, lado);
        URL.revokeObjectURL(url);
        ok(c.toDataURL('image/jpeg', 0.85));
      };
      img.onerror = function () { URL.revokeObjectURL(url); falha(new Error('Não consegui abrir esta imagem.')); };
      img.src = url;
    });
  }

  function opcoes(nome, valores, atual, aoMudar) {
    var grupo = el('div', 'config__opcoes');
    grupo.setAttribute('role', 'radiogroup');
    valores.forEach(function (v) {
      var rotulo = el('label', 'config__opcao');
      var input = el('input');
      input.type = 'radio'; input.name = nome; input.value = v[0]; input.checked = v[0] === atual;
      input.addEventListener('change', function () { aoMudar(v[0]); });
      rotulo.append(input, el('span', null, v[1]));
      grupo.append(rotulo);
    });
    return grupo;
  }

  var dialogo = null;
  function montar(conta) {
    var d = el('dialog', 'config');
    d.setAttribute('aria-labelledby', 'config-titulo');
    var topo = el('div', 'config__topo');
    topo.append(el('h2', null, 'Configurações'));
    topo.firstChild.id = 'config-titulo';
    var fechar = el('button', 'icone-btn', '✕');
    fechar.type = 'button'; fechar.setAttribute('aria-label', 'Fechar');
    fechar.addEventListener('click', function () { d.close(); });
    topo.append(fechar);
    d.append(topo);

    // Conta e foto
    var secConta = el('section', 'config__secao');
    secConta.append(el('h3', null, 'Perfil'));
    var linha = el('div', 'config__perfil');
    var avatar = el('span', 'perfil__avatar config__avatar');
    function desenharAvatar() {
      avatar.replaceChildren();
      var f = fotoPerfil();
      if (f) { var i = el('img'); i.src = f; i.alt = 'Sua foto'; avatar.append(i); } else avatar.textContent = '👤';
    }
    desenharAvatar();
    var info = el('div');
    info.append(el('strong', null, conta ? (conta.nome || conta.email) : 'Convidado'),
      el('small', 'dica', conta ? conta.email : 'Sem conta: as conversas não ficam salvas.'));
    linha.append(avatar, info);
    var arquivo = el('input'); arquivo.type = 'file'; arquivo.accept = 'image/*'; arquivo.hidden = true;
    var trocar = el('button', 'botao botao--leve', 'Trocar foto');
    trocar.type = 'button';
    trocar.addEventListener('click', function () { arquivo.click(); });
    var remover = el('button', 'botao botao--leve', 'Remover foto');
    remover.type = 'button';
    remover.addEventListener('click', function () { gravar('tutoron-foto', null); desenharAvatar(); aplicarFoto(); });
    arquivo.addEventListener('change', async function () {
      if (!arquivo.files[0]) return;
      try { gravar('tutoron-foto', await reduzir(arquivo.files[0])); desenharAvatar(); aplicarFoto(); }
      catch (e) { window.alert(e.message); }
    });
    var acoesFoto = el('div', 'config__acoes');
    acoesFoto.append(trocar, remover, arquivo);
    secConta.append(linha, acoesFoto, el('p', 'dica', 'A foto fica só neste aparelho.'));
    d.append(secConta);

    // Aparência
    var secAparencia = el('section', 'config__secao');
    secAparencia.append(el('h3', null, 'Aparência'), el('p', 'config__rotulo', 'Tema'),
      opcoes('tema', [['sistema', 'Igual ao sistema'], ['claro', 'Claro'], ['escuro', 'Escuro']],
        ler('tutoron-tema') || 'sistema', function (v) { gravar('tutoron-tema', v === 'sistema' ? null : v); aplicarTema(); }),
      el('p', 'config__rotulo', 'Tamanho da letra'),
      opcoes('letra', [['normal', 'Normal'], ['grande', 'Grande']], ler('tutoron-letra') || 'normal',
        function (v) { gravar('tutoron-letra', v === 'normal' ? null : v); aplicarTema(); }),
      el('p', 'config__rotulo', 'Idioma'),
      el('p', 'dica', 'Português (Brasil). O TutorON responde em português; outros idiomas ainda não estão disponíveis.'));
    d.append(secAparencia);

    // Sobre e créditos
    var secSobre = el('section', 'config__secao');
    secSobre.append(el('h3', null, 'Sobre o TutorON'),
      el('p', null, 'O TutorON foi criado na disciplina de Empreendedorismo do curso de Engenharia de Computação, ' +
        'para uso do Instituto de Computação (IC/UFAL) e de outros cursos da universidade.'),
      el('p', null, 'Ele é um tutor de apoio no modelo socrático: em vez de entregar a resposta, faz perguntas, ' +
        'dá pistas e cria exercícios para você chegar à solução sozinho. O material de cada disciplina vem ' +
        'das provas e listas dos professores.'),
      el('p', 'config__rotulo', 'Equipe'));
    var lista = el('ul', 'config__equipe');
    EQUIPE.forEach(function (n) { lista.append(el('li', null, n)); });
    secSobre.append(lista);
    d.append(secSobre);

    if (conta) {
      var sair = el('button', 'botao botao--leve config__sair', 'Sair da conta');
      sair.type = 'button';
      sair.addEventListener('click', async function () {
        var tc = window.TutorConta;
        d.close();
        if (tc && tc.confirmarSaida && !(await tc.confirmarSaida())) return;
        if (tc) await tc.sair();
        location.reload();
      });
      d.append(sair);
    }
    d.addEventListener('click', function (e) { if (e.target === d) d.close(); });  // clique fora fecha
    d.addEventListener('close', function () { d.remove(); dialogo = null; });
    document.body.append(d);
    return d;
  }

  window.TutorConfig = {
    abrir: function (conta) {
      if (dialogo) return;
      dialogo = montar(conta || null);
      dialogo.showModal();
    },
    aplicarFoto: aplicarFoto,
  };
  document.addEventListener('DOMContentLoaded', aplicarFoto);
})();
