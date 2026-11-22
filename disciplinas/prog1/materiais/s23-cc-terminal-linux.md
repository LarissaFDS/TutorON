---
id: prog1-cc-terminal-linux
titulo: Dicas de terminal Linux da turma de Ciência da Computação — pwd, ls, cd, mkdir, mv, rm, nano e compilar com gcc
assunto: prog1-02-compilacao
tipo: material_estudo
resolucao: sim
curso: Ciência da Computação (UFAL), Programação 1; turma não identificada; arquivo de 06/12/2018
fonte: "Iniciando no Terminal Linux" (dicas-terminal), material de Programação 1 da turma de Ciência da Computação (UFAL), 3 páginas
fontes_catalogo: ufal-cc-dicas-terminal
autoria: Autoria não identificada no arquivo; parafraseado pela equipe TutorON com auxílio de IA
licenca: Não declarada; o original não está no repositório
publicacao_transcricao: não se aplica: o bloco parafraseia com texto próprio
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: corrigida
revisao_humana: pendente
---
O Linux diferencia maiúsculas de minúsculas: `Prog.c` e `prog.c` são arquivos diferentes.

```bash
pwd                         # em que diretório estou
ls -l                       # lista o conteúdo, com detalhes
cd Downloads                # entra num diretório; cd .. volta um nível; cd ~ vai para a home
mkdir Nova\ Pasta           # a barra antes do espaço; ou use aspas: "Nova Pasta"
mv nome.txt novoNome.txt    # renomeia; mv nome.txt ../ move para o diretório pai
rm nome.txt                 # apaga o arquivo, sem lixeira
rm -r Pasta                 # apaga o diretório e tudo dentro
nano lista1.c               # cria ou edita o arquivo no terminal
gcc -std=c99 -Wall -Wextra lista1.c -o lista1
./lista1 < entrada.txt      # roda lendo a entrada de um arquivo
```

Sem `-o`, o gcc gera o executável `a.out`, que roda com `./a.out`. O `./` diz que o programa está no diretório atual. Para testar um exercício de juiz online, salve o exemplo de entrada em `entrada.txt` e compare a sua saída com a esperada. Status da resolução: corrigida (correção da equipe TutorON, não é gabarito do professor).

Correções da equipe
- Divergência: o material diz que não existe comando para renomear. O jeito comum é `mv`, mas várias distribuições também têm `rename`, que serve para muitos arquivos de uma vez.
- O material manda usar `rm -Rf` para apagar diretório. Basta `rm -r`. O `-f` apaga sem perguntar e sem avisar de erro, e não há lixeira: cuidado com o caminho.
- Para usar o terminal do Linux no Windows, o material aponta um blog de 2017. Hoje o caminho oficial é o WSL, da Microsoft.
