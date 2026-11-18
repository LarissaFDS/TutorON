---
curadoria: aprovado
natureza: material_da_disciplina
resolucao: sim
licenca: Não declarada (anotações manuscritas de aluno, 2025.2); PDFs e imagens fora do repositório
publicacao_transcricao: não se aplica: os enunciados são parafraseados e só os dados foram mantidos
revisao_humana: pendente
fontes_catalogo: ufal-oac-anotacoes-otavio-2025-2
id: oac-otavio-ab2-q2-q7
titulo: Revisão AB2 (aluno, 2025.2) — Q2 a Q7: write-through × write-back, associatividade, AMAT, memória virtual de 40 bits e CPI com L2
assunto: oac-15-hierarquia-memoria
tipo: lista
fonte: Anotações manuscritas "Revisão AB2" (7 páginas), turma 2025.2, questões 2 a 7
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de OAC 2025.2, Prof. Erick de Andrade Barboza); revisão da equipe TutorON
status_resolucao: corrigida
---
Resolução de um aluno, não gabarito do professor. Status da resolução: corrigida (Q5 e Q7b; ver "Correções").

Q2: write-back reduz escritas na memória (mais rápido) e tem lógica mais complexa; write-through mantém a memória atualizada, é mais simples e gera mais tráfego.
Q3: mais associatividade reduz faltas de conflito, mas exige mais comparadores e aumenta custo e hit time.
Q4: AMAT = hit time + miss rate × miss penalty. Menos penalidade: cache multinível; menos faltas: mais associatividade; menor hit time: cache menor e menos associativa.
Q6: CPI base 2, I-cache 2%, D-cache 4%, 36% de loads e stores, penalidade 100 ciclos: CPI = 2 + 0,02 × 100 + 0,36 × 0,04 × 100 = 2 + 2 + 1,44 = 5,44 (correto).
Q7: CPI base 1, 4 GHz (0,25 ns), memória 100 ns = 400 ciclos, I-miss 2%. a) CPI = 1 + 0,02 × 400 = 9 (correto).

Correções da equipe:
- Q5a (endereço virtual de 40 bits, físico de 36, página de 16 KiB): as anotações dividem o virtual em 4 + 36 bits. O certo: offset = log2(16 Ki) = 14 bits; número da página virtual = 40 − 14 = 26 bits; número da página física = 36 − 14 = 22 bits. A tabela tem 2^26 entradas, não 16; com PTE de 4 bytes (22 bits + validade, dirty e proteção cabem em 32), são 2^26 × 4 B = 256 MiB. O tamanho da PTE depende do enunciado; confira.
- Q7b (L2 de 5 ns = 20 ciclos, taxa global 0,5%): toda falta da L1 paga a L2, não só 1,5%. CPI = 1 + 0,02 × 20 + 0,005 × 400 = 3,4 (não 3,3); ganho 9 / 3,4 ≈ 2,6 (não 2,73).
