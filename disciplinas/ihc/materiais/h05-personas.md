---
id: ihc-personas-conceito-alan-cooper-dados-reais-como-elaborar-exemplo
titulo: Personas: conceito (personagem semifictício baseado em dados reais), origem com Alan Cooper, como elaborar uma persona para a interface analisada e erros comuns
assunto: ihc-01-design-centrado-no-usuario
tipo: exercicio
questao: projeto AB2 (construir o conceito de personas e elaborar pelo menos uma persona)
resolucao: sim
fonte: Etapas do projeto de microteste de usabilidade pedidas pelo Prof. Fábio Paraguaçu (IC-UFAL), 2020.2, conhecidas pelos enunciados citados nos trabalhos entregues
curso: Ciência da Computação (UFAL), COMP395 Interação Homem-Máquina (ênfase Sistemas de Informação); turma 2020.2 (aulas em 2021)
fontes_catalogo: ufal-ihc-etapas-projeto
autoria: Etapas do projeto do Prof. Fábio Paraguaçu (IC-UFAL); explicação e exemplo parecido da equipe TutorON
licenca: Não declarada; paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Interação Humano-Computador (IC-UFAL, 2020.2), projeto AB2 (construir o conceito de personas e elaborar pelo menos uma persona) (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

O projeto é **avaliativo** e feito em grupo: aqui vão o método e um exemplo parecido, não o trabalho pronto.

**Persona:** personagem **semifictício** que representa um grupo de usuários reais. Tem nome, contexto, objetivos, frustrações e nível de experiência, e é **construído a partir de dados**: entrevistas, observação, pesquisa. O conceito foi popularizado no design de interação por **Alan Cooper**: projetar para "alguém concreto" ajuda a decidir o que entra e o que sai da interface.

Em IHC, a persona serve ao **design**: orienta tarefas, prioridades e linguagem. Em marketing há a "buyer persona", com foco em vendas. Não confunda as duas no trabalho.

**Como elaborar:**
1. reúna dados de usuários reais (entrevistas, questionário, observação do microteste);
2. agrupe padrões de comportamento e objetivos;
3. escreva a persona:
   - nome e foto ilustrativa (não de uma pessoa real identificável);
   - idade e contexto;
   - **objetivos** com a interface;
   - **frustrações**;
   - experiência com tecnologia;
   - um cenário de uso;
4. ligue cada característica a um dado observado;
5. use a persona para escolher as tarefas e avaliar soluções ("a Dona Lúcia acharia este botão?").

**Exemplo parecido** (aplicativo de ônibus): Dona Lúcia, 67 anos, aposentada, usa o celular para mensagens. **Objetivo:** saber quando o ônibus passa no ponto. **Frustrações:** letras pequenas e mapas confusos. **Experiência:** iniciante. **Cenário:** no ponto, com sol na tela, quer a resposta em um toque.

**Erros comuns:**
- persona inventada sem dados;
- persona "média" sem objetivos;
- personas demais;
- usar dados pessoais de um participante real.

**Verificação:** `test_persona_tem_campos_essenciais` confere que a persona de exemplo tem objetivos, frustrações, experiência e cenário, e que cada característica aponta para um dado de origem.
