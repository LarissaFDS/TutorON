---
id: seguranca-requisitos-basicos-confidencialidade-integridade-disponibilidade-autenticidade-nao-repudio
titulo: Requisitos básicos de segurança da informação: confidencialidade, integridade, disponibilidade (tríade CID), autenticidade e não repúdio; ameaças, vulnerabilidades e riscos; redundância para tolerância a falhas
assunto: seg-01-fundamentos-e-politica
tipo: prova
questao: AB1 2020.1 e 2020.2, Reposição AB1 e Final, questão 1; AB2, questões 5 e 6; Lista 1, questões 1, 2 e 4
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
Segurança de Sistemas Computacionais (IC-UFAL), AB1 2020.1 e 2020.2, Reposição AB1 e Final, questão 1; AB2, questões 5 e 6; Lista 1, questões 1, 2 e 4 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Requisitos básicos** (cada um com o mecanismo que o atende):
- **Confidencialidade:** só quem tem autorização lê a informação. Mecanismos: criptografia, controle de acesso.
- **Integridade:** a informação não é alterada sem autorização, ou a alteração é detectada. Mecanismos: hash, MAC, assinatura digital.
- **Disponibilidade:** a informação e o sistema estão acessíveis quando precisa. Mecanismos: redundância, *backup*, proteção contra negação de serviço.
- **Autenticidade:** a origem é quem diz ser. Mecanismos: senhas, certificados, MAC.
- **Não repúdio:** o autor não pode negar a autoria depois. Mecanismo: **assinatura digital com chave privada** (só o dono tem a chave).

Na questão de múltipla escolha da AB2, os atributos principais são **Confidencialidade, Integridade e Disponibilidade**. As outras opções trocam um deles por persistência, consistência, durabilidade ou confiabilidade. A definição "não poderá negar a autoria, pois só aquela chave privada geraria a assinatura" é **não repúdio**.

**Termos vizinhos:**
- **ameaça:** causa potencial de um incidente (pessoa, programa, desastre);
- **vulnerabilidade:** fraqueza que a ameaça explora;
- **risco:** probabilidade × impacto.

**Redundância para tolerância a falhas** (disponibilidade):
- RAID (espelhamento ou paridade);
- fontes e enlaces duplicados;
- *cluster* com *failover*;
- *backup* fora do local.

No RAID 5, o bloco de paridade é o XOR dos blocos de dados. Se um disco falha, o XOR dos que restam reconstrói o bloco perdido.

**Verificação:** `test_paridade_raid5` reconstrói um bloco perdido pelo XOR dos outros e `test_hash_detecta_alteracao` mostra que mudar um byte muda o SHA-256 (integridade).
