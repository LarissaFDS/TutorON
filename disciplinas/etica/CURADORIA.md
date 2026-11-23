# Curadoria — Computação, Sociedade e Ética

Situação: **em validação**. Revisão humana pendente em todos os blocos.

## Origem e ementa
Material da turma de Ciência da Computação da UFAL (pasta `03. COMP361 - Computação, Sociedade e
Ética`), turmas X e M, semestre 2020.2, com entregas em maio e junho de 2021. São três enunciados de
avaliação:
- Reavaliação da AB1;
- Reavaliação da AB2;
- Avaliação Final.

Juntos, eles trazem seis questões, todas trabalhos escritos. O professor não aparece nos arquivos.

**Ementa não conferida.** O prompt indica impactos sociais, ética profissional, privacidade, LGPD e
propriedade intelectual, mas pede que isso seja confirmado pela ementa, que não estava disponível.
Os blocos cobrem o que as avaliações pedem:
- ética e moral;
- TIC na pandemia;
- computação verde;
- EaD;
- código de conduta;
- IA e ética com a técnica dos 4 passos.

A LGPD entra como apoio, porque é citada nesses temas. **Propriedade intelectual não tem bloco**: não
há material da turma sobre ela.

## O que entrou
9 blocos (`materiais/e01`–`e09`).
- Os blocos e01–e07 explicam o método e dão um roteiro, sem o texto pronto, e apresentam posições
  divergentes nos temas controversos.
- O bloco e01 **não resume** o artigo de Cremonese: não foi lido nesta curadoria. O aluno deve ler o
  original.

## Conferência das citações legais
**LGPD:** os artigos 5º (I, II, III, V, VI, VII, VIII, X), 6º (I a X), 7º (I a X), 14, 18 e 20 foram
conferidos em 22/11/2026 no texto do Planalto (`lgpd-planalto`). O texto do Planalto traz alterações
posteriores, como a Lei 13.853/2019 e normas mais recentes. Os valores da multa do art. 52 não foram lidos direto do texto e **o bloco não os cita**; conferir na
versão compilada.

**Código de ética do IEEE:** a página oficial não carregou na consulta. Por isso o bloco e07 não numera
nem reproduz itens do código e pede ao aluno que cite pelo texto oficial.

Os testes em `tests_acervo/test_disciplina_etica.py` conferem:
- as citações de artigos e incisos contra uma tabela tirada do texto oficial;
- a soma dos critérios de pontuação;
- o PUE;
- a ordem dos 4 passos;
- a estrutura do código de conduta.

## O que ficou de fora
- **Os arquivos originais:** não foram versionados.
- **Trabalhos de alunos:** nenhum, porque a pasta não tem.

## Fronteiras
Metodologia da Pesquisa (`metodologia`) cobre método e normas de citação; Segurança de Sistemas
Computacionais (`seguranca`) cobre os mecanismos técnicos. O isolamento é testado nos dois sentidos.
Noções de Direito ainda não está cadastrada.

## Pendências
- Revisão humana dos blocos.
- Ementa de COMP361.
- Art. 52 da LGPD na versão compilada.
- Texto do código de ética do IEEE.
- Material sobre propriedade intelectual.
