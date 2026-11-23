---
id: seguranca-engenharia-social-phishing-pharming-dns-contramedidas
titulo: Engenharia social, phishing e Pharming (desvio de DNS para site falso): definição e contramedidas; engenharia social junto com negação de serviço
assunto: seg-02-ameacas-e-ataques
tipo: prova
questao: AB1 2020.1, questões 2 e 5; Reposição AB1 e Final, Pharming; Lista 5, questões 3 e 5
resolucao: sim
fonte: Provas (2020.1 e 2020.2) e listas semanais de Segurança de Sistemas Computacionais do IC-UFAL
curso: Ciência da Computação (UFAL), COMP403 Segurança de Sistemas Computacionais (ênfase Sistemas de Informação); provas de 2020.1 e 2020.2 (algumas com cabeçalho de Engenharia da Computação)
fontes_catalogo: ufal-seguranca-provas-listas
autoria: Questões das provas e listas da disciplina (IC-UFAL; professor não identificado nos PDFs); explicação da equipe TutorON
licenca: Não declarada (provas e listas); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Segurança de Sistemas Computacionais (IC-UFAL), AB1 2020.1, questões 2 e 5; Reposição AB1 e Final, Pharming; Lista 5, questões 3 e 5 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

Só defesa e conceitos: o acervo não traz roteiro de ataque nem código de exploração.

**Engenharia social:** obter informação ou acesso explorando a **confiança das pessoas**, não uma falha técnica. Exemplos: ligação fingindo ser do suporte pedindo a senha, crachá emprestado, *e-mail* urgente do "diretor". É a porta de entrada de muitos ataques. Pode ser combinada com negação de serviço: o serviço cai e o falso "técnico" liga oferecendo ajuda.

**Phishing:** mensagem falsa que leva a vítima a um site falso ou a abrir um anexo. A vítima precisa clicar.

**Pharming:** o desvio acontece na **resolução de nomes**. A vítima digita o endereço certo e chega ao site falso, porque o DNS foi adulterado: arquivo `hosts` alterado, cache do servidor DNS envenenado ou roteador doméstico com DNS trocado. É mais perigoso que o phishing porque o endereço digitado está correto.

**Contramedidas:**
- **HTTPS com verificação do certificado**: o site falso não tem certificado válido para o nome, e o navegador avisa;
- **DNSSEC**: respostas DNS assinadas;
- resolvedor DNS confiável, roteador com a senha padrão trocada e *firmware* atualizado;
- antivírus e conferência do arquivo `hosts`;
- conscientização: não ignorar aviso de certificado;
- autenticação em dois fatores, que limita o estrago de uma senha roubada.

**Contra engenharia social:**
- política escrita que diz que senha nunca é pedida por telefone;
- treinamento;
- canal de confirmação;
- menor privilégio.

**Verificação:** `test_certificado_confere_nome` usa a regra de nomes de `ssl.match_hostname` (reimplementada) para mostrar que um certificado de `banco.com.br` não vale para `banco-seguro.net`.
