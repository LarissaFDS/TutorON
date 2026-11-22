---
id: sd_dist-modelo-sincrono-assincrono-detectores-de-falhas-confiaveis
titulo: Modelo de sistema distribuído síncrono × assíncrono; detectores de falhas: o que são, detector confiável (reliable) × não confiável (unreliable)
assunto: sd_dist-03-coordenacao-e-falhas
tipo: prova
questao: provas de 2017 (prova 2 Q1); AB2 de 2017 Q2
resolucao: sim
fonte: Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Sistemas Distribuídos (CCOM044); provas de 2017
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
Provas de Sistemas Distribuídos do Prof. Leandro Melo de Sales (UFAL), provas de 2017 (prova 2 Q1); AB2 de 2017 Q2 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Modelo síncrono:** existem **limites conhecidos** para (1) o tempo de execução de cada passo de um processo, (2) o tempo de entrega de uma mensagem e (3) a taxa de desvio dos relógios locais. **Modelo assíncrono:** **não há limite** para nenhum dos três: um processo pode demorar qualquer tempo, e uma mensagem pode chegar depois de qualquer atraso. A Internet é assíncrona. (Dizer só "tem ou não tem relógio global" é incompleto.)

**Detector de falhas:** serviço que responde, sobre cada processo, se ele **falhou** (*crashed*). Implementação usual: cada processo envia **"estou vivo"** (*heartbeat*) a cada $T$ segundos; se nada chega em $T + D$ (com $D$ o atraso máximo estimado), o detector **suspeita** da falha.

**Não confiável (*unreliable*):** responde **"suspeito"** ou **"não suspeito"**. Pode errar nos dois sentidos: suspeitar de um processo **lento** que está vivo, ou ainda não ter notado um que caiu. É o único possível num sistema **assíncrono**, porque lá não há como distinguir um processo morto de um muito lento.

**Confiável (*reliable*):** responde **"falhou"** (com certeza) ou "não suspeito". Exige **sistema síncrono**: com o limite $D$ garantido, a falta do *heartbeat* em $T + D$ prova a falha.

Consequência prática: escolher $T + D$ pequeno detecta rápido, mas gera **falsas suspeitas**; escolher grande reduz erros, mas demora a reagir.

**Verificação:** `test_detector_de_falhas` simula *heartbeats* com atrasos: com limite de atraso garantido (síncrono), o detector nunca suspeita de um processo vivo; com atrasos sem limite (assíncrono), ele suspeita de um processo lento e vivo, e um prazo maior reduz as falsas suspeitas.
