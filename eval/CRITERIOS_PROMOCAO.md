# Comparação do candidato treinado

Critérios definidos antes da nova geração em `casos_promocao.json`. São 12 situações de dificuldade e tentativas sintéticas, sem copiar alvos do treino. Os critérios ficam apenas no arquivo de avaliação; não entram na pergunta ao modelo. O mesmo fluxo de busca, publicação e revisão atende ambos os modelos, localmente e sem raciocínio, com temperatura 0,2. A revisão usa o próprio modelo; a decisão exige inspeção separada do texto.

Para promover o candidato nesta bateria exploratória: nenhuma entrega de resultado pedido nem erro técnico claro nas ajudas publicadas; melhora de potencial de ajuda em pelo menos três pares, piora em no máximo um; número de reservas não maior que o atual; nenhum pedido acima de 120 segundos. Exigir também que a comparação anterior de 32 casos por modelo não mostre regressão operacional relevante. Uma falha bloqueia a promoção. Esses limiares são uma regra prática desta entrega, não uma garantia de aprendizagem.

Inspeção técnica: ajuda 0 = não destrava ou contradiz a tentativa; 1 = relevante, mas vaga ou exige salto; 2 = correta, reconhece a tentativa e oferece próximo passo pequeno. Registrar motivo, correção e vazamento em cada modelo. A validação com docente e alunos continua necessária. O conjunto fica fora dos alvos de treino e de escolha de hiperparâmetros.
