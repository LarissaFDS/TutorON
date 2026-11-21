"""Simuladores pequenos que conferem as resoluções do acervo de Sistemas Operacionais.

Cada função refaz uma conta dos blocos de `disciplinas/so/materiais`: escalonamento de tarefas, substituição
de páginas, alocação de memória, escalonamento de disco, endereços paginados e alocação de arquivos.
Convenções do caderno do Prof. Maziero: trocas de contexto nulas, empate decidido pela tarefa de menor índice,
prioridade maior = número maior.
"""

from collections import deque

# ---------------------------------------------------------------- escalonamento de tarefas


def escalonar(tarefas, politica, quantum=2):
    """tarefas: lista de (nome, ingresso, duracao, prioridade). Devolve (gantt, tempos de vida, tempos de espera).

    gantt: lista de (inicio, fim, nome). Politicas: fcfs, sjf, srtf, prio, prio_p, rr.
    """
    ordem = {n: i for i, (n, *_) in enumerate(tarefas)}
    ingresso = {n: a for n, a, _, _ in tarefas}
    resta = {n: d for n, _, d, _ in tarefas}
    prio = {n: p for n, _, _, p in tarefas}
    fim, gantt, t = {}, [], 0
    fila = deque()  # só para RR
    chegou = set()

    def admitir(ate):
        for n, a, _, _ in sorted(tarefas, key=lambda x: (x[1], ordem[x[0]])):
            if a <= ate and n not in chegou:
                chegou.add(n)
                fila.append(n)

    def anota(ini, f, n):
        if gantt and gantt[-1][2] == n and gantt[-1][1] == ini:
            gantt[-1] = (gantt[-1][0], f, n)
        else:
            gantt.append((ini, f, n))

    if politica == "rr":
        admitir(0)
        atual = None
        while len(fim) < len(tarefas):
            if not fila:
                t = min(a for n, a in ingresso.items() if n not in chegou)
                admitir(t)
            atual = fila.popleft()
            fatia = min(quantum, resta[atual])
            anota(t, t + fatia, atual)
            t += fatia
            resta[atual] -= fatia
            admitir(t)  # quem chega durante a fatia entra na fila antes de quem foi preemptado
            if resta[atual]:
                fila.append(atual)
            else:
                fim[atual] = t
    else:
        preemptiva = politica in ("srtf", "prio_p")
        chave = {
            "fcfs": lambda n: (ingresso[n], ordem[n]),
            "sjf": lambda n: (resta[n], ordem[n]),
            "srtf": lambda n: (resta[n], ordem[n]),
            "prio": lambda n: (-prio[n], ordem[n]),
            "prio_p": lambda n: (-prio[n], ordem[n]),
        }[politica]
        while len(fim) < len(tarefas):
            prontas = [n for n in resta if n not in fim and ingresso[n] <= t]
            if not prontas:
                t = min(ingresso[n] for n in resta if n not in fim)
                continue
            n = min(prontas, key=chave)
            if preemptiva:
                proximos = [ingresso[m] for m in resta if m not in fim and ingresso[m] > t]
                passo = min([resta[n], *(p - t for p in proximos)])
            else:
                passo = resta[n]
            anota(t, t + passo, n)
            t += passo
            resta[n] -= passo
            if not resta[n]:
                fim[n] = t
    duracao = {n: d for n, _, d, _ in tarefas}
    vida = {n: fim[n] - ingresso[n] for n in fim}
    espera = {n: vida[n] - duracao[n] for n in fim}
    return gantt, vida, espera


def medias(tarefas, politica, quantum=2):
    _, vida, espera = escalonar(tarefas, politica, quantum)
    k = len(tarefas)
    return sum(vida.values()) / k, sum(espera.values()) / k


# Caderno de exercícios do Prof. Maziero, cap. 2, exercício 17 (lista 2 da turma, questão 5 do cap. 6).
TAREFAS_CADERNO_17 = [("t1", 0, 5, 2), ("t2", 0, 4, 3), ("t3", 3, 5, 5), ("t4", 5, 6, 9), ("t5", 7, 4, 6)]
# Prova AB1 (respostas da turma), questão 7: lote de jobs com chegada simultânea.
JOBS_AB1_Q7 = [("A", 0, 100, 0), ("B", 0, 30, 0), ("C", 0, 20, 0), ("D", 0, 240, 0), ("E", 0, 120, 0)]


# ---------------------------------------------------------------- substituição de páginas


def faltas(refs, quadros, algoritmo):
    """Devolve (número de faltas, lista de conteúdos dos quadros após cada referência)."""
    mem, hist, n = [], [], 0
    uso = {}
    for i, p in enumerate(refs):
        if p in mem:
            uso[p] = i
        else:
            n += 1
            if len(mem) == quadros:
                if algoritmo == "fifo":
                    vitima = mem[0]
                elif algoritmo == "lru":
                    vitima = min(mem, key=lambda q: uso[q])
                elif algoritmo == "otimo":
                    futuro = refs[i + 1 :]
                    vitima = max(mem, key=lambda q: futuro.index(q) if q in futuro else len(refs) + mem.index(q))
                else:
                    raise ValueError(algoritmo)
                mem.remove(vitima)
            mem.append(p)
            uso[p] = i
        hist.append(tuple(mem))
    return n, hist


# Sequência clássica da anomalia de Belady (FIFO com 3 e 4 quadros).
BELADY = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
# Sequência usada nos blocos de LRU/FIFO/ótimo (exemplo da equipe).
REFS_EXEMPLO = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]


def envelhecimento(leituras, bits=4):
    """Algoritmo de envelhecimento (aging): a cada leitura, contador = (R << (bits-1)) | (contador >> 1)."""
    k = len(leituras[0])
    cont = [0] * k
    for r in leituras:
        cont = [(int(r[q]) << (bits - 1)) | (cont[q] >> 1) for q in range(k)]
    return cont


LEITURAS_AGING = ["0101", "0011", "1110", "1100", "1001", "1011", "1010", "0111", "0110", "0111"]


# ---------------------------------------------------------------- memória


def alocar(buracos, pedidos, estrategia):
    """Devolve os buracos depois de atender os pedidos (first, best, worst)."""
    b = list(buracos)
    for p in pedidos:
        cabem = [i for i, x in enumerate(b) if x >= p]
        if not cabem:
            raise ValueError(f"sem espaço para {p}")
        i = {
            "first": cabem[0],
            "best": min(cabem, key=lambda i: (b[i], i)),
            "worst": max(cabem, key=lambda i: (b[i], -i)),
        }[estrategia]
        b[i] -= p
    return b


BURACOS = [10, 4, 7, 30, 12, 20]
PEDIDOS = [5, 10, 2]


def bits_endereco(paginas, tamanho_pagina, quadros):
    """Bits do endereço lógico e do físico numa memória paginada."""
    desloc = (tamanho_pagina - 1).bit_length()
    return (paginas - 1).bit_length() + desloc, (quadros - 1).bit_length() + desloc


def traduzir(endereco, tamanho_pagina, tabela):
    pagina, desloc = divmod(endereco, tamanho_pagina)
    return pagina, desloc, tabela[pagina] * tamanho_pagina + desloc


# ---------------------------------------------------------------- disco


def disco(pedidos, cabeca, politica, subindo=True, maximo=199):
    """Devolve (percurso, total de blocos percorridos). SCAN e C-SCAN vão até a borda; LOOK e C-LOOK, não."""
    caminho = [cabeca]
    if politica == "fcfs":
        caminho += pedidos
    elif politica == "sstf":
        resta, pos = list(pedidos), cabeca
        while resta:
            pos = min(resta, key=lambda b: (abs(b - pos), b))
            resta.remove(pos)
            caminho.append(pos)
    else:
        # "acima" = pedidos no sentido atual, na ordem de atendimento; "abaixo" = os do outro lado, do mais perto
        if subindo:
            acima = sorted(b for b in pedidos if b >= cabeca)
            abaixo = sorted((b for b in pedidos if b < cabeca), reverse=True)
        else:
            acima = sorted((b for b in pedidos if b <= cabeca), reverse=True)
            abaixo = sorted(b for b in pedidos if b > cabeca)
        borda, outra = (maximo, 0) if subindo else (0, maximo)
        if politica == "scan":
            caminho += acima + [borda] + abaixo
        elif politica == "look":
            caminho += acima + abaixo
        elif politica == "cscan":
            caminho += acima + [borda, outra] + abaixo[::-1]
        elif politica == "clook":
            caminho += acima + abaixo[::-1]
        else:
            raise ValueError(politica)
    total = sum(abs(b - a) for a, b in zip(caminho, caminho[1:], strict=False))
    return caminho, total


PEDIDOS_DISCO = [95, 164, 36, 68, 17, 115]


# ---------------------------------------------------------------- arquivos


def ext2_maximo(bloco=1024, ponteiro_bytes=8, diretos=12):
    """Tamanho máximo de arquivo (bytes) com ponteiros diretos, indireto, duplo e triplo."""
    p = bloco // ponteiro_bytes
    return bloco * (diretos + p + p**2 + p**3)


def insercao_arquivo(alocacao, onde, blocos=500):
    """(leituras, escritas) para inserir um bloco no início ou no fim (caderno do Maziero, cap. 6).

    Contígua: só há espaço livre antes do arquivo. Encadeada: o diretório (em memória) aponta para o primeiro
    bloco. Indexada: i-node de um nível, no disco.
    """
    if alocacao == "contigua":
        return (0, 1) if onde == "inicio" else (blocos, blocos + 1)
    if alocacao == "encadeada":
        # início: grava o novo bloco apontando para o antigo primeiro; fim: percorre todos e reescreve o último
        return (0, 1) if onde == "inicio" else (blocos, 2)
    if alocacao == "indexada":
        return (1, 2)
    raise ValueError(alocacao)


def clusters(tamanho, cluster):
    return -(-tamanho // cluster)


# ---------------------------------------------------------------- impasses


def estado_seguro(disponivel, alocado, maximo):
    """Algoritmo do banqueiro (um tipo de recurso ou vetores). Devolve a ordem segura ou None."""
    um = isinstance(disponivel, int)
    if um:
        disponivel, alocado, maximo = [disponivel], [[a] for a in alocado], [[m] for m in maximo]
    livre, feito, ordem = list(disponivel), [False] * len(alocado), []
    while len(ordem) < len(alocado):
        for i, (a, m) in enumerate(zip(alocado, maximo, strict=True)):
            if not feito[i] and all(mx - al <= lv for mx, al, lv in zip(m, a, livre, strict=True)):
                livre = [lv + al for lv, al in zip(livre, a, strict=True)]
                feito[i] = True
                ordem.append(i)
                break
        else:
            return None
    return ordem


def pior_caso_sem_impasse(recursos, processos, maximo_por_processo):
    """Há impasse possível se todos podem segurar max-1 e não sobra nenhum: processos*(max-1) >= recursos."""
    return processos * (maximo_por_processo - 1) < recursos
