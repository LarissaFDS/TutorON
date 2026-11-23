---
id: compevol-estrategias-evolutivas-1-mais-1-regra-do-um-quinto-mu-lambda
titulo: Estratégias evolutivas: (1+1)-ES, regra do 1/5 de Rechenberg, (μ+λ) × (μ,λ), autoadaptação do desvio; diferenças para algoritmos genéticos
assunto: compevol-03-outras-metaheuristicas
tipo: exercicio_resolvido
questao: Dianati, Song e Treiber, seções II-III
resolucao: sim
fonte: Apostilas e textos da pasta da turma (Lucas, UFRGS 2002; Lacerda e Carvalho; Dianati, Song e Treiber)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Computação Evolucionária (COMP397); turma 2021.1
fontes_catalogo: dianati-gaes
autoria: Exercício clássico dos textos da pasta da turma; resolução da equipe TutorON
licenca: Textos sem licença aberta declarada; paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Computação Evolucionária (UFAL, turma 2021.1), Dianati, Song e Treiber, seções II-III (enunciado parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Estratégias evolutivas (EE, em inglês ES):** criadas em Berlim (Rechenberg, Schwefel, 1964) para **otimização de parâmetros reais**. O indivíduo é um vetor real; o operador principal é a **mutação gaussiana**:
$$x' = x + \sigma\, N(0, I)$$

**(1+1)-ES:** um pai gera um filho por mutação; o melhor dos dois sobrevive. É uma subida de encosta estocástica.

**Regra do 1/5** (Rechenberg): a razão entre mutações bem-sucedidas (filho melhor que o pai) e o total deve ficar perto de **1/5**. Se for **maior**, os passos estão pequenos demais: **aumente** $\sigma$; se for **menor**, **diminua** (ex.: multiplicar ou dividir $\sigma$ por $0{,}82$ a cada $k$ gerações).

**(μ+λ)-ES:** $\mu$ pais geram $\lambda$ filhos; os $\mu$ melhores entre **pais e filhos** sobrevivem (elitista). **(μ,λ)-ES:** os $\mu$ melhores só entre os **filhos** ($\lambda > \mu$): esquece soluções antigas, ajuda a sair de ótimos locais e a autoadaptar $\sigma$.

**Autoadaptação:** o próprio $\sigma$ vai no cromossomo e também sofre mutação, $\sigma' = \sigma\, e^{\tau N(0,1)}$; bons $\sigma$ sobrevivem junto com boas soluções.

**EE × AG:**

| | AG | EE |
|---|---|---|
| representação | binária (clássica) | real |
| operador principal | cruzamento | mutação gaussiana |
| seleção | probabilística dos pais | determinística dos sobreviventes |
| parâmetros | fixos | autoadaptativos |

**Exemplo:** uma (1+5)-ES maximizando $F(x, y) = -x^2 - y^2 + 4$ sobe até o máximo $4$ em $(0, 0)$.

**Verificação:** `test_estrategia_evolutiva` roda a (1+1)-ES com a regra do 1/5 na esfera e a (1+5)-ES no exemplo com semente fixa, e confere que chegam a menos de $10^{-3}$ do ótimo e que $\sigma$ diminui perto dele.
