---
id: redes-subredes-mascara-30-26-endereco-9-ttl
titulo: Endereçamento IP: A 192.168.0.9 e B 192.168.0.13 com máscara /30 conversam? faixas das sub-redes de 192.168.1.0 com máscara 255.255.255.192, endereços disponíveis em 10.0.0.0/9, campo TTL do IPv4
assunto: redes-06-camada-de-rede
tipo: prova
questao: AB2 2020.1 Q4; reposição AB2 2020.1 Q4 e Q5; AB2 2017 Q2 e Q3
resolucao: sim
fonte: Provas AB2 de 2017 e 2020.1 e reposição da AB2 de 2020.1 de Redes de Computadores 1, Prof. Leandro Melo de Sales (IC-UFAL)
curso: Ciência da Computação (UFAL), Redes de Computadores 1 (COMP — Prof. Leandro Melo de Sales); provas de 2017 e 2020.1
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
Provas de Redes de Computadores 1 do Prof. Leandro Melo de Sales (UFAL), AB2 2020.1 Q4; reposição AB2 2020.1 Q4 e Q5; AB2 2017 Q2 e Q3 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**/30 (255.255.255.252):** sobram 2 bits para hospedeiros, blocos de $2^2 = 4$ endereços: rede, 2 hospedeiros, broadcast. A = 192.168.0.9 está no bloco **.8–.11** (rede .8, hospedeiros .9 e .10, broadcast .11). B = 192.168.0.13 está em **.12–.15**. Estão em **sub-redes diferentes**: mesmo no mesmo barramento, cada um acha que o outro está fora da sua rede e manda o pacote ao gateway. **Sem um roteador** entre as duas sub-redes, **não conversam**. Teste rápido: A AND máscara = .8 e B AND máscara = .12; são diferentes.

**192.168.1.0 com 255.255.255.192 (/26):** 2 bits de sub-rede, 4 sub-redes de 64 endereços:
| sub-rede | hospedeiros | broadcast |
|---|---|---|
| 192.168.1.0 | .1 a .62 | .63 |
| 192.168.1.64 | .65 a .126 | .127 |
| 192.168.1.128 | .129 a .190 | .191 |
| 192.168.1.192 | .193 a .254 | .255 |
(O exemplo do enunciado, ".0 – .4; .5 – .8", só mostra o formato; não são blocos de máscara.)

**10.0.0.0/9:** $32 - 9 = 23$ bits de hospedeiro: $2^{23} - 2 = 8\,388\,606$ endereços para máquinas (menos a rede e o broadcast), de 10.0.0.1 a 10.127.255.254.

**TTL (*time to live*):** campo de 8 bits do IPv4. Cada roteador o **decrementa**; se chega a 0, o datagrama é **descartado** e volta uma mensagem ICMP *Time Exceeded*. Evita que pacotes circulem para sempre num laço de roteamento. O **traceroute** usa isso: manda pacotes com TTL 1, 2, 3, … e descobre cada roteador pelas respostas ICMP.

**Verificação:** `test_subredes` usa o módulo `ipaddress` do Python: A e B ficam em redes /30 diferentes, a /26 dá as 4 faixas da tabela, e `10.0.0.0/9` tem 8 388 606 hospedeiros.
