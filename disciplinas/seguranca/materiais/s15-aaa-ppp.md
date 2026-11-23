---
id: seguranca-autenticacao-ppp-pap-chap-aaa-radius-tacacs-controle-de-acesso-dac-mac-rbac
titulo: Protocolos de autenticação do PPP (PAP e CHAP), arquitetura AAA (autenticação, autorização e contabilização), RADIUS e TACACS+, controles de acesso DAC, MAC e RBAC
assunto: seg-03-criptografia-e-autenticacao
tipo: lista
questao: AB2, questão 4 (PPP); Lista 10, questões 1, 2, 4 e 5
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
Segurança de Sistemas Computacionais (IC-UFAL), AB2, questão 4 (PPP); Lista 10, questões 1, 2, 4 e 5 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**PPP** (RFC 1661): protocolo de enlace ponto a ponto. A autenticação acontece depois do estabelecimento do enlace (LCP).

**PAP:**
- o cliente envia usuário e **senha em texto aberto**, em duas vias;
- o servidor confere;
- não há proteção contra captura nem contra reprodução.

**CHAP** (RFC 1994):
- o servidor envia um **desafio** aleatório;
- o cliente responde com $\text{MD5}(\text{id} \,\|\, \text{segredo} \,\|\, \text{desafio})$, em três vias;
- o servidor calcula o mesmo valor e compara;
- a senha **nunca trafega**, e o desafio muda a cada vez (contra reprodução);
- pode se repetir durante a sessão.

**AAA:**
- **autenticação**: quem é;
- **autorização**: o que pode fazer;
- **contabilização** (*accounting*): o que fez, quanto tempo.

Um protocolo AAA centraliza essas funções num servidor, em vez de cada equipamento guardar as próprias senhas. Essa é a diferença para um protocolo só de autenticação, como o PAP ou o CHAP local.

**RADIUS e TACACS+:**
- **RADIUS:** usa UDP, cifra só a senha e junta autenticação e autorização;
- **TACACS+** (Cisco): usa **TCP 49**, cifra **o pacote inteiro** e **separa** as três funções AAA. Permite autorizar comando a comando, o que é útil na administração de roteadores.

**Controle de acesso:**
- **DAC (discricionário):** o **dono** do recurso decide quem acessa. Exemplo: permissões de arquivo do Unix;
- **MAC (obrigatório):** o **sistema** impõe rótulos de sigilo e autorização. O usuário não muda. Exemplo: "não ler acima do próprio nível";
- **RBAC (por papéis):** permissões dadas a **papéis** (professor, aluno), e usuários recebem papéis.

**Verificação:** `test_chap_md5` calcula a resposta do CHAP com `hashlib.md5(id + segredo + desafio)`, confere que o servidor valida e que outro desafio dá outra resposta; `test_rbac_por_papel` checa permissões por papel.
