---
id: pcom-lista4-distancia-separacao
titulo: Lista 4: distância mínima entre transmissor de RF (4G, 5G) e equipamento médico (oxímetro, imunidade de 3 V/m), d = (6/E)·√P
assunto: pcom-08-exposicao-campos
tipo: lista
resolucao: sim
fonte: Anotações "Lista 4" (22 out. 2026), p. 2 (questão 7, enunciado não transcrito)
autoria: Otávio Joshua Costa Brandão Menezes (aluno da turma de Princípios de Comunicação 2026.2; docente Jobson de Araújo Nascimento, conforme os cabeçalhos das simulações); paráfrase e conferência da equipe TutorON
licenca: Não declarada (anotações manuscritas de aluno, 2026.2); PDFs e imagens fora do repositório
publicacao_transcricao: autorizada pelo autor (integrante da equipe TutorON), conforme registro da equipe; enunciados de listas e de provas parafraseados; fotos de slide, capturas de tela e figuras coladas não foram copiadas
fontes_catalogo: ufal-pcom-anotacoes-otavio-2026-2, iec-60601-1-2
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
revisao_humana: pendente
status_resolucao: pendente_professor
---
Anotações de aluno (2026.2), parafraseadas e conferidas pela equipe. Status da resolução: pendente de confirmação do professor.

**Ideia:** um equipamento médico (aqui um oxímetro) suporta, sem falhar, um campo $E_1$ (nível de imunidade, 3 V/m na anotação). A distância mínima a um transmissor de potência $P$ é aquela em que o campo do transmissor cai para $E_1$. A forma usada pela norma de compatibilidade eletromagnética de equipamentos médicos (IEC 60601-1-2) é
$$d = \frac{6}{E_1}\sqrt{P}$$ (d em metros, P em watts, E em V/m: seis sobre E vezes a raiz de P).

**Contas das anotações:**
- "5G" (ou celular de 22,5 mW): $d = \frac{6\sqrt{22{,}5\cdot 10^{-3}}}{3} = \frac{6\cdot 0{,}15}{3} = 0{,}3$ m. Se a distância real é maior que 0,3 m, há conformidade.
- 4G com 90 mW: a anotação usa outro fator, $d = \frac{23\sqrt{90\cdot 10^{-3}}}{3} = \frac{23\cdot 0{,}3}{3} = 2{,}3$ m, e conclui "não há conformidade". Com o fator 6, seria $\frac{6\cdot 0{,}3}{3} = 0{,}6$ m.

As contas estão certas com os fatores escritos, mas a origem do fator 23 não foi identificada, e a distância real comparada está no enunciado, que não foi transcrito.

Pendente: confirmar com o professor a fórmula e os dados da questão; consulte a cláusula 8.10 da IEC 60601-1-2 (texto protegido, não incluído aqui).

**Verificação:** $\sqrt{0{,}0225} = 0{,}15$ e $\sqrt{0{,}09} = 0{,}3$; as três distâncias (0,3 m, 2,3 m e 0,6 m) foram recalculadas.
