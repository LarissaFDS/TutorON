---
id: projsw-refatoramento-extract-move-method
titulo: Refatoramento — mau cheiro, Extract Method (método longo com comentário), Move Method e Move Field (cobrança de cheque descoberto vai para TipoDeConta), sempre apoiado em testes
assunto: projsw-06-refatoramento
tipo: notas
questao: exemplos de Extract Method, Move Method e Move Field
resolucao: sim
fonte: Notas de aula de Programação II (UFCG), seção "Refatoramento de Software"
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
Notas de aula de Programação II da UFCG, seção "Refatoramento de Software" (paráfrase; código da equipe TutorON). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Refatorar** é mudar a estrutura do código **sem mudar o que ele faz**, para corrigir "maus cheiros" (método longo, classe que só guarda dados, código duplicado, método que usa mais dados de outra classe do que da sua). Sempre com **testes de unidade** rodando antes e depois.

**Extract Method:** quando sentir vontade de comentar um trecho ("imprime detalhes"), transforme-o num método com nome que diga isso: `imprimeDetalhes(getValorDivida())`. Métodos curtos são mais fáceis de entender e reusar.

**Move Method:** `Conta.cobrancaDeChequeDescoberto()` decide pela regra do tipo de conta (premium: 10 mais 0,85 por dia acima de 7; comum: 1,75 por dia). Quem tem essa informação é `TipoDeConta` (especialista da informação):
```java
class ContaDepois {
    double cobrancaDeChequeDescoberto() {
        return tipo.cobrancaDeChequeDescoberto(diasDescobertos);
    }
}
```
**Move Field:** a taxa de juros também passa para `TipoDeConta`, e `Conta` usa `tipo.getTaxaDeJuros()`.

**Como saber que não mudou nada?** Rode o mesmo conjunto de casos antes e depois. Por exemplo, premium com 10 dias: $10 + 3 \times 0{,}85 = 12{,}55$; comum com 10 dias: $10 \times 1{,}75 = 17{,}5$.

Catálogo de referência: Fowler, *Refactoring* (livro protegido, só referência por seção).

**Verificação:** `test_refatoramento` roda `tests_acervo/projsw_java/refatoramento`: antes e depois do Move Method dão o mesmo valor nos 62 casos (2 tipos × 0 a 30 dias), com 12,55 e 17,5 nos exemplos.
