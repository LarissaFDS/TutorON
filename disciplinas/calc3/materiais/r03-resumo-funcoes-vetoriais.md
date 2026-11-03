---
id: calc3-resumo-funcoes-vetoriais
titulo: Resumos de aula — funções vetoriais: limite, derivada, regras do produto, reta tangente, integral e comprimento de arco no espaço
assunto: calc3-04-funcoes-vetoriais
tipo: material_estudo
resolucao: nao
fonte: "Resumo 4" e "Resumo 5" (página do Notion "Cálculo 3"; manuscritos escaneados). O "Resumo 3" não está na página.
autoria: Resumos manuscritos anexados ao Notion da turma com o rótulo "Resumo do professor" (autoria não confirmada); paráfrase da equipe TutorON
licenca: Não declarada (material de turma); os arquivos não estão no repositório
publicacao_transcricao: não autorizada até agora; o bloco resume com texto próprio
fontes_catalogo: ufal-calc3-notion-resumos
curadoria: aprovado
natureza: material_da_disciplina
verificacao: exemplos_conferidos
status_resolucao: validada
revisao_humana: pendente
---
Resumos 4 e 5 de aula, parafraseados (rótulo "Resumo do professor" no Notion; autoria não confirmada). Status da resolução: validada (fórmulas e exemplos conferidos com SymPy).

Função vetorial $\mathbf{r}(t) = \langle f(t), g(t), h(t) \rangle$. Limite, continuidade, derivada e integral são feitos **componente a componente**: $\mathbf{r}'(t) = \langle f'(t), g'(t), h'(t) \rangle$ (vetor tangente, quando não nulo).

Regras de derivação (u e v funções vetoriais, f escalar):
- $(\mathbf{u} + \mathbf{v})' = \mathbf{u}' + \mathbf{v}'$; $(f\mathbf{u})' = f'\mathbf{u} + f\mathbf{u}'$;
- $(\mathbf{u} \cdot \mathbf{v})' = \mathbf{u}' \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{v}'$ (produto escalar);
- $(\mathbf{u} \times \mathbf{v})' = \mathbf{u}' \times \mathbf{v} + \mathbf{u} \times \mathbf{v}'$ (produto vetorial; a ordem importa);
- regra da cadeia: $\frac{d}{dt}\mathbf{u}(f(t)) = f'(t)\,\mathbf{u}'(f(t))$.
- Se $\mathbf{R}_1' = \mathbf{R}_2'$, então $\mathbf{R}_1 = \mathbf{R}_2 + \mathbf{C}$ (vetor constante). No manuscrito este item e o anterior estão ambos numerados "5".

Reta tangente em $t_0$: $\mathbf{L}(t) = \mathbf{r}(t_0) + t\,\mathbf{r}'(t_0)$. Integral: $\int_a^b \mathbf{r}(t)\,dt = \mathbf{R}(b) - \mathbf{R}(a)$, com $\mathbf{R}' = \mathbf{r}$ (Teorema Fundamental para funções vetoriais).

Comprimento de arco no espaço: $L = \int_a^b \|\mathbf{r}'(t)\|\,dt$; função comprimento de arco $s(t) = \int_a^t \|\mathbf{r}'(u)\|\,du$; velocidade escalar $ds/dt = \|\mathbf{r}'(t)\|$. Reparametrizar pelo comprimento de arco: inverter $s = g(t)$ e usar $\mathbf{r}_1(s) = \mathbf{r}(g^{-1}(s))$, que tem $\|\mathbf{r}_1'(s)\| = 1$. O resumo traz uma figura comparando um vetor velocidade unitário (parametrização por comprimento de arco) com um não unitário.

**Verificação:** a hélice $\langle \cos t, \operatorname{sen} t, t \rangle$ tem $\|\mathbf{r}'\| = \sqrt2$, então $s = \sqrt2\,t$ e $\mathbf{r}_1(s) = \langle \cos(s/\sqrt2), \operatorname{sen}(s/\sqrt2), s/\sqrt2 \rangle$, com velocidade 1.
