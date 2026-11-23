---
id: ia-sistemas-especialistas-base-de-conhecimento-maquina-de-inferencia-engenheiro-do-conhecimento-explicacao-mycin
titulo: Sistemas especialistas: arquitetura (base de conhecimento, memória de trabalho, máquina de inferência, interface e explicação), papéis (especialista, engenheiro do conhecimento), vantagens e limites
assunto: ia-03-conhecimento-e-raciocinio
tipo: material_estudo
questao: slide 04 (Sistemas Especialistas)
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
Inteligência Artificial (IC-UFAL, 2020.2), slide 04 (Sistemas Especialistas) (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Sistema especialista (SE):** usa conhecimento específico de um domínio estreito para resolver problemas com desempenho próximo ao de um especialista humano. O conhecimento é teórico e prático (heurísticas, atalhos).

**Arquitetura:**
- **base de conhecimento:** regras se-então e fatos gerais do domínio;
- **memória de trabalho:** fatos do caso atual;
- **máquina de inferência:** aplica as regras (encadeamento para frente ou para trás) e resolve conflitos quando várias disparam;
- **interface com o usuário;**
- **subsistema de explicação:** responde "por quê?" (por que fez a pergunta) e "como?" (como chegou à conclusão), mostrando as regras usadas.

Separar a base de conhecimento da máquina de inferência permite trocar o conhecimento sem reescrever o programa (a "casca", ou shell).

**Papéis:** o **especialista do domínio** fornece o conhecimento; o **engenheiro do conhecimento** o extrai e codifica; o usuário final consulta. A **aquisição de conhecimento** é o gargalo.

**Características:** raciocínio heurístico, tolerância a dados incompletos (fatores de certeza, como no MYCIN), capacidade de explicar.

**Limites:** conhecimento raso e frágil fora do domínio, difícil de manter quando cresce, não aprende sozinho.

**Exemplos clássicos:** MYCIN (infecções bacterianas, para trás), DENDRAL (estruturas químicas), XCON/R1 (configuração de computadores, para frente).

**Verificação:** `test_explicacao_como` roda um SE mínimo que guarda as regras disparadas e confere que a explicação "como?" lista a cadeia de regras até a conclusão.
