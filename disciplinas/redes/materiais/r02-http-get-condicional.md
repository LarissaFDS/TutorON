---
id: redes-http-get-condicional-proxy-stateless
titulo: HTTP: GET condicional (If-Modified-Since, 304 Not Modified) e Web Proxy (cache), protocolo stateless e stateful (HTTP, TCP, SMTP, FTP, UDP)
assunto: redes-02-aplicacao
tipo: prova
questao: prova 1 2012 Q4-Q5; AB1 2017 Q8; prova 2020.1 Q2; AB1 2020.1 Q3; reposição AB1 2020.1 Q3
resolucao: sim
fonte: Provas de 2012, 2017 e 2020.1 de Redes de Computadores 1, Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Redes de Computadores 1 (COMP — Prof. Leandro Melo de Sales); provas de 2012, 2017 e 2020.1
fontes_catalogo: ufal-leandro-provas-redes
autoria: Questões do Prof. Leandro Melo de Sales (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, fotos e PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Provas de Redes de Computadores 1 do Prof. Leandro Melo de Sales (UFAL), prova 1 2012 Q4-Q5; AB1 2017 Q8; prova 2020.1 Q2; AB1 2020.1 Q3; reposição AB1 2020.1 Q3 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Web Proxy (cache):** o navegador manda as requisições ao proxy; se o proxy tem uma cópia, responde ele mesmo, senão busca no servidor de origem, guarda e repassa. Vantagens: resposta mais rápida, menos tráfego no enlace de acesso da instituição, menos carga no servidor de origem.

**Problema:** a cópia pode estar velha. **GET condicional:** o proxy guarda a data `Last-Modified` da resposta e, ao revalidar, envia
```
GET /pagina.html HTTP/1.1
Host: www.exemplo.br
If-Modified-Since: Wed, 10 Jun 2020 12:00:00 GMT
```
Se o objeto não mudou, o servidor responde **`304 Not Modified` sem corpo** (economiza a transferência) e o proxy usa a cópia. Se mudou, responde `200 OK` com o objeto novo. (Variante: `ETag` com `If-None-Match`.)

**Stateless × stateful:** um protocolo *stateless* não guarda, no servidor, estado de interações anteriores. Cada requisição se basta. Um *stateful* mantém estado da sessão.
- HTTP: **stateless** (cookies criam estado na aplicação, não no protocolo);
- TCP: **stateful** (estado da conexão: números de sequência, janelas);
- SMTP e FTP: **stateful** (sessão com comandos em sequência; o FTP guarda diretório atual e usuário);
- UDP: **stateless**.

Na questão de múltipla escolha de 2017 (HTTP, TCP, SMTP, FTP, UDP), a sequência certa é: stateless, stateful, stateful, stateful, stateless.

**Verificação:** `test_get_condicional` sobe o `http.server` do Python em localhost, pede o arquivo (200 com `Last-Modified`) e repete com `If-Modified-Since`: vem 304 sem corpo; depois de alterar o arquivo, vem 200 de novo.
