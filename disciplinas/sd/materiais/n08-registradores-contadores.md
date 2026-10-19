---
id: sd-nota-registradores-contadores
titulo: Nota — registrador com carga (ld/clr), registrador de deslocamento e contador com tc
assunto: sd-08-registradores-contadores
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: wikibooks-digital-circuits,wikilivros-eletronica-digital,kuphaldt-lec-vol4
autoria: Equipe TutorON, redigida com auxílio de IA; revisão humana pendente
licenca: Texto original da equipe TutorON
curadoria: aprovado
---
Registradores e contadores

Registrador de n bits: n flip-flops D com o mesmo clock. Com carga paralela (ld): um MUX 2:1 na entrada de cada flip-flop escolhe entre a entrada nova (ld = 1) e a própria saída (ld = 0, mantém). Com clr: zera na borda (ou de forma assíncrona). Nos projetos RTL, cada registrador do bloco operacional tem sinais _ld e _clr comandados pela FSM.

Registrador de deslocamento: a saída de cada flip-flop alimenta o seguinte; a cada borda, os bits andam uma posição e entra o bit serial. Com MUX 4:1 na entrada de cada flip-flop e seleção comum (por exemplo, um controle T de 2 bits), o mesmo registrador pode manter, deslocar à direita, deslocar à esquerda ou carregar em paralelo. Para explicar um circuito desses, faça uma tabela "valor de controle → o que entra no D de cada flip-flop → operação".

Contador binário síncrono: registrador + incrementador (C+ = C + 1). Com flip-flops T, o bit i inverte quando todos os bits abaixo dele valem 1: Tᵢ = Q₀·Q₁·…·Qᵢ₋₁.
- ld (load): carrega um valor inicial em vez de contar.
- tc (terminal count): vale 1 quando o contador atinge o valor final (1111 num contador de 4 bits crescente; 0000 num decrescente); serve para encadear contadores ou avisar o fim de uma contagem.
- Contador módulo M: detecta o valor M − 1 e volta a zero (ou carrega 0) na próxima borda.
- Contador assíncrono (ripple): o clock de cada flip-flop é a saída do anterior. É mais simples, mas acumula atrasos.

Divisor de frequência: o bit i de um contador oscila com a frequência do clock dividida por 2ⁱ⁺¹.
