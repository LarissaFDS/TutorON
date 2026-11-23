---
id: redes-controle-de-fluxo-versus-congestionamento-tcp-udp
titulo: Controle de fluxo × controle de congestionamento (rwnd e cwnd), por que não são equivalentes, por que um fluxo TCP recua para quase 0 competindo com um fluxo UDP
assunto: redes-05-congestionamento
tipo: prova
questao: prova 1 2012 Q1; AB1 2017 Q5; reposição AB1 2020.1 Q1
resolucao: sim
fonte: Provas de 2012, 2017 e 2020.1 de Redes de Computadores 1, Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Redes de Computadores 1 (COMP — Prof. Leandro Melo de Sales); provas de 2012, 2017 e 2020.1
fontes_catalogo: ufal-leandro-provas-redes
autoria: Questões do Prof. Leandro Melo de Sales (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, fotos e PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Provas de Redes de Computadores 1 do Prof. Leandro Melo de Sales (UFAL), prova 1 2012 Q1; AB1 2017 Q5; reposição AB1 2020.1 Q1 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Não são equivalentes:** os dois limitam o emissor, mas protegem coisas diferentes.
- **Controle de fluxo** protege o **receptor**: não enviar mais do que o buffer dele comporta. O receptor anuncia a janela de recepção **rwnd** (espaço livre) em cada segmento; é uma conversa entre os dois sistemas finais.
- **Controle de congestionamento** protege a **rede**: não enviar mais do que os roteadores do caminho suportam. O emissor **estima** a janela de congestionamento **cwnd** a partir de sinais indiretos (perdas, *timeouts*, ACKs duplicados), sem ajuda da rede.

O emissor TCP mantém em trânsito no máximo $\min(\text{rwnd}, \text{cwnd})$ bytes não confirmados. Um receptor rápido numa rede lenta é limitado pelo cwnd; um receptor lento numa rede vazia, pelo rwnd.

**TCP × UDP no mesmo enlace:** o UDP **não tem controle de congestionamento**: envia à taxa que a aplicação quiser. Quando o enlace satura, os dois perdem pacotes. O TCP interpreta a perda como congestionamento e **reduz a cwnd à metade (ou a 1)**, e o UDP continua igual. Cada recuo do TCP deixa mais espaço que o UDP ocupa. Repetindo, a vazão do TCP vai a quase zero. O TCP é "educado" e o UDP não; por isso se discute justiça (*fairness*) e controle de congestionamento para aplicações sobre UDP.

Erro comum: dizer que o controle de fluxo evita congestionamento na rede.

**Verificação:** `test_fluxo_e_congestionamento` confere que a janela efetiva é $\min(\text{rwnd}, \text{cwnd})$ nos dois casos e simula, rodada a rodada, um fluxo TCP com AIMD num enlace de 100 pacotes por rodada dividido com um fluxo UDP de 95: a vazão média do TCP fica abaixo de 10% do enlace.
