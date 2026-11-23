---
id: seguranca-autenticacao-nonce-reproducao-ap-homem-do-meio-kdc-kerberos-centro-de-distribuicao-de-chaves
titulo: Autenticação do ponto final: finalidade do nonce contra ataque de reprodução, protocolos ap1.0 a ap5.0, ataque do homem do meio, centro de distribuição de chaves (KDC) e Kerberos
assunto: seg-03-criptografia-e-autenticacao
tipo: lista
questao: Lista 9, questões 1, 3 e 5; Lista 11, questão 1; Lista 8, questão 4
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
Segurança de Sistemas Computacionais (IC-UFAL), Lista 9, questões 1, 3 e 5; Lista 11, questão 1; Lista 8, questão 4 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Nonce:** número usado **uma única vez**. Na autenticação, o verificador envia um nonce novo $R$, e o outro lado prova a identidade devolvendo $R$ cifrado ou com MAC, usando a chave. Uma resposta antiga, gravada e **reproduzida** por um intruso, não serve, porque o nonce mudou. Essa é a finalidade: **evitar ataque de reprodução** (*replay*) e garantir que o outro lado está **vivo agora**.

**Sequência didática ap1.0–ap5.0** (Kurose e Ross):
- ap1.0: "sou Alice" (qualquer um diz);
- ap2.0: mais o endereço IP (falsificável);
- ap3.0: mais a senha (gravável);
- ap3.1: senha cifrada (reproduzível);
- **ap4.0:** nonce com chave simétrica;
- **ap5.0:** nonce com chave pública, em que Alice cifra $R$ com a privada e Bob confere com a pública dela.

**Homem do meio no ap5.0:** se Bob obtém a chave pública "de Alice" **pelo próprio canal** que Trudy controla, Trudy entrega a chave dela e responde aos dois lados. O nonce não resolve, porque o problema é **confiar na chave pública**. A solução é o **certificado** assinado por uma AC. Na Lista 9, questão 3, pense na autenticação dos dois lados **e** na origem das chaves.

**KDC (centro de distribuição de chaves):** servidor confiável que compartilha uma chave secreta com cada usuário. Para Alice falar com Bob, o KDC gera uma **chave de sessão** $K_{AB}$ e a envia cifrada para Alice, junto com um "bilhete" para Bob cifrado com a chave de Bob. Com $n$ usuários, bastam $n$ chaves com o KDC, em vez de $n(n-1)/2$. O **Kerberos** usa essa ideia com bilhetes que expiram e um servidor de bilhetes.

**Verificação:** `test_desafio_resposta_com_nonce` simula desafio e resposta com HMAC: a resposta certa passa, uma resposta gravada de um nonce antigo é recusada e cada nonce só é aceito uma vez; `test_numero_de_chaves_kdc` compara $n(n-1)/2$ com $n$.
