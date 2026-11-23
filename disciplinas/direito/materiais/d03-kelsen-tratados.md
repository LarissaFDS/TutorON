---
id: direito-piramide-de-kelsen-hierarquia-das-normas-constituicao-tratados-de-direitos-humanos-supralegal
titulo: Pirâmide de Kelsen e hierarquia das normas (Constituição no topo); tratados de direitos humanos com e sem o rito do art. 5º, §3º da Constituição (equivalência a emenda, status supralegal); norma jurídica e sanção
assunto: dir-02-constituicao-e-direitos-humanos
tipo: prova
questao: Avaliação de 2020.2, questões sobre Kelsen, tratados e norma
resolucao: sim
fonte: Avaliações de Noções de Direito da Profa. Jessica Hind (IC-UFAL), 2020.2 (setembro e outubro de 2021), e slides "Noções Iniciais" da disciplina
curso: Ciência da Computação (UFAL), COMP387 Noções de Direito (7º período); turma 2020.2 (aulas em 2021)
fontes_catalogo: ufal-direito-avaliacoes,constituicao-planalto
autoria: Questões da Profa. Jessica Hind (IC-UFAL); explicação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Noções de Direito (IC-UFAL, 2020.2), Avaliação de 2020.2, questões sobre Kelsen, tratados e norma (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

Conteúdo de estudo, não é aconselhamento jurídico.

**Kelsen** (*Teoria Pura do Direito*) vê o ordenamento como um **escalonamento**: cada norma tira a validade de uma norma superior. A imagem usual é uma **pirâmide**:
- no **topo**, a **Constituição**;
- abaixo, as leis (complementares, ordinárias e equivalentes);
- depois, decretos e regulamentos;
- na base, os atos de menor nível, como contratos e sentenças.

Uma norma inferior que contraria a superior é inválida. Daí o controle de constitucionalidade.

**Tratados de direitos humanos no Brasil:**
- **com o rito qualificado** (Constituição, art. 5º, §3º): aprovação em cada Casa do Congresso, em **dois turnos**, por **três quintos** dos votos dos membros. O tratado **equivale a emenda constitucional**. Três quintos são 308 dos 513 deputados e 49 dos 81 senadores;
- **sem o rito qualificado:** o STF entendeu, no julgamento sobre a prisão do depositário infiel (2008), que esses tratados têm hierarquia **supralegal**: acima das leis e abaixo da Constituição. Parte da doutrina defende que, pelo **conteúdo** (natureza *material*), eles são **constitucionais**.

A avaliação perguntava pela natureza **material**, e a resposta esperada era **constitucional**. Diga as duas posições: a material, da doutrina, e a formal ou hierárquica, do STF.

**Norma e sanção:** o procedimento de criação muda com a espécie normativa (lei ordinária, complementar, emenda). Sobre "toda norma tem sanção", há divergência: para Kelsen, a sanção é central na norma jurídica. Outros lembram normas sem sanção direta, como as que definem competências ou conceitos.

**Verificação:** `test_tres_quintos` calcula três quintos de 513 e de 81 (308 e 49) e `test_hierarquia_kelsen` confere a ordem da pirâmide; as citações do art. 5º foram conferidas no texto do Planalto.
