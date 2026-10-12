/* TutorON — renderizador local das respostas (Markdown + TeX leve).
 *
 * Por que existe: as respostas dos modelos chegam em Markdown com fórmulas
 * em LaTeX. Mostradas como texto cru (### , **, \( T(n) \)) elas ficam
 * ilegíveis, e o aluno acaba avaliando a formatação em vez do conteúdo.
 * A página de validação precisa funcionar offline, então não dá para
 * depender de marked/KaTeX via CDN.
 *
 * Segurança: todo texto de entrada é escapado; as únicas tags geradas são
 * as desta lista (p, br, h3, h4, ul, ol, li, strong, em, code, pre,
 * blockquote, hr, table, sup, sub, span, div). Não gera links nem atributos
 * além de `class` e `start` numérico.
 *
 * Justiça do teste cego: as duas respostas passam pelo mesmo renderizador.
 */
(function (global) {
  'use strict';

  var ESC = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' };
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return ESC[c]; }); }

  // ------------------------------------------------------------------ TeX leve
  var SYMBOLS = {
    le: '≤', leq: '≤', ge: '≥', geq: '≥', neq: '≠', ne: '≠', approx: '≈', equiv: '≡',
    cdot: '·', times: '×', div: '÷', pm: '±', to: '→', rightarrow: '→', leftarrow: '←',
    gets: '←', Rightarrow: '⇒', implies: '⇒', Leftarrow: '⇐', iff: '⇔', Leftrightarrow: '⇔',
    longrightarrow: '⟶', mapsto: '↦', infty: '∞', in: '∈', notin: '∉', subset: '⊂',
    subseteq: '⊆', supseteq: '⊇', cup: '∪', cap: '∩', emptyset: '∅', varnothing: '∅',
    forall: '∀', exists: '∃', neg: '¬', lnot: '¬', land: '∧', wedge: '∧', lor: '∨', vee: '∨',
    sum: 'Σ', prod: 'Π', ldots: '…', dots: '…', cdots: '⋯', vdots: '⋮', lfloor: '⌊',
    rfloor: '⌋', lceil: '⌈', rceil: '⌉', langle: '⟨', rangle: '⟩', Theta: 'Θ', theta: 'θ',
    Omega: 'Ω', omega: 'ω', alpha: 'α', beta: 'β', gamma: 'γ', Gamma: 'Γ', delta: 'δ',
    Delta: 'Δ', epsilon: 'ε', varepsilon: 'ε', lambda: 'λ', mu: 'μ', pi: 'π', sigma: 'σ',
    Sigma: 'Σ', phi: 'φ', varphi: 'φ', Phi: 'Φ', rho: 'ρ', tau: 'τ', log: 'log', lg: 'lg',
    ln: 'ln', exp: 'exp', max: 'max', min: 'min', mod: ' mod ', bmod: ' mod ', gcd: 'mdc',
    mid: ' | ', vert: '|', lvert: '|', rvert: '|', star: '⋆', circ: '∘', ll: '≪', gg: '≫',
    sim: '∼', perp: '⊥', ell: 'ℓ', prime: '′', quad: ' ', qquad: '  ',
    lim: 'lim', sqrt: '√', not: '¬', leftrightarrow: '↔', uparrow: '↑', downarrow: '↓'
  };
  var BLACKBOARD = { N: 'ℕ', Z: 'ℤ', R: 'ℝ', Q: 'ℚ', C: 'ℂ' };
  var SIZERS = { left: 1, right: 1, big: 1, Big: 1, bigg: 1, Bigg: 1, displaystyle: 1, textstyle: 1, limits: 1, nolimits: 1 };
  var TEXTUAL = { text: 1, textrm: 1, mathrm: 1, textbf: 1, mathbf: 1, mathit: 1, textit: 1, operatorname: 1, mathsf: 1, texttt: 1, mathtt: 1, mbox: 1 };

  function strip(html) { return html.replace(/<[^>]+>/g, ''); }

  function tex(src) {
    var out = '';
    var i = 0;
    function group() {
      while (src[i] === ' ') i++;
      if (i >= src.length) return '';
      if (src[i] === '{') {
        var depth = 0, start = i + 1;
        for (; i < src.length; i++) {
          if (src[i] === '\\') { i++; continue; }
          if (src[i] === '{') depth++;
          else if (src[i] === '}' && --depth === 0) { i++; return src.slice(start, i - 1); }
        }
        return src.slice(start);
      }
      if (src[i] === '\\') {
        var m = /^\\([a-zA-Z]+|.)/.exec(src.slice(i));
        i += m[0].length;
        return m[0];
      }
      return src[i++];
    }
    while (i < src.length) {
      var ch = src[i];
      if (ch === '\\') {
        var m = /^\\([a-zA-Z]+|.?)/.exec(src.slice(i));
        var name = m[1];
        i += m[0].length;
        if (name === 'frac' || name === 'dfrac' || name === 'tfrac') {
          var a = tex(group()), b = tex(group());
          var wrap = function (x) { return /[\s+\-−·×]/.test(strip(x).trim()) ? '(' + x + ')' : x; };
          out += wrap(a) + '/' + wrap(b);
        } else if (name === 'binom') {
          out += 'C(' + tex(group()) + ', ' + tex(group()) + ')';
        } else if (name === 'sqrt') {
          var g = tex(group());
          out += '√' + (strip(g).length > 1 ? '(' + g + ')' : g);
        } else if (TEXTUAL[name]) {
          out += '<span class="math-text">' + esc(group()) + '</span>';
        } else if (name === 'mathbb' || name === 'mathcal') {
          var letter = group();
          out += BLACKBOARD[letter] || esc(letter);
        } else if (name === 'begin' || name === 'end') {
          group();
        } else if (SIZERS[name]) {
          /* só ajustam tamanho: ignorar */
        } else if (SYMBOLS.hasOwnProperty(name)) {
          out += SYMBOLS[name];
        } else if (name === '\\') {
          out += '<br>';
        } else if (name === ',' || name === ':' || name === ';' || name === ' ') {
          out += ' ';
        } else if (name === '!' || name === '') {
          /* espaço negativo ou barra solta */
        } else {
          out += esc(name); // \{ \} \% \_ \& e comandos desconhecidos viram o próprio nome
        }
      } else if (ch === '^' || ch === '_') {
        i++;
        var tag = ch === '^' ? 'sup' : 'sub';
        out += '<' + tag + '>' + tex(group()) + '</' + tag + '>';
      } else if (ch === '{' || ch === '}' || ch === '&') {
        i++;
      } else {
        out += esc(ch);
        i++;
      }
    }
    return out;
  }

  // ------------------------------------------------------------------ inline
  var INLINE_TOKEN = /(`+)([\s\S]*?)\1|\\\(([\s\S]+?)\\\)|\\\[([\s\S]+?)\\\]|\$\$([\s\S]+?)\$\$|\$(?=\S)([^$\n]+?)(?<=\S)\$/g;

  function inline(raw) {
    var saved = [];
    var marked = raw.replace(INLINE_TOKEN, function (all, ticks, code, m1, m2, m3, m4) {
      var html;
      if (ticks) html = '<code>' + esc(code.trim()) + '</code>';
      else if (m2 !== undefined || m3 !== undefined) html = '<span class="math-block">' + tex(m2 !== undefined ? m2 : m3) + '</span>';
      else html = '<span class="math">' + tex(m1 !== undefined ? m1 : m4) + '</span>';
      saved.push(html);
      return '\u0000' + (saved.length - 1) + '\u0000';
    });
    var html = esc(marked)
      .replace(/\*\*(?=\S)([\s\S]+?)\*\*/g, '<strong>$1</strong>')
      .replace(/__(?=\S)([\s\S]+?)__/g, '<strong>$1</strong>')
      .replace(/(^|[^*\w])\*(?=[^\s*])([^*\n]+?)\*(?!\w)/g, '$1<em>$2</em>')
      .replace(/\n/g, '<br>');
    return html.replace(/\u0000(\d+)\u0000/g, function (_, n) { return saved[+n]; });
  }

  // ------------------------------------------------------------------ blocos
  var RE = {
    fence: /^(\s*)(```+|~~~+)/,
    heading: /^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$/,
    hr: /^\s{0,3}([-*_])(\s*\1){2,}\s*$/,
    quote: /^\s{0,3}>\s?/,
    item: /^(\s*)([-*+]|\d{1,3}[.)])\s+(.*)$/,
    indented: /^( {4}|\t)/,
    mathOpen: /^\s*(\\\[|\$\$)\s*$/,
    tableSep: /^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$/
  };

  function indentOf(line) { return line.match(/^\s*/)[0].replace(/\t/g, '    ').length; }
  function dedent(line, n) {
    var expanded = line.replace(/^\t+/, function (t) { return '    '.repeat(t.length); });
    var cut = Math.min(n, indentOf(expanded));
    return expanded.slice(cut);
  }
  function startsBlock(line) {
    return RE.fence.test(line) || RE.heading.test(line) || RE.hr.test(line) || RE.item.test(line) || RE.mathOpen.test(line) || RE.quote.test(line);
  }
  function kindOf(marker) { return /\d/.test(marker) ? 'ol' : 'ul'; }

  function blocks(lines) {
    var out = [];
    var i = 0;
    var afterBlank = true;
    while (i < lines.length) {
      var line = lines[i];
      var m;
      if (!line.trim()) { i++; afterBlank = true; continue; }

      if ((m = RE.fence.exec(line))) {
        var pad = m[1].length, fence = m[2], body = [];
        i++;
        while (i < lines.length && !new RegExp('^\\s*' + fence[0] + '{' + fence.length + ',}\\s*$').test(lines[i])) {
          body.push(dedent(lines[i], pad));
          i++;
        }
        i++;
        out.push('<pre><code>' + esc(body.join('\n')) + '</code></pre>');
      } else if (RE.mathOpen.test(line)) {
        var closer = line.trim() === '$$' ? /^\s*\$\$\s*$/ : /^\s*\\\]\s*$/;
        var math = [];
        i++;
        while (i < lines.length && !closer.test(lines[i])) { math.push(lines[i]); i++; }
        i++;
        out.push('<div class="math-block">' + tex(math.join(' ')) + '</div>');
      } else if ((m = RE.heading.exec(line))) {
        var tag = m[1].length <= 2 ? 'h3' : 'h4';
        out.push('<' + tag + '>' + inline(m[2]) + '</' + tag + '>');
        i++;
      } else if (RE.hr.test(line)) {
        out.push('<hr>');
        i++;
      } else if (RE.quote.test(line)) {
        var quoted = [];
        while (i < lines.length && RE.quote.test(lines[i])) { quoted.push(lines[i].replace(RE.quote, '')); i++; }
        out.push('<blockquote>' + blocks(quoted) + '</blockquote>');
      } else if (RE.item.test(line)) {
        var res = list(lines, i);
        out.push(res.html);
        i = res.next;
      } else if (afterBlank && RE.indented.test(line)) {
        var code = [];
        while (i < lines.length && (RE.indented.test(lines[i]) || !lines[i].trim())) { code.push(dedent(lines[i], 4)); i++; }
        while (code.length && !code[code.length - 1].trim()) code.pop();
        out.push('<pre><code>' + esc(code.join('\n')) + '</code></pre>');
      } else if (/^\s*\|/.test(line) && i + 1 < lines.length && RE.tableSep.test(lines[i + 1])) {
        var rows = [line];
        i += 2;
        while (i < lines.length && /^\s*\|/.test(lines[i])) { rows.push(lines[i]); i++; }
        out.push(table(rows));
      } else {
        var para = [line.trim()];
        i++;
        while (i < lines.length && lines[i].trim() && !startsBlock(lines[i])) { para.push(lines[i].trim()); i++; }
        out.push('<p>' + inline(para.join('\n')) + '</p>');
      }
      afterBlank = false;
    }
    return out.join('');
  }

  function cells(row) {
    return row.trim().replace(/^\|/, '').replace(/\|$/, '').split('|').map(function (c) { return c.trim(); });
  }
  function table(rows) {
    var head = cells(rows[0]).map(function (c) { return '<th>' + inline(c) + '</th>'; }).join('');
    var body = rows.slice(1).map(function (r) {
      return '<tr>' + cells(r).map(function (c) { return '<td>' + inline(c) + '</td>'; }).join('') + '</tr>';
    }).join('');
    return '<div class="table-scroll"><table class="table"><thead><tr>' + head + '</tr></thead><tbody>' + body + '</tbody></table></div>';
  }

  function list(lines, start) {
    var first = RE.item.exec(lines[start]);
    var base = indentOf(first[1]);
    var kind = kindOf(first[2]);
    var items = [];
    var i = start;
    while (i < lines.length) {
      var m = RE.item.exec(lines[i]);
      if (m && indentOf(m[1]) === base) {
        if (kindOf(m[2]) !== kind) break;
        var contentIndent = m[0].length - m[3].length;
        var body = [m[3]];
        i++;
        while (i < lines.length) {
          var l = lines[i];
          if (!l.trim()) {
            var next = lines[i + 1];
            if (next !== undefined && next.trim() && indentOf(next) > base) { body.push(''); i++; continue; }
            break;
          }
          var mi = RE.item.exec(l);
          if (indentOf(l) > base) { body.push(dedent(l, contentIndent)); i++; continue; }
          if (mi || startsBlock(l)) break;
          body.push(l.trim()); // continuação preguiçosa
          i++;
        }
        items.push({ number: parseInt(m[2], 10), body: body });
        if (i < lines.length && !lines[i].trim()) {
          var j = i;
          while (j < lines.length && !lines[j].trim()) j++;
          var mj = j < lines.length && RE.item.exec(lines[j]);
          if (mj && indentOf(mj[1]) === base && kindOf(mj[2]) === kind) { i = j; continue; }
          break;
        }
      } else {
        break;
      }
    }
    var html = items.map(function (it) {
      var inner = blocks(it.body);
      var single = /^<p>([\s\S]*)<\/p>$/.exec(inner);
      if (single && single[1].indexOf('<p>') === -1) inner = single[1];
      else inner = inner.replace(/^<p>([\s\S]*?)<\/p>/, '$1');
      return '<li>' + inner + '</li>';
    }).join('');
    var startAttr = kind === 'ol' && items.length && items[0].number > 1 ? ' start="' + items[0].number + '"' : '';
    return { html: '<' + kind + startAttr + '>' + html + '</' + kind + '>', next: i };
  }

  function toHtml(text) {
    return blocks(String(text || '').replace(/\r\n?/g, '\n').split('\n'));
  }

  // ------------------------------------------------------------------ enunciado
  // Enunciados de PAA misturam texto com pseudocódigo sem cercas de código.
  var CODE_START = /^\s*(procedure|function|algorithm|algoritmo|procedimento|fun[cç][aã]o|for|while|if|return|def)\b/i;
  function questionHtml(text) {
    return String(text || '').replace(/\r\n?/g, '\n').split(/\n\s*\n/).map(function (chunk) {
      var lines = chunk.split('\n');
      var indented = lines.filter(function (l) { return /^\s{2,}\S/.test(l); }).length;
      if (CODE_START.test(lines[0]) || indented >= 2) {
        return '<pre class="pseudocode">' + esc(chunk.replace(/\s+$/, '')) + '</pre>';
      }
      return '<p>' + inline(chunk.trim()) + '</p>';
    }).join('');
  }

  function safely(el, text, fn) {
    try {
      el.innerHTML = fn(text);
      el.classList.remove('is-plain');
    } catch (err) {
      el.textContent = text;
      el.classList.add('is-plain');
      if (global.console) console.warn('TutorON: renderização caiu para texto puro.', err);
    }
  }

  global.TutorONText = {
    toHtml: toHtml,
    tex: tex,
    render: function (el, text) { safely(el, text, toHtml); },
    renderQuestion: function (el, text) { safely(el, text, questionHtml); },
    firstLine: function (text) {
      var first = String(text || '').trim().split(/\n\s*\n|\n/)[0] || '';
      return first.length > 160 ? first.slice(0, 157).trimEnd() + '…' : first;
    }
  };
})(typeof window !== 'undefined' ? window : globalThis);
