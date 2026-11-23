---
id: direito-digital-provas-whatsapp-ata-notarial-prova-ilicita-teoria-dos-frutos-da-arvore-envenenada
titulo: Direito digital e provas: como usar uma conversa de WhatsApp como prova (ata notarial no cartório de notas, fragilidade de prints), provas ilícitas (Constituição, art. 5º, LVI) e a teoria dos frutos da árvore envenenada
assunto: dir-03-direito-civil-e-digital
tipo: prova
questao: Avaliação de 2020.2, questões sobre prova digital
resolucao: sim
fonte: Avaliações de Noções de Direito da Profa. Jessica Hind (IC-UFAL), 2020.2 (setembro e outubro de 2021), e slides "Noções Iniciais" da disciplina
curso: Ciência da Computação (UFAL), COMP387 Noções de Direito (7º período); turma 2020.2 (aulas em 2021)
fontes_catalogo: ufal-direito-avaliacoes,constituicao-planalto
autoria: Questões da Profa. Jessica Hind (IC-UFAL); explicação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Noções de Direito (IC-UFAL, 2020.2), Avaliação de 2020.2, questões sobre prova digital (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

Conteúdo de estudo, não é aconselhamento jurídico. Para um caso real, procure um advogado ou a Defensoria Pública.

**Conversa de aplicativo como prova:**
- o recomendado é ir a um **cartório de notas** e pedir uma **ata notarial**. O tabelião, que tem fé pública, vê a conversa no aparelho e descreve o conteúdo, a data e os participantes. O Código de Processo Civil prevê a ata notarial, inclusive para dados de imagem ou som em arquivos eletrônicos;
- **prints** sozinhos são fáceis de editar e podem ser contestados;
- **apagar** mensagens para destacar só algumas compromete a integridade da prova;
- copiar o texto num editor de texto não prova nada.

Outra opção é a perícia ou a preservação técnica, com cadeia de custódia e hash dos arquivos.

**Provas ilícitas:** a Constituição (art. 5º, LVI) diz que são **inadmissíveis**, no processo, as provas obtidas por meios ilícitos. Exemplo: um grampo telefônico sem ordem judicial.

**Teoria dos frutos da árvore envenenada** (origem na jurisprudência dos EUA): a ilicitude da prova original **contamina** as provas **derivadas** dela. Exemplo: uma busca feita a partir de informações do grampo ilegal. O Código de Processo Penal adota a ideia, com duas exceções:
- quando não há **nexo de causalidade** com a prova ilícita;
- quando a prova derivada poderia ser obtida por uma **fonte independente**.

Não confunda com os crimes contra a honra (calúnia, difamação, injúria) nem com a proteção de dados (LGPD), que são outros temas da mesma área.

**Verificação:** `test_prova_derivada` modela a regra da contaminação (derivada de ilícita sem fonte independente é inadmissível) e confere que o bloco só cita o artigo da Constituição conferido no texto oficial.
