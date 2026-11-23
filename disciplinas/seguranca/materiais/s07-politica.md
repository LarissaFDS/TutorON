---
id: seguranca-politica-de-seguranca-da-informacao-classificacao-controles-fisicos-logicos
titulo: Política de Segurança da Informação (PSI): definição, ameaças tratadas, classificação das informações (pública, interna, confidencial, secreta), controles físicos, lógicos e administrativos, bloqueio de tela, certo ou errado
assunto: seg-01-fundamentos-e-politica
tipo: prova
questao: Reposição AB1, questão 3; AB1 2020.1, questão 6; Lista 3; projeto de PSI (AB1 2020.2)
resolucao: sim
fonte: Provas (2020.1 e 2020.2) e listas semanais de Segurança de Sistemas Computacionais do IC-UFAL
curso: Ciência da Computação (UFAL), COMP403 Segurança de Sistemas Computacionais (ênfase Sistemas de Informação); provas de 2020.1 e 2020.2 (algumas com cabeçalho de Engenharia da Computação)
fontes_catalogo: ufal-seguranca-provas-listas
autoria: Questões das provas e listas da disciplina (IC-UFAL; professor não identificado nos PDFs); explicação da equipe TutorON
licenca: Não declarada (provas e listas); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Segurança de Sistemas Computacionais (IC-UFAL), Reposição AB1, questão 3; AB1 2020.1, questão 6; Lista 3; projeto de PSI (AB1 2020.2) (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**PSI:** documento aprovado pela direção que define princípios, responsabilidades e regras para proteger a informação da organização. Orienta normas e procedimentos mais detalhados. É divulgada e revisada.

**Ameaças que a PSI trata:**
- acesso não autorizado;
- *malware*;
- engenharia social;
- vazamento;
- falhas de equipamento e desastres;
- erro humano;
- fraude interna.

**Classificação da informação** pela importância para o negócio:
- **pública**;
- **interna** (uso interno);
- **confidencial** (restrita a grupos);
- **secreta** (altamente restrita).

Cada nível tem regras de rotulagem, armazenamento, transmissão e descarte.

**Tipos de controle:**
- **físicos:** portas com crachá, câmeras, salas de servidores, *no-break*, proteção contra incêndio;
- **lógicos ou técnicos:** senhas, controle de acesso, criptografia, *firewall*, antivírus, IDS, registro (*log*);
- **administrativos:** a própria política, treinamento, termo de responsabilidade, classificação, plano de continuidade.

**Certo ou errado da AB1 2020.1:**
- "a política deve nortear os parâmetros de configuração de *firewall*, antivírus e IDS": **certo**;
- "segurança física das pessoas e instalações está fora do escopo da política": **errado**, porque a segurança física faz parte da política.

**Lista 3, acesso não autorizado à estação de trabalho:** a medida que reduz o problema é **senha com bloqueio automático de tela** (opção a). As outras opções tratam de *malware* ou de dados.

**Projeto de PSI:** ao montar a política de uma empresa fictícia, organize por escopo, papéis, classificação, controles por área e sanções. O trabalho avaliado é da equipe: o TutorON ajuda a estruturar, não escreve a política.

**Verificação:** `test_controle_por_classificacao` confere uma tabela pequena de níveis: quem tem autorização "interna" lê pública e interna, mas não confidencial.
