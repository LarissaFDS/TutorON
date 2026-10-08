# TutorON — validar antes do MVP

Resultados medidos e pendências: [RELATORIO_VALIDACAO.md](RELATORIO_VALIDACAO.md). A [PoC histórica](docs/POC_HISTORICA.md) foi preservada. A branch de trabalho é `codex/paa-acervo-validacao`, reunida no [PR #15](https://github.com/LarissaFDS/TutorON/pull/15).

## Abrir a validação

No Ubuntu, o duplo clique em `.sh` pode abrir um editor. Para instalar o atalho **TutorON — Validação** no menu de aplicativos e na área de trabalho, execute uma vez, pelo terminal dentro da pasta do projeto:

```bash
bash instalar_atalho.sh
```

Depois abra o atalho. Se o Ubuntu pedir, clique com o botão direito nele e escolha **Permitir execução**. Com os serviços locais já ativos, também basta abrir http://127.0.0.1:8765 no navegador.

No Ubuntu, dentro da pasta do projeto:

```bash
./preparar_modelos.sh
./iniciar_validacao.sh
```

No Windows, execute `preparar_modelos.bat` e depois `iniciar_validacao.bat`. Abra http://127.0.0.1:8765. Mantenha notebook e terminal ativos, sem suspensão; Ctrl+C encerra o servidor.

Escolha a questão, compare A/B, dê as notas e indique sua preferência. A posição é sorteada. Votos reais ficam em `07-validacao-alunos/respostas.csv`, fora do Git. Não informe dados pessoais nos comentários. Nenhum voto humano foi fabricado nesta rodada.

Pares prontos são respostas reais armazenadas; perguntas livres exigem Ollama e podem levar minutos nesta CPU. Os textos podem conter erros: a comparação coleta evidências, não garante correção matemática.

## Atualizar OCR e dados

Coloque fontes em `materiais/Disponiveis`. No Ubuntu 24.04 amd64:

```bash
./instalar_ocr.sh
./atualizar_acervo.sh
.venv-acervo/bin/python -m acervo.audit
./testar_acervo.sh
```

No Windows use os equivalentes `.bat` e instale Tesseract com português/inglês para reproduzir esse motor. RapidOCR é o fallback. PNG, JPEG, WebP, BMP, GIF, TIFF e PDFs digitalizados são aceitos. Manuscritos, diagramas e fórmulas exigem conferência visual. `extrair_com_visao` produz interpretações separadas, incertas e lentas nesta CPU.

Confira [a auditoria por arquivo](03-triagem/AUDITORIA.md), `01-extraido/`, `02-acervo/itens.json` e `03-triagem/pacote-revisao/`. Somente o inventário atual entra no índice. Originais são preservados por hash e não devem ser sobrescritos.

## Curadoria com procedência

As 53 versões derivadas em `03-triagem/correcoes/` estão vinculadas aos hashes do texto e do arquivo original no catálogo `03-triagem/correcoes.json`. `scripts/curar_catalogo.py` gera esse catálogo explícito e recusa reaplicar uma correção a uma fonte alterada. `texto_original` e `curadoria` em `itens.json` permitem conferir a transformação.

Essas correções têm revisão por agente e confiança média. Não representam aprovação humana de todas as páginas. Material incerto, ilegível, de assunto indefinido ou confiança baixa ou não verificada é excluído da busca automática. Blocos sem correção válida continuam pendentes.

Uma aprovação humana deve registrar ID, hash atual do texto e `sha256_fonte` do arquivo original, revisor real, confiabilidade e justificativa em `03-triagem/revisoes.json`, preservando os registros existentes. Use `alta` somente após conferir fonte, enunciado e solução. Textos alterados invalidam a aprovação anterior. Refaça triagem/indexação depois de revisar.

## Repetir a comparação

```bash
./preparar_modelos.sh
./avaliar_modelos.sh
./resumo_validacao.sh
```

A avaliação compara 12 questões em quatro condições: genérico, instruções sem dados, RAG manual e RAG automático. Aplica regras e revisões existentes. Parecer adicional por IA só é ativado com `TUTORON_TRIAGE_AI=1`; não é aprovação do professor. O cache reutiliza chamadas idênticas.

Veja [COMPARACAO_ATUAL.md](06-avaliacao/COMPARACAO_ATUAL.md), `resultados.json` e [revisao-tecnica.json](06-avaliacao/revisao-tecnica.json). Cobertura lexical não equivale a acurácia. As notas dos alunos medem preferência percebida; evidência pedagógica exige revisão por professor e amostra humana suficiente.

Para amostra curta: `python -m acervo avaliar --gerar --questoes Q1,Q2`. Isso substitui o agregado pela amostra; rode sem filtro depois para restaurar os resultados completos via cache.

## Treinar em outra máquina

Padrão local: Qwen2.5 3B, contexto 4096, temperatura 0,2 e seed 42. `tutoron-paa` compartilha os pesos da base e adiciona instruções; RAG fornece contexto na aplicação. Nenhum peso foi ajustado nesta rodada.

O Ryzen 7 3700U tem cerca de 10 GiB de RAM e nenhuma GPU NVIDIA detectada. A receita QLoRA preparada requer GPU CUDA externa:

```bash
./preparar_treino.sh
./treinar_lora.sh --steps 30
```

O primeiro comando prepara 26 exemplos de treino e seis de validação por agente e verifica hashes/famílias. O segundo é para a máquina com GPU. No Windows existem `.bat`; WSL2 pode usar `.sh`. Leia [COMO_TREINAR.md](05-modelo/COMO_TREINAR.md). O ambiente CUDA não foi executado neste notebook; dados e dry-run foram verificados. Famílias do benchmark ficam excluídas do treino. Depois de treinar/exportar/importar, repita benchmark e avaliação cega; loss menor não comprova superioridade.

A implantação pública e o MVP ficam para depois das evidências de qualidade. O servidor local basta para esta validação.

Aprovações em `03-triagem/revisoes.json` exigem `sha256` (texto atual) e `sha256_fonte` (arquivo original), além de revisor, confiabilidade e justificativa. Mudanças no arquivo invalidam o parecer mesmo com OCR idêntico. Votos preservam o hash e snapshot de cada par; resumos não misturam versões.
