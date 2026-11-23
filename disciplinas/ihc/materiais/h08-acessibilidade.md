---
id: ihc-acessibilidade-letramento-digital-idosos-pessoas-com-deficiencia-wcag
titulo: Acessibilidade e letramento digital: usuários idosos e sem experiência, pessoas com deficiência, princípios do WCAG (perceptível, operável, compreensível, robusto), contraste e tamanho de alvo
assunto: ihc-01-design-centrado-no-usuario
tipo: exercicio
questao: slides (utilização universal) e autoavaliação do projeto (barreiras para o público idoso)
resolucao: sim
fonte: Slides da disciplina (utilização universal) e etapas do projeto (2020.2); diretrizes WCAG do W3C
curso: Ciência da Computação (UFAL), COMP395 Interação Homem-Máquina (ênfase Sistemas de Informação); turma 2020.2 (aulas em 2021)
fontes_catalogo: ufal-ihc-slides-dcu,ufal-ihc-etapas-projeto,w3c-wcag
autoria: Explicação da equipe TutorON com base no WCAG do W3C
licenca: Não declarada; paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Interação Humano-Computador (IC-UFAL, 2020.2), slides (utilização universal) e autoavaliação do projeto (barreiras para o público idoso) (parafraseado). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Por que importa:** a utilização universal exige que pessoas com **pouco letramento digital**, **idosos** e **pessoas com deficiência** consigam usar o sistema. Os trabalhos citados no projeto incluem a avaliação de uma plataforma por pessoas com deficiência intelectual. No microteste com iniciante, a dificuldade com teclado e *mouse* aparece antes de qualquer problema de navegação.

**WCAG** (Diretrizes de Acessibilidade para Conteúdo Web, do W3C) tem quatro princípios:
- **perceptível:**
  - texto alternativo em imagens;
  - legendas em vídeos;
  - **contraste** suficiente (texto normal: razão de pelo menos 4,5:1 no nível AA);
  - não depender só da cor;
- **operável:**
  - tudo funciona pelo teclado;
  - tempo suficiente;
  - alvos de toque grandes;
  - sem conteúdo que pisca perigosamente;
- **compreensível:**
  - linguagem simples;
  - comportamento previsível;
  - ajuda para corrigir erros em formulários;
- **robusto:** funciona com tecnologias assistivas, como leitores de tela.

**Para idosos e iniciantes:**
- letras e botões maiores;
- rótulos com texto, não só ícones;
- menos passos;
- caminho principal sempre visível;
- confirmação em ações irreversíveis;
- **mais de um caminho** para a função principal (busca e menu).

**Razão de contraste:** $(L_1 + 0{,}05)/(L_2 + 0{,}05)$, com $L$ a luminância relativa da cor mais clara ($L_1$) e da mais escura ($L_2$). Preto no branco dá 21:1.

**Verificação:** `test_razao_de_contraste` calcula a luminância relativa pela fórmula do WCAG e confere 21:1 para preto no branco, 1:1 para cores iguais, e que cinza `#777777` no branco fica abaixo de 4,5:1.
