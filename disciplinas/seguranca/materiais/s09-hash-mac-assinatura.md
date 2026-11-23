---
id: seguranca-hash-codigo-de-autenticacao-de-mensagem-mac-hmac-assinatura-digital-certificado-x509-autoridade-certificadora
titulo: Funções hash, código de autenticação de mensagem (MAC, HMAC), assinatura digital, certificado digital (padrão X.509, diretório X.500), autoridade certificadora e proteção de e-mail com confidencialidade, autenticidade e integridade
assunto: seg-03-criptografia-e-autenticacao
tipo: prova
questao: Final e Reposição AB2, questão 1 (MAC); AB2, questão 7; Lista 8, questões 3 e 5; Lista 10, questão 3
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
Segurança de Sistemas Computacionais (IC-UFAL), Final e Reposição AB2, questão 1 (MAC); AB2, questão 7; Lista 8, questões 3 e 5; Lista 10, questão 3 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Hash criptográfico** (SHA-256): resumo de tamanho fixo. É difícil inverter e difícil achar duas mensagens com o mesmo resumo. Sozinho não autentica: qualquer um recalcula o hash de uma mensagem alterada.

**MAC (código de autenticação de mensagem):** resumo que depende de uma **chave secreta compartilhada**, $\text{MAC} = H_K(m)$. Por exemplo, **HMAC**: $H\big((K \oplus \text{opad}) \,\|\, H((K \oplus \text{ipad}) \,\|\, m)\big)$. O emissor envia $m$ e o MAC. O receptor recalcula com a mesma chave e compara. Garante **integridade e autenticidade da origem**, mas **não** não repúdio, porque os dois lados têm a chave.

**Assinatura digital:** o emissor cifra o **hash** da mensagem com a sua **chave privada**. Qualquer um verifica com a chave pública. Garante integridade, autenticidade e **não repúdio**.

**Certificado digital (X.509):** arquivo assinado por uma **Autoridade Certificadora (AC)** que liga uma chave pública a uma identidade. Contém:
- nome do titular;
- **chave pública**;
- número de série;
- validade;
- emissor;
- assinatura da AC.

Na questão 7 da AB2, a resposta são essas informações, não senhas nem biometria. O **X.500** é o padrão de diretório (nomes distintos, como `CN=..., O=..., C=BR`) usado nos campos do X.509. A AC emite, renova e **revoga** certificados (lista de revogação, OCSP). 

**E-mail com confidencialidade, autenticação do emissor e integridade** (ideia do PGP/S-MIME):
1. o emissor assina o hash com a sua chave privada (autenticação e integridade);
2. gera uma chave de sessão simétrica e cifra a mensagem e a assinatura;
3. cifra a chave de sessão com a **chave pública do destinatário** (confidencialidade);
4. o destinatário faz o caminho inverso.

**Verificação:** `test_hmac_detecta_alteracao` usa `hmac` e `hashlib`: o MAC confere com a chave certa, falha com outra chave ou com um byte alterado, e a comparação usa `hmac.compare_digest`.
