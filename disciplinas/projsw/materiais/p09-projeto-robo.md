---
id: projsw-projeto-oo-robo-sala-substantivos-verbos
titulo: Exemplo de design OO do robô — substantivos viram classes e atributos, verbos viram métodos, Robo tem Sala, Robo é Comparable pela energia, robô de segurança e de diversão herdam de Robo
assunto: projsw-05-regras-de-projeto
tipo: notas
questao: especificação do robô (exemplo de design)
resolucao: sim
fonte: Notas de aula de Programação II (UFCG), seção "Regras básicas de projeto OO (I)"
curso: Ciência da Computação (UFAL), pasta da turma de Programação 2 / Projeto de Software (COMP372); notas de aula da UFCG usadas pela turma
fontes_catalogo: ufcg-notas-programacao2
autoria: Notas de aula dos Profs. Jacques Sauvé, Raquel Lopes e Dalton Serey (DSC-UFCG); resolução e código da equipe TutorON
licenca: Copyright da UFCG nos exemplos; paráfrase, PDF não versionado
publicacao_transcricao: não autorizada; o bloco traz paráfrase e código próprio
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Notas de aula de Programação II da UFCG, seção "Regras básicas de projeto OO (I)" (paráfrase; código da equipe TutorON). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Enunciado (paráfrase):** um robô anda numa sala (matriz) em 4 direções, um passo por vez, perdendo 1 de energia por passo; começa em (0,0); só vai a posições livres; pode mudar de sala (volta a (0,0)); há robôs de segurança (soam alarme) e de diversão (respondem a voz); robôs se comparam pela energia; o robô informa passos e energia.

**Projetar = decidir** quais classes, quais responsabilidades (métodos), quais dados (atributos) e quais relacionamentos.
- **Substantivos:** robô, sala, posição, passos, energia → classes `Robo` e `Sala`; atributos `linha`, `coluna`, `passos`, `energia`.
- **Verbos:** movimentar, mudar de sala, ocupar posição, informar → `mover(direcao)`, `mudarDeSala(sala)`, `getPassos()`, `getEnergia()`.
- **Relacionamentos:** Robo **tem** Sala (composição); Robo se **comporta como** comparável (`implements Comparable<Robo>`); RoboSeguranca e RoboDiversao **são** Robos (herança, com `acaoEspecial()` abstrato).

Quem sabe se uma posição está livre? A `Sala` (especialista da informação): `sala.livre(l, c)`. O robô não deve ler a matriz da sala diretamente.

Depois do design: escrever testes de unidade para cada responsabilidade (mover para fora da sala falha; com energia 0 não anda) e documentar.

**Verificação:** `test_projeto_robo` roda o esboço em `tests_acervo/projsw_java/robo`: subir a partir de (0,0) falha, direita e descer andam, sem energia não anda, passos e energia são contados e a comparação usa a energia.
