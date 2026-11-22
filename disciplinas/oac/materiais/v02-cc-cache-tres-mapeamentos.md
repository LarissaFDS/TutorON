---
id: oac-cc-cache-tres-mapeamentos
titulo: Cache de 4 blocos com os endereços 0, 8, 0, 6, 8, 4, 8, 10, 6: faltas no mapeamento direto, associativo de 2 vias e totalmente associativo (LRU)
assunto: oac-15-hierarquia-memoria
tipo: prova
fonte: Provas de OAC do Prof. Erick de Andrade Barboza (IC-UFAL, cursos de Engenharia e Ciência da Computação) | Prova 2 de 2017.2 (Q3)
curso: Ciência da Computação (UFAL), prova comum às turmas de Engenharia e Ciência da Computação, 2017.2
autoria: Enunciados: provas do Prof. Erick de Andrade Barboza, parafraseadas pela equipe TutorON; resolução da equipe TutorON com auxílio de IA, conferida com o gabarito do professor e por simulação
licenca: Não declarada (prova com gabarito); os PDFs não estão no repositório
publicacao_transcricao: não se aplica: o enunciado é parafraseado e só os dados foram mantidos
fontes_catalogo: ufal-cc-oac-provas-erick-2017
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Questão da prova 2 de 2017.2 (enunciado parafraseado). Status da resolução: validada (resolução da equipe TutorON, conferida com o gabarito do professor e em Python; a prova é de 2017 e usa MIPS, não RISC-V).

Cache de 4 blocos de 1 palavra, vazia no início, LRU. Endereços: 0, 8, 0, 6, 8, 4, 8, 10, 6. Com bloco de 1 palavra, o endereço já é o número do bloco.

**Mapeamento direto** (bloco = endereço mod 4): 0, 8 e 4 disputam o bloco 0; 6 e 10, o bloco 2. Cada acesso tira o anterior: **9 faltas**, nenhum acerto. Estado final: bloco 0 com 8, bloco 2 com 6.

**Associativo por conjunto de 2 vias** (2 conjuntos, conjunto = endereço mod 2): todos os endereços são pares e caem no conjunto 0, que só tem duas vias. Acertos só no segundo 0 e no terceiro 8: **7 faltas**. Estado final do conjunto 0: 10 e 6.

**Totalmente associativo** (4 vias): acertos no segundo 0, no segundo e no terceiro 8 e no último 6; o 10 tira o 0, que é o menos usado recentemente. **5 faltas**. Estado final: 6, 8, 4 e 10.

Conclusão da prova: aqui, mais associatividade diminui a taxa de faltas (9/9, 7/9, 5/9), porque os conflitos somem. As 5 faltas que sobram são compulsórias (primeiro acesso de cada um dos 5 endereços distintos).

**Verificação:** o mesmo simulador de cache LRU usado nos testes de OAC confirma 9, 7 e 5 faltas e os estados finais.
