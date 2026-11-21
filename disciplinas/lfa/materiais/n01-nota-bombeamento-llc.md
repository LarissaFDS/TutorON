---
id: lfa-nota-bombeamento-livres-de-contexto
titulo: Nota da equipe — lema do bombeamento para linguagens livres de contexto e prova de que aⁿbⁿcⁿ não é livre de contexto
assunto: lfa-05-livres-de-contexto
tipo: nota
resolucao: nao
fonte: Nota da equipe TutorON escrita com apoio de IA, a partir das ideias gerais da aula 5 das notas de Sipser (MIT), sem transcrição
fontes_catalogo: lee-sipser-notas-2012,mit-ocw-18-404j
autoria: Equipe TutorON com apoio de IA; sem revisão humana
licenca: Texto próprio
publicacao_transcricao: não se aplica
curadoria: candidato
natureza: nota_da_equipe_ia
verificacao: nao_verificada
revisao_humana: pendente
---
**Lema do bombeamento para LLC:** se $L$ é livre de contexto, existe $p$ tal que toda $s \in L$ com $|s| \ge p$ se escreve $s = uvxyz$ com $|vxy| \le p$, $|vy| \ge 1$ e $uv^ixy^iz \in L$ para todo $i \ge 0$.

**$a^nb^nc^n$ não é livre de contexto:** tome $s = a^pb^pc^p$. Como $|vxy| \le p$, a janela $vxy$ toca no máximo dois tipos de símbolo vizinhos. Bombear com $i = 2$ aumenta no máximo dois dos três contadores (ou desarruma a ordem), então $uv^2xy^2z \notin L$.

**Verificação:** nota sem revisão humana; fica fora da busca até ser revisada.
