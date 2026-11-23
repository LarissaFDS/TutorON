---
id: ia-raciocinio-baseado-em-casos-rbc-ciclo-dos-4-rs-recuperar-reusar-revisar-reter-similaridade
titulo: Raciocínio baseado em casos (RBC): ciclo dos 4 Rs (recuperar, reusar, revisar, reter), problemas e técnicas de cada etapa, similaridade por vizinho mais próximo, exemplo
assunto: ia-04-incerteza-e-aprendizado
tipo: lista
questao: Lista 2 (2020.2), questão 1 sobre raciocínio baseado em casos
resolucao: sim
fonte: Listas 1 e 2 de Inteligência Artificial (IC-UFAL), 2020.2, Prof. Evandro de Barros Costa
curso: Ciência da Computação (UFAL), COMP380 Inteligência Artificial; turma 2020.2 (Prof. Evandro de Barros Costa)
fontes_catalogo: ufal-ia-listas-2020-2
autoria: Questões do Prof. Evandro de Barros Costa (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Inteligência Artificial (IC-UFAL, 2020.2), Lista 2 (2020.2), questão 1 sobre raciocínio baseado em casos (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**RBC:** resolve um problema novo adaptando a solução de **casos** passados parecidos. Um caso é (descrição do problema, solução, resultado).

**Ciclo dos 4 Rs** (Aamodt e Plaza), com o problema central e as técnicas de cada etapa:
- **Recuperar:** achar os casos mais parecidos. Problema: medir **similaridade** e indexar a base. Técnicas: vizinho mais próximo com pesos, $\text{sim}(q,c) = \sum_i w_i\,\text{sim}_i(q_i,c_i) / \sum_i w_i$; índices e árvores para filtrar.
- **Reusar:** aplicar a solução do caso recuperado. Problema: o que transferir. Técnicas: cópia direta, adaptação **transformacional** (ajusta a solução) ou **derivacional** (refaz o raciocínio).
- **Revisar:** avaliar e corrigir a solução proposta. Problema: detectar falhas. Técnicas: simulação, avaliação por especialista, regras de reparo.
- **Reter:** guardar o caso novo. Problema: o que guardar sem inchar a base. Técnicas: atualizar índices e pesos, esquecer casos redundantes.

**Exemplo (estrutura pedida no item b):** base de suporte técnico de celulares com marca, modelo e sintoma. Um caso novo (mesma marca, sintoma "não liga") recupera o caso "desliga sozinho, troca de bateria" por ter a maior similaridade, reusa a solução, revisa para o modelo específico e retém o caso resolvido.

Na resposta, mostre a **conta de similaridade** com os pesos, não só a escolha do caso.

**Verificação:** `test_rbc_similaridade` calcula a similaridade ponderada de um caso novo contra uma base pequena e confere que o recuperado é o de maior similaridade.
