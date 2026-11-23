---
id: cd-perceptron-versus-svm-margem-maxima-kernel-redes-neurais-parametros
titulo: Perceptron × Máquina de Vetores de Suporte (SVM): problemas em comum e vantagem do SVM (margem máxima, kernel); otimizar parâmetros do SVM; parâmetros de uma rede neural e passo a passo para configurá-la (exemplo COVID)
assunto: cd-03-metodos
tipo: prova
questao: AB2 2020.1 Q3; REAV 2 2020.1 Q3; AB2 2020.2 Q3; REAV AB2 2020.2 Q2; Lista 2 Q3
resolucao: sim
fonte: Provas e listas de Ciência de Dados do Prof. Bruno Pimentel (IC-UFAL)
curso: Ciência da Computação (UFAL), ênfase Sistemas Inteligentes, Ciência de Dados (COMP401); turmas 2020.1, 2020.2 e 2021.1
fontes_catalogo: ufal-pimentel-provas-cd
autoria: Questões do Prof. Bruno Pimentel (IC-UFAL); resolução da equipe TutorON
licenca: Não declarada (prova); paráfrase, PDFs não versionados
publicacao_transcricao: não autorizada; o bloco traz paráfrase
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Ciência de Dados, Prof. Bruno Pimentel (UFAL), AB2 2020.1 Q3; REAV 2 2020.1 Q3; AB2 2020.2 Q3; REAV AB2 2020.2 Q2; Lista 2 Q3 (enunciados parafraseados). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Em comum:** perceptron de camada única e SVM linear são **classificadores binários lineares**: separam as classes por um hiperplano $w \cdot x + b = 0$.

**Vantagem do SVM:**
- o perceptron para em **qualquer** hiperplano que separe o treino e **não converge** se os dados não forem linearmente separáveis;
- o SVM escolhe o hiperplano de **margem máxima** (maior distância aos pontos mais próximos, os **vetores de suporte**), que tende a **generalizar melhor**; com **margem suave** (parâmetro $C$) tolera erros; com o **truque do kernel** (RBF, polinomial) separa classes **não lineares**, como o XOR.

**Otimizar parâmetros do SVM** ($C$, tipo de kernel, $\gamma$ do RBF):
1. **busca em grade** (*grid search*) com validação cruzada, em escala logarítmica ($C \in \{0{,}1, 1, 10, 100\}$);
2. **busca aleatória**, mais eficiente com muitos parâmetros.
Sempre **normalize** os atributos antes.

**Parâmetros de uma rede neural:**
- **número de camadas escondidas** (e de neurônios): mais camadas captam relações mais complexas, mas aumentam o risco de overfitting e o custo;
- **função de ativação** (sigmoide, tanh, **ReLU**): dá a não linearidade; ReLU evita o desaparecimento do gradiente em redes profundas;
- **taxa de aprendizagem:** tamanho do passo do gradiente; alta demais diverge ou oscila, baixa demais é lenta e fica presa.

**Passo a passo (diagnóstico de COVID com dados de pacientes):** limpar e normalizar; separar um teste estratificado; escolher a métrica (**cobertura** alta, pois um falso negativo é grave, e F1); buscar arquitetura, ativação, taxa e regularização com **k-fold estratificado**; usar parada antecipada; medir uma vez no teste.

**Verificação:** `test_svm_e_perceptron` mostra no scikit-learn que, em círculos concêntricos, o `Perceptron` fica perto de 50% e o SVM com kernel RBF passa de 95%, e que a `GridSearchCV` escolhe $C$ e $\gamma$ por validação cruzada.
