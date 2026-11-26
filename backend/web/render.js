/* TutorON — renderização das respostas: Markdown (marked) + fórmulas (KaTeX), sanitizado (DOMPurify).
 *
 * Por que o cuidado com a ordem: o Markdown estraga LaTeX ("_" e "*" viram
 * itálico, "\\" vira quebra). Então as fórmulas são retiradas do texto antes
 * do marked, trocadas por marcadores, e só voltam depois, já renderizadas
 * pelo KaTeX. Código (``` e `) é preservado intacto: "$" dentro de código não
 * é fórmula.
 *
 * Aceita os delimitadores que os modelos usam: $…$, $$…$$, \(…\) e \[…\].
 * Se as bibliotecas não carregarem, mostra o texto puro.
 */
(function (global) {
  'use strict';

  var hasLibs = function () { return global.marked && global.DOMPurify && global.katex; };

  if (global.marked) {
    global.marked.setOptions({ gfm: true, breaks: false });
  }

  // Trechos de código não podem ter fórmulas extraídas.
  var CODE = /(```[\s\S]*?(?:```|$)|~~~[\s\S]*?(?:~~~|$)|`[^`\n]+`)/g;
  // Ordem importa: blocos antes de inline.
  var MATH = [
    { re: /\$\$([\s\S]+?)\$\$/g, display: true },
    { re: /\\\[([\s\S]+?)\\\]/g, display: true },
    { re: /\\\(([\s\S]+?)\\\)/g, display: false },
    // $x$ inline: não abre com espaço, não fecha com espaço, não é "R$ 5" nem "$5".
    { re: /(^|[^\\$\w])\$(?![\s$])([^$\n]+?)(?<![\s\\])\$(?!\d)/g, display: false, lead: true },
    // "$ x $" com espaços (estilo de alguns modelos locais): só se o miolo parecer fórmula.
    { re: /(^|[^\\$\w])\$ ([^$\n]*?[\\^_=+(){}<>|][^$\n]*?|[A-Za-z]) \$(?!\d)/g, display: false, lead: true }
  ];

  function protectMath(text, store) {
    return text.split(CODE).map(function (part, i) {
      if (i % 2 === 1) return part; // código: intacto
      MATH.forEach(function (m) {
        part = part.replace(m.re, function (all, a, b) {
          var lead = m.lead ? a : '';
          var tex = m.lead ? b : a;
          store.push({ tex: tex.trim(), display: m.display });
          var token = 'KTXMATH' + (store.length - 1) + 'KTX';
          // Fórmula em bloco vira parágrafo próprio.
          return lead + (m.display ? '\n\n' + token + '\n\n' : token);
        });
      });
      return part;
    }).join('');
  }

  function renderMath(item) {
    try {
      return global.katex.renderToString(item.tex, {
        displayMode: item.display, throwOnError: false, strict: 'ignore', trust: false, output: 'html'
      });
    } catch (e) {
      var span = document.createElement('code');
      span.textContent = item.tex;
      return span.outerHTML;
    }
  }

  function toHtml(text) {
    var store = [];
    var src = String(text || '').replace(/\r\n?/g, '\n');
    var protectedText = protectMath(src, store);
    var html = global.DOMPurify.sanitize(global.marked.parse(protectedText), {
      USE_PROFILES: { html: true }, FORBID_TAGS: ['style', 'img', 'iframe', 'form', 'input'], FORBID_ATTR: ['style']
    });
    // Bloco sozinho num parágrafo: tirar o <p> para o KaTeX centralizar.
    html = html.replace(/<p>\s*KTXMATH(\d+)KTX\s*<\/p>/g, function (all, n) {
      return store[+n].display ? '<div class="math-display">' + renderMath(store[+n]) + '</div>' : all;
    });
    return html.replace(/KTXMATH(\d+)KTX/g, function (all, n) {
      var item = store[+n];
      return item ? renderMath(item) : all;
    });
  }

  function render(el, text) {
    if (!hasLibs()) {
      el.textContent = text;
      el.classList.add('is-plain');
      return;
    }
    try {
      el.innerHTML = toHtml(text);
      el.classList.remove('is-plain');
      mapas(el);
      // Links das respostas abrem fora do site.
      el.querySelectorAll('a[href]').forEach(function (a) { a.target = '_blank'; a.rel = 'noopener noreferrer'; });
    } catch (err) {
      el.textContent = text;
      el.classList.add('is-plain');
      if (global.console) console.warn('TutorON: renderização caiu para texto puro.', err);
    }
  }

  // ```mapa (ferramenta "Mapa mental"): linhas com 2 espaços de recuo por nível viram uma árvore visual.
  function mapas(el) {
    el.querySelectorAll('pre > code.language-mapa').forEach(function (code) {
      var linhas = code.textContent.split(/\r?\n/).filter(function (l) { return l.trim(); });
      if (!linhas.length) return;
      var raiz = document.createElement('div');
      raiz.className = 'mapa-mental';
      var pilha = [{ nivel: -1, ul: document.createElement('ul') }];
      raiz.append(pilha[0].ul);
      linhas.forEach(function (l) {
        var nivel = Math.floor((l.match(/^\s*/)[0].replace(/	/g, '  ').length) / 2);
        var rotulo = l.trim().replace(/^[-*•]\s*/, '');
        while (pilha.length > 1 && pilha[pilha.length - 1].nivel >= nivel) pilha.pop();
        var topo = pilha[pilha.length - 1];
        var li = document.createElement('li'), span = document.createElement('span');
        span.innerHTML = toHtml(rotulo).replace(/^<p>|<\/p>\s*$/g, '');
        li.append(span);
        topo.ul.append(li);
        var filhos = document.createElement('ul');
        li.append(filhos);
        pilha.push({ nivel: nivel, ul: filhos });
      });
      raiz.querySelectorAll('ul').forEach(function (u) { if (!u.children.length) u.remove(); });
      code.parentNode.replaceWith(raiz);
    });
  }

  // Enunciado do aluno: só texto, preservando quebras de linha.
  function renderPlain(el, text) {
    el.textContent = text;
    el.classList.add('is-plain');
  }

  global.TutorONRender = { toHtml: toHtml, render: render, renderPlain: renderPlain };
})(typeof window !== 'undefined' ? window : globalThis);
