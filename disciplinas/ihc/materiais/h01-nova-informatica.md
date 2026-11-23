---
id: ihc-nova-informatica-excelencia-no-design-utilizacao-universal-therac-25-iran-air-655
titulo: A nova informática (Shneiderman): excelência no design, utilização universal, casos de falha de interface (Therac-25, voo Iran Air 655) e o que eles ensinam sobre feedback e mensagens de erro
assunto: ihc-01-design-centrado-no-usuario
tipo: exercicio
questao: slides 1 a 11
resolucao: sim
fonte: Slides "A Nova Informática: Design centrado no Usuário" da disciplina (base: Shneiderman, 2006; Nielsen, 1993)
curso: Ciência da Computação (UFAL), COMP395 Interação Homem-Máquina (ênfase Sistemas de Informação); turma 2020.2 (aulas em 2021)
fontes_catalogo: ufal-ihc-slides-dcu,shneiderman-laptop-leonardo
autoria: Slides da disciplina (IC-UFAL); explicação da equipe TutorON
licenca: Não declarada; paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Interação Humano-Computador (IC-UFAL, 2020.2), slides 1 a 11 (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**A nova informática** (Shneiderman, *O Laptop de Leonardo*, 2006) pede três coisas:
- **excelência no design**;
- **utilização universal**;
- **métodos eficientes** para criar software que pessoas comuns usem com sucesso.

**Excelência no design:** os slides comparam com campanhas de segurança de outras áreas: Ralph Nader (1965) contra carros mal projetados e Rachel Carson (1962) contra pesticidas. Uma interface malfeita também pode ter efeito catastrófico.

**Therac-25** (máquina de radioterapia controlada por computador, anos 1980): pacientes receberam doses maciças de radiação. Os problemas de interface apontados:
- **feedback pobre** para o operador;
- **mensagens de erro obscuras** ("Malfunction 54", sem dizer o que fazer);
- **manuais de treinamento incompletos**.

Os operadores se acostumaram a ignorar e prosseguir.

**Voo Iran Air 655** (1988): o avião civil foi abatido e 290 pessoas morreram. A apresentação confusa das informações no sistema de defesa contribuiu para o operador achar que o Airbus era um caça.

**O que isso ensina** (ligue às heurísticas de Nielsen):
- mostrar o **estado do sistema** com clareza;
- mensagens de erro que **digam o problema e a saída**;
- **prevenir erros** em ações perigosas: confirmação e limites que o sistema impõe;
- treinar e documentar.

**Utilização universal:** segundo Shneiderman, o uso é universal quando 90% das famílias usam com sucesso as tecnologias de informação e comunicação pelo menos uma vez por semana. **Dar acesso não basta**: a complexidade dos serviços exige design para pessoas com pouca experiência, idosos e pessoas com deficiência.

**Verificação:** `test_mensagem_de_erro_util` confere a regra prática: uma mensagem útil diz o que aconteceu e o que fazer ("Malfunction 54" falha nas duas).
