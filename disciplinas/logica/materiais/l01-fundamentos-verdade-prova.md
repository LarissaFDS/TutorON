---
id: logica-fundamentos-verdade-prova
titulo: O que é lógica: verdade, prova, sintaxe e semântica; por que importa na computação
assunto: logica-01-historico-fundamentos
tipo: material_estudo
resolucao: sim
fonte: Slides de Lógica Clássica Proposicional (Baldoino Fonseca, UFAL), parte inicial; slides de introdução e de semântica de predicados (Tiago Massoni, UFCG)
fontes_catalogo: ufal-baldoino-slides-proposicional, ufcg-massoni-slides
autoria: Profs. Evandro Costa e Baldoino Fonseca (IC-UFAL) e Prof. Tiago Massoni (UFCG), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (material do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

A lógica estuda dois conceitos: **verdade** (semântica: quando uma fórmula é verdadeira numa interpretação) e **prova** (sintaxe: sequência de fórmulas obtida aplicando regras de inferência a fórmulas iniciais). Um sistema lógico tem uma linguagem formal (fórmulas), uma semântica (valor V ou F) e regras de inferência que, aplicadas a fórmulas verdadeiras, só geram fórmulas verdadeiras.

Três dimensões de uma linguagem: **sintaxe** (como se escreve), **semântica** (o que significa) e **pragmática** (como se usa).

Por que na computação: lógica serve para especificar, testar, analisar e projetar sistemas (verificação de programas, SAT solvers, Prolog, model checking, Alloy).

Marco histórico citado nos slides da UFCG: Alonzo Church (1903–1995), orientador de Turing em Princeton, provou que a validade na lógica de primeira ordem é **indecidível**: não existe programa que sempre responda se uma fórmula de predicados é válida. Na lógica proposicional a validade é decidível (tabela-verdade com $2^n$ linhas para $n$ átomos), mas o custo cresce exponencialmente.

A ementa (PPC 2014) cita "histórico evolutivo"; os slides da turma não trazem uma linha do tempo detalhada, então outros fatos históricos são conhecimento geral, não do material.

**Verificação:** a afirmação de custo foi conferida contando linhas: 3 átomos dão $2^3=8$ linhas e 10 átomos dão 1024.
