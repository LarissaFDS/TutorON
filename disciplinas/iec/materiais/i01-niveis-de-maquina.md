---
id: iec-niveis-de-maquina
titulo: Máquina multinível: os seis níveis de um computador (Tanenbaum) e componentes básicos
assunto: iec-02-componentes-niveis
tipo: material_estudo
resolucao: sim
fonte: Slides do Capítulo 3 (O nível lógico digital) de Organização Estruturada de Computadores, Tanenbaum, 6ª ed., Pearson, slide 2 (Máquinas multiníveis contemporâneas); capítulo 1 do livro só como referência
fontes_catalogo: pearson-tanenbaum-slides
autoria: Slides da editora Pearson (baseados em Tanenbaum), usados na disciplina; parafraseados pela equipe TutorON com auxílio de IA
licenca: Protegido (© 2014 Pearson, todos os direitos reservados): só paráfrase e referência por seção
publicacao_transcricao: não se aplica: o bloco parafraseia com texto e exemplos próprios; os originais não estão no repositório
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Material de estudo (paráfrase dos slides). Status da resolução: validada (resolução da equipe TutorON, não é gabarito do professor; conferida com Python).

Tanenbaum descreve o computador como uma **máquina multinível**: cada nível é uma linguagem (ou máquina virtual) que o nível de baixo executa, por **tradução** (o programa inteiro é convertido antes, como num compilador) ou **interpretação** (cada instrução é examinada e executada na hora).

Os seis níveis, de baixo para cima:
- **0. Lógico digital:** portas lógicas, registradores, memórias de 1 bit (assunto do capítulo 3). Abaixo dele fica o nível de dispositivos (transistores).
- **1. Microarquitetura:** registradores e ULA ligados pelo caminho de dados, controlados por microprograma ou por hardware.
- **2. Arquitetura do conjunto de instruções (ISA):** as instruções de máquina do manual do processador.
- **3. Máquina do sistema operacional:** a ISA mais serviços do SO (memória virtual, arquivos, processos).
- **4. Linguagem de montagem (assembly):** forma simbólica dos níveis de baixo, traduzida pelo **montador**.
- **5. Linguagem orientada a problemas:** C, Java, Python; traduzida por **compilador** ou executada por **interpretador**.

Os níveis 0 a 3 trabalham com números; os níveis 4 e 5 usam palavras legíveis por pessoas. Hardware e software são logicamente equivalentes: uma operação pode ser feita em hardware ou simulada em software.

Componentes básicos de um sistema de computação: **CPU** (unidade de controle, ULA e registradores), **memória principal** e **dispositivos de E/S**, ligados por **barramentos** (endereço, dados e controle).

**Verificação:** conte de baixo para cima: lógico digital (0), microarquitetura (1), ISA (2), SO (3), montagem (4), orientada a problemas (5): seis níveis.
