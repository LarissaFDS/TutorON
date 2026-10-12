# TutorON — baseline de validação local

Este relatório separa execução técnica de validação pedagógica. Os resultados anteriores de 41%/70% pertencem à PoC fornecida, não a esta rodada.

## 1. Digitalizar e revisar o acervo

- 57 documentos de entrada inventariados; 57 saídas de extração.
- 161 páginas/blocos: boa: 10, ilegivel: 5, parcial: 146.
- 0 tentativas de visão em recortes/fotos: 0 candidatos incertos e 0 falhas. Nenhum candidato substitui automaticamente a fonte.
- Cópias imutáveis por hash em 00-originais; imagens/páginas para conferência em 01-extraido/figuras.
- Extração automática não certifica manuscritos, fórmulas, diagramas nem qualidade de soluções.

## 2. Organizar por questão, fonte e confiabilidade

- 220 blocos no índice; 15 sem segmentação segura.
- 10 classificados como baixa confiança, incluindo ilegíveis.
- Pareceres locais: 16 concluídos; 0 falhas; os demais não foram solicitados ou não tinham resolução identificada.
- Contagens por assunto (blocos candidatos, não questões únicas certificadas):

  - assunto_incerto: 90
  - b1-01-corretude-complexidade: 40
  - b1-02-divisao-e-conquista: 15
  - b1-03-algoritmos-gulosos: 24
  - b2-04-programacao-dinamica: 13
  - b2-05-transformacao-de-problemas: 10
  - b2-06-np-completude: 18
  - b2-07-lidando-com-np-completude: 10

## 3. Automatizar a busca do trecho certo

- 53 blocos elegíveis; busca: hibrido.
- Baixa confiança, ilegíveis e cortes incertos não entram na busca. Metadados acompanham cada citação.
- Ollama local; Gemini opcional com fallback. As chamadas reais registram provedor, modelo e tempo.

## 4. Validar com questões, alunos e professor

- 12 questões no conjunto; 48 respostas reais concluídas na rodada atual.
- 12 pares offline; 0 registros de avaliação salvos (não equivalem, por si, a um estudo com alunos).
- Comparação A/B sorteada no servidor; notas separadas para clareza, confiança e utilidade.
- Professor: pendente. As expressões regulares medem cobertura lexical, não prova de correção.

## Limitações e revisão manual necessária

- Conferir páginas com imagens e OCR parcial; segmentação automática pode confundir enumerações e linhas de código.
- Conferir origem/autoria e corrigir apenas em arquivos derivados aprovados; triagem não reescreve resoluções.
- Revisar suspeitas em 03-triagem/relatorio.md e confirmar enunciados, fontes esperadas e checklists em 06-avaliacao/questoes.json.
- Nenhum fine-tuning foi executado. Dataset só admite pares de alta confiança, com aprovação e fonte verificável.
- A comparação rápida antiga em 05-modelo/comparacao.json pertence ao hardware Windows de setembro; não é o resultado desta validação Linux.
- Inferência e acervo são locais; GitHub recebe código e artefatos de validação. Não há publicação do servidor nem envio a Gemini nesta rodada.

Execução: iniciar_validacao.sh (Linux) ou iniciar_validacao.bat (Windows). avaliar_modelos executa quatro condições, incluindo controle somente com instruções.

## Resultados técnicos do checklist

| Condição | Respostas concluídas | Critérios encontrados / aplicáveis |
|---|---:|---:|
| generico | 12 | 17 / 46 |
| controle_prompt | 12 | 16 / 47 |
| rag_manual | 12 | 30 / 47 |
| rag_automatica | 12 | 29 / 47 |

Esses números não são acurácia matemática. Fontes recuperadas e exclusões estão em 06-avaliacao/relatorio.md; respostas, tempos de geração e eventuais repetições estão em 06-avaliacao/resultados.json.
