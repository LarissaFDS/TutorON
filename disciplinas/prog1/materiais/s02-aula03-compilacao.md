---
id: prog1-aula03-compilacao
titulo: Aula 3 — primeiro programa em C, compilador e gcc
assunto: prog1-02-compilacao
tipo: material_estudo
resolucao: sim
fonte: Slides de Programação 1 (ECOM002, UFAL), Prof. Rodrigo de Barros Paes, Aula 3 (Primeiro programa; livro, capítulo 4)
fontes_catalogo: ufal-prog1-slides-paes
autoria: Slides do Prof. Rodrigo de Barros Paes (IC/UFAL), parafraseados pela equipe TutorON com auxílio de IA
licenca: Não declarada (slides do professor)
publicacao_transcricao: não se aplica: o bloco parafraseia com texto próprio e código revisado; os slides não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: corrigida
revisao_humana: pendente
---
O processador só entende linguagem de máquina (binário). O **compilador** traduz o programa da linguagem fonte (C) para a linguagem de máquina (o arquivo executável). Línguas naturais são ambíguas; uma linguagem de programação tem só instruções com um sentido e usa símbolos (+ - / ().

Por que C: dá controle da memória (ponteiros, alocação), ajuda a escrever código eficiente e mostra "o que está por baixo dos panos"; será usada em Sistemas Operacionais, Estrutura de Dados e Compiladores.

```c
#include <stdio.h>

int main(void)
{
    printf("Primeiro programa em C\n");
    return 0;
}
```

Compilar e executar no terminal:

```bash
gcc primeiro.c -o primeiro
./primeiro
```

`-o` dá o nome do executável: `gcc primeiro.c -o livro` gera outro executável, que faz a mesma coisa, porque vem do mesmo código-fonte. Mudou o código? Compile de novo antes de executar. `\n` é a quebra de linha: três `\n` no fim pulam três linhas. `return 0` em `main` indica que o programa terminou sem erro.

Para ver avisos que apontam erros comuns, compile com `gcc -std=c99 -Wall -Wextra primeiro.c -o primeiro`. Status da resolução: corrigida (correção da equipe TutorON, não é gabarito do professor).

Correções da equipe
- Divergência: o slide escreve `int main()`; aqui fica `int main(void)`, a forma do padrão C para "sem parâmetros". As duas compilam.
- O slide diz que só dá suporte em Linux; no Windows, o gcc do MinGW ou o WSL também compilam estes programas.
