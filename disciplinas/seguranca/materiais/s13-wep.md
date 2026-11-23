---
id: seguranca-redes-sem-fio-wep-rc4-vetor-de-inicializacao-crc-fraquezas-wpa2
titulo: Segurança em redes sem fio: modo de operação do WEP (RC4, chave compartilhada, vetor de inicialização de 24 bits, ICV com CRC-32), por que é fraco e o que o substituiu (WPA2, WPA3, 802.11i)
assunto: seg-04-seguranca-em-redes
tipo: prova
questao: AB2, Final e Reposição AB2, questão 3 (WEP)
resolucao: sim
fonte: Provas (2020.1 e 2020.2) e listas semanais de Segurança de Sistemas Computacionais do IC-UFAL
curso: Ciência da Computação (UFAL), COMP403 Segurança de Sistemas Computacionais (ênfase Sistemas de Informação); provas de 2020.1 e 2020.2 (algumas com cabeçalho de Engenharia da Computação)
fontes_catalogo: ufal-seguranca-provas-listas
autoria: Questões das provas e listas da disciplina (IC-UFAL; professor não identificado nos PDFs); explicação da equipe TutorON
licenca: Não declarada (provas e listas); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Segurança de Sistemas Computacionais (IC-UFAL), AB2, Final e Reposição AB2, questão 3 (WEP) (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Operação do WEP** (802.11 original):
1. emissor e ponto de acesso compartilham uma chave $K$ de 40 ou 104 bits;
2. para cada quadro, o emissor escolhe um **vetor de inicialização (IV) de 24 bits** e gera o fluxo de chave $\text{RC4}(IV \,\|\, K)$;
3. calcula o **ICV**, um CRC-32 dos dados, e faz o XOR de (dados ‖ ICV) com o fluxo;
4. envia o **IV em claro** junto com o quadro cifrado;
5. o receptor junta o IV com $K$, gera o mesmo fluxo, decifra e confere o ICV.

A autenticação de chave compartilhada usa desafio e resposta com a mesma cifra.

**Fraquezas:**
- **IV curto:** só $2^{24}$ valores. Repetem rápido, e IV repetido significa fluxo repetido. O XOR de dois cifrados com o mesmo fluxo é o XOR dos dois textos claros;
- pelo paradoxo do aniversário, a chance de repetição passa de 50% por volta de 4 800 quadros;
- **CRC-32 não é MAC:** é linear. Dá para alterar bits do cifrado e corrigir o ICV sem saber a chave, então não há integridade real;
- chave fixa e compartilhada por todos, sem gerência de chaves;
- fraquezas do RC4 com IVs conhecidos permitem recuperar a chave capturando tráfego.

**O que usar:** WPA2 (802.11i, com AES-CCMP: chave por sessão, MIC criptográfico e *4-way handshake*) ou **WPA3** (SAE), com 802.1X/EAP nas empresas. WEP não deve ser usado.

**Verificação:** `test_crc32_e_linear` mostra com `zlib.crc32` que o CRC do XOR de duas mensagens se obtém dos CRCs, sem chave; `test_repeticao_de_iv` calcula pelo aniversário que, com $2^{24}$ IVs, a chance de repetição passa de 50% por volta de 4 823 quadros.
