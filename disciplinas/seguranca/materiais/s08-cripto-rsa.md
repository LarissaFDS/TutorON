---
id: seguranca-criptografia-simetrica-assimetrica-rsa-chaves-p-q-cifrar-decifrar-exemplo
titulo: Criptografia simétrica e assimétrica (diferença), algoritmo RSA passo a passo com primos pequenos p e q: n, phi(n), expoente público e privado, cifrar e decifrar letras
assunto: seg-03-criptografia-e-autenticacao
tipo: lista
questao: Lista 8, questões 1 e 2; Lista 9, questão 2
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
Segurança de Sistemas Computacionais (IC-UFAL), Lista 8, questões 1 e 2; Lista 9, questão 2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Simétrica:** a **mesma chave** cifra e decifra (AES, 3DES). É rápida, mas exige distribuir a chave por um canal seguro, e com $n$ pessoas são $n(n-1)/2$ chaves.

**Assimétrica:** **par de chaves**. A pública cifra (ou verifica a assinatura) e a privada decifra (ou assina). Exemplos: RSA e curvas elípticas. Resolve a distribuição de chaves, mas é lenta. Na prática, a assimétrica troca uma chave de sessão e a simétrica cifra os dados.

**RSA, passo a passo** (com primos pequenos, só para estudar):
1. escolha os primos $p$ e $q$ e calcule $n = pq$ e $\varphi(n) = (p-1)(q-1)$;
2. escolha $e$ com $\mathrm{mdc}(e, \varphi(n)) = 1$;
3. calcule $d$ com $e\,d \equiv 1 \pmod{\varphi(n)}$, o inverso modular;
4. para cifrar, $c = m^e \bmod n$; para decifrar, $m = c^d \bmod n$. Cada mensagem $m$ precisa ser menor que $n$.

**Exemplo parecido** (as listas pedem outras palavras). Use $p = 5$ e $q = 11$:
- então $n = 55$ e $\varphi = 40$;
- com $e = 3$, temos $d = 27$, pois $3 \cdot 27 = 81 = 2 \cdot 40 + 1$;
- a palavra "cafe" com $a = 1, \dots, z = 26$ vira $m = 3, 1, 6, 5$;
- cifrado: $3^3 = 27$, $1^3 = 1$, $6^3 = 216 \equiv 51$, $5^3 = 125 \equiv 15 \pmod{55}$;
- decifrar com $d = 27$ devolve $3, 1, 6, 5$.

**Cuidados:**
- com $p = 3$ e $q = 11$ (Lista 9), $n = 33$, e as letras até z ($26 < 33$) cabem;
- confira sempre que $m < n$;
- RSA de verdade usa primos com centenas de dígitos e *padding* (OAEP). Cifrar letra por letra é inseguro, porque vira uma cifra de substituição.

**Verificação:** `test_rsa_exemplo` refaz o exemplo com `pow(e, -1, phi)` e `pow(m, e, n)`, confere $d$, o texto cifrado e a decifração, e checa que $e\,d \bmod \varphi = 1$.
