---
id: sd_dist-utility-computing-cobranca-por-uso-servico-de-ordenacao
titulo: Utility computing: como cobrar por um serviço de ordenação de um array de n posições, considerando tamanho de n e algoritmo (pseudo-algoritmo de tarifação)
assunto: sd_dist-01-caracterizacao-e-modelos
tipo: prova
questao: AB1 2020.1 Q5
resolucao: sim
fonte: Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Sistemas Distribuídos (CCOM044); provas de 2020.1
fontes_catalogo: ufal-leandro-provas-sd
autoria: Questões do Prof. Leandro Melo de Sales (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (UFAL), AB1 2020.1 Q5 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Utility computing:** recursos de computação vendidos **como energia ou água**: o cliente (em geral outro software) **paga pelo que consome**, medido pelo provedor. É a base da cobrança na nuvem (por segundo de CPU, por GB, por requisição).

**Como montar a tarifa do serviço de ordenação (a questão aceita critérios próprios, desde que justificados):**
1. **medir o trabalho**, não só o tempo de relógio, que depende da carga do servidor. Para comparações, o custo cresce como $n \log_2 n$ (n vezes o logaritmo de n) no merge sort ou heapsort; para *counting sort* de inteiros num intervalo $k$, como $n + k$;
2. cobrar uma **taxa fixa** por chamada (custo de rede, autenticação e *marshalling*) mais um valor **por unidade de trabalho** e por **memória** usada ($O(n)$ elementos de tamanho conhecido);
3. permitir **níveis de serviço**: ordenação **estável** ou prioridade com preço maior;
4. registrar cada chamada (cliente, $n$, algoritmo, tempo, bytes) para auditoria e fatura.

Pseudo-algoritmo:
```text
funcao tarifa(n, algoritmo, bytes_por_item):
    se algoritmo == "counting": trabalho = n + k
    senao: trabalho = n * log2(max(n, 2))
    memoria_mb = n * bytes_por_item / 2^20
    retorna FIXA + PRECO_TRABALHO * trabalho + PRECO_MB * memoria_mb
```
Com $n = 1024$: $n \log_2 n = 1024 \cdot 10 = 10\,240$ unidades; dobrando $n$ para 2048, o trabalho vai a $2048 \cdot 11 = 22\,528$, um pouco mais que o dobro.

Discussão esperada: tarifar por **trabalho estimado** é previsível para o cliente; por **tempo medido** é mais justo para o provedor, mas varia com a carga. Uma combinação comum é estimar e ajustar pelo medido.

**Verificação:** `test_tarifa_por_uso` implementa a tarifa, confere 10 240 e 22 528 unidades, que a tarifa cresce com $n$ e conta as comparações reais de um merge sort em listas aleatórias, que ficam abaixo de $n \log_2 n$.
