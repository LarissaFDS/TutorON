---
id: etica-questoes-ambientais-e-computacao-verde-energia-de-data-centers-pue-lixo-eletronico
titulo: Questões ambientais e computação verde: consumo de energia de data centers e da computação, métrica PUE, lixo eletrônico e ciclo de vida dos equipamentos, obsolescência, boas práticas
assunto: etica-02-tecnologia-e-sociedade
tipo: exercicio
questao: Reavaliação da AB2, questão 1
resolucao: sim
fonte: Reavaliações da AB1 e da AB2 (turmas X e M) e Avaliação Final de Computação, Sociedade e Ética do IC-UFAL, 2020.2 (entregas em maio e junho de 2021)
curso: Ciência da Computação (UFAL), COMP361 Computação, Sociedade e Ética; turmas X e M, semestre 2020.2 (aulas em 2021)
fontes_catalogo: ufal-etica-avaliacoes
autoria: Enunciados das avaliações da disciplina (IC-UFAL; professor não identificado nos arquivos); orientação da equipe TutorON
licenca: Não declarada; paráfrase, arquivos não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Computação, Sociedade e Ética (IC-UFAL, 2020.2), Reavaliação da AB2, questão 1 (parafraseado). Status da resolução: validada. A orientação é da equipe TutorON e não é gabarito do professor.

As avaliações são **trabalhos escritos avaliados**: aqui vão o método, um roteiro e pontos de discussão, não o texto pronto.

**Computação verde:** projetar, usar e descartar computadores e sistemas reduzindo o impacto ambiental.

**Eixos para o desenvolvimento:**
- **Energia:** data centers, redes e dispositivos consomem eletricidade e precisam de refrigeração. O impacto depende da **fonte** de energia (matriz elétrica), não só da quantidade.
  - **PUE** (*Power Usage Effectiveness*): $\text{PUE} = \dfrac{\text{energia total do data center}}{\text{energia dos equipamentos de TI}}$. Em palavras: quanto do consumo vai para algo além de computar (refrigeração, perdas). O ideal é 1. Um PUE de 1,5 quer dizer que, para cada 1 kWh de TI, gasta-se 0,5 kWh a mais.
- **Software eficiente:** algoritmos e código que fazem menos trabalho gastam menos energia. Entram aqui o treino de grandes modelos de IA, a mineração de criptomoedas e o *streaming* em alta resolução.
- **Lixo eletrônico (*e-lixo*):** metais pesados e baixa taxa de reciclagem. No Brasil, a Política Nacional de Resíduos Sólidos (Lei 12.305/2010) prevê a logística reversa de eletroeletrônicos.
- **Ciclo de vida e obsolescência:** a fabricação também consome energia e recursos, e a vida útil curta aumenta o impacto. Discuta a obsolescência programada e o direito ao reparo.
- **Boas práticas:**
  - virtualização e consolidação de servidores;
  - desligar o que está ocioso;
  - escolher região de nuvem com energia renovável;
  - prolongar o uso dos equipamentos;
  - descarte correto.

**Posições divergentes:** a TI também **reduz** emissões (viagens trocadas por videoconferência, otimização de logística), o chamado efeito habilitador. Alguns autores alertam para o **efeito rebote**: eficiência maior estimula mais uso. Mostre os dois.

**Verificação:** `test_pue` calcula o PUE de um exemplo (1 500 kWh no total, 1 000 kWh de TI, PUE 1,5) e confere que o PUE nunca é menor que 1.
