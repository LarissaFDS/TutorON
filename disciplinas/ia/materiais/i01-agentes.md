---
id: ia-definicao-de-ia-agentes-inteligentes-sensores-atuadores-racionalidade-ambientes
titulo: O que é Inteligência Artificial; agentes inteligentes: sensores, atuadores, função do agente, racionalidade e propriedades dos ambientes
assunto: ia-01-fundamentos-e-agentes
tipo: material_estudo
questao: slides 01 e 02 (Introdução e Agentes Inteligentes)
resolucao: sim
fonte: Slides de Inteligência Artificial do Prof. Jacson R. C. Silva (Departamento de Computação, CCA-UFES), usados na turma da UFAL
curso: Ciência da Computação (UFAL), COMP380 Inteligência Artificial; turma 2020.2 (Prof. Evandro de Barros Costa)
fontes_catalogo: ufes-jeiks-slides
autoria: Slides do Prof. Jacson R. C. Silva (UFES), usados como material da turma da UFAL; explicação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Inteligência Artificial (IC-UFAL, 2020.2), slides 01 e 02 (Introdução e Agentes Inteligentes) (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**IA** é o ramo da Computação que trata da automação do comportamento inteligente. Ela se apoia em estruturas de dados para **representar conhecimento**, em **algoritmos** que aplicam esse conhecimento e em linguagens e técnicas de programação. A dificuldade da definição é que a própria inteligência não é bem definida.

**Agente:** algo que **percebe** o ambiente por **sensores** e **age** sobre ele por **atuadores**.
- humano: olhos e ouvidos; mãos, pernas e boca;
- robô: câmeras e infravermelho; motores;
- software: teclado, arquivos e pacotes de rede; tela, disco e envio de pacotes.

**Função do agente:** mapeia a sequência de percepções em uma ação. O **programa do agente** implementa essa função.

**Agente racional:** escolhe a ação que maximiza a **medida de desempenho** esperada, dada a sequência de percepções e o que sabe. Racional não é onisciente.

**Propriedades do ambiente:** totalmente ou parcialmente observável; determinístico ou estocástico; episódico ou sequencial; estático ou dinâmico; discreto ou contínuo; um ou vários agentes.

**Tipos de agente:** reativo simples (regras condição-ação), reativo com modelo (estado interno), baseado em objetivos, baseado em utilidade e agente com aprendizado.

**Exemplo:** o aspirador de pó com dois quadrados A e B percebe (local, sujo?) e age: se sujo, aspira; senão, vai para o outro quadrado.

**Verificação:** `test_aspirador_reativo` simula o agente reativo do aspirador e confere que os dois quadrados ficam limpos.
