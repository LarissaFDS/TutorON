// Executar com: node --test backend/tests/test_foto_frontend.cjs
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');

const source = fs.readFileSync(path.join(__dirname, '../web/app.js'), 'utf8');
const photo = source.slice(source.indexOf('  /* Foto do papel:'), source.indexOf('  /* Animação (Manim):'));
const submit = source.slice(source.indexOf("  $('form-tutor').addEventListener('submit'"), source.indexOf('  async function retomarTutor('));
const deferred = () => {
  let resolve;
  const promise = new Promise(r => { resolve = r; });
  return { promise, resolve };
};
const tick = () => new Promise(r => setImmediate(r));
const result = text => ({ status: 'pronta', leitura: { enunciado: text, legivel: true, confianca: 'alta' } });

function setup() {
  const nodes = new Map();
  const paint = [];
  const node = () => ({ hidden: true, value: '', dataset: {}, handlers: {},
    addEventListener(event, fn) { this.handlers[event] = fn; },
    replaceChildren() {}, append() {}, focus() {},
    getContext() { return { fillRect() { paint.push('fundo'); }, drawImage() { paint.push('imagem'); } }; },
    toDataURL() { return 'data:image/jpeg;base64,teste'; }
  });
  const $ = id => {
    if (!nodes.has(id)) nodes.set(id, node());
    return nodes.get(id);
  };
  const context = vm.createContext({ $, paint, gerando: 0, enviando: false,
    document: { createElement: node, createTextNode: text => text, querySelectorAll: () => [] },
    el: node, rolarPara() {}, setStatus(n, text) { n.textContent = text; },
    URL: { createObjectURL() { return 'blob:teste'; }, revokeObjectURL() {} },
    Image: class { constructor() { this.naturalWidth = 100; this.naturalHeight = 100; }
      set src(value) { queueMicrotask(() => this.onload()); } },
    postJSON: async () => ({ id: 'tarefa' }), acompanhar: async () => result('foto'),
    ajudaEscolhida: () => 'auto', perguntar: async () => true
  });
  vm.runInContext(photo + '\n' + submit, context);
  return { context, $, select(file = {}) {
    $('foto-arquivo').files = [file];
    return $('foto-arquivo').handlers.change.call($('foto-arquivo'));
  }, submit() { return $('form-tutor').handlers.submit({ preventDefault() {} }); } };
}

test('pergunta aguarda a leitura da foto, sem enviar texto sozinho', async () => {
  const app = setup();
  const waiting = deferred();
  app.context.comprimir = () => waiting.promise;
  const upload = app.select();
  app.$('pergunta').value = 'Confira minha tentativa';
  let sent = false;
  app.context.perguntar = async () => { sent = true; };
  await app.submit();
  assert.equal(sent, false);
  assert.match(app.$('status-tutor').textContent, /Aguarde a leitura/);
  waiting.resolve('imagem');
  await upload;
  assert.equal(app.context.gerando, 0);
});

test('resultado de uma foto anterior não sobrescreve a foto atual', async () => {
  const app = setup();
  const first = deferred(), second = deferred();
  let calls = 0;
  app.context.comprimir = async () => 'imagem';
  app.context.acompanhar = () => (++calls === 1 ? first.promise : second.promise);
  const oldUpload = app.select();
  await tick();
  const newUpload = app.select();
  await tick();
  second.resolve(result('nova foto'));
  await newUpload;
  first.resolve(result('foto antiga'));
  await oldUpload;
  assert.equal(app.$('foto-enunciado').value, 'nova foto');
  assert.equal(app.context.gerando, 0);
});

test('descartar durante leitura impede que o resultado reapareça', async () => {
  const app = setup();
  const waiting = deferred();
  app.context.comprimir = async () => 'imagem';
  app.context.acompanhar = () => waiting.promise;
  const upload = app.select();
  await tick();
  app.context.limparFoto();
  waiting.resolve(result('descartada'));
  await upload;
  assert.equal(app.$('foto-conferir').hidden, true);
});

test('PNG transparente ganha fundo branco antes de virar JPEG', async () => {
  const app = setup();
  await app.context.comprimir({});
  assert.deepEqual(Array.from(app.context.paint), ['fundo', 'imagem']);
});

test('resposta da pergunta anterior preserva uma nova foto selecionada', async () => {
  const app = setup();
  const waiting = deferred();
  app.context.fotoConfirmada = 'foto anterior';
  app.$('pergunta').value = 'Me ajude com esta foto';
  app.context.perguntar = () => waiting.promise;
  const sending = app.submit();
  await app.select();
  waiting.resolve(true);
  await sending;
  assert.equal(app.$('foto-conferir').hidden, false);
  assert.equal(app.$('foto-enunciado').value, 'foto');
});
