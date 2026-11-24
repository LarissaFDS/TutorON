---
id: calc2-lista4-integracao-por-partes
titulo: Lista 4 (Profa. Xu Yang) — integração por partes: x cos x, ln √x, x⁴ ln x, (x² + 1)e^(−x), sen x · ln(cos x), x e^(−x) e e^(√x)
assunto: calc2-01-integracao-por-partes
tipo: exercicio_resolvido
resolucao: sim
fonte: Lista 4 de Cálculo 2 (Profa. Xu Yang, UFAL), imagem do material do 2º período de Engenharia de Computação | enunciados parafraseados
curso: Engenharia de Computação (UFAL), ECOM010 Cálculo 2, 2º período; semestre não identificado
fontes_catalogo: ufal-xu-yang-calc2-listas
autoria: Enunciados da lista da Profa. Xu Yang; resoluções da equipe TutorON com apoio de IA, conferidas com SymPy
licenca: Não declarada (lista da disciplina; imagem não versionada)
publicacao_transcricao: não autorizada; enunciados parafraseados
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Cálculo 2, Lista 4 (integração por partes). Status da resolução: validada. A resolução é da equipe TutorON e não é gabarito do professor.

**Regra:** $\int u\,dv = uv - \int v\,du$. Escolha para $u$ o que simplifica ao derivar (logaritmo, potência de $x$) e para $dv$ o que se integra fácil (exponencial, seno, cosseno).

- $\int x\cos x\,dx$: $u = x$, $dv = \cos x\,dx$. Resultado $x\,\text{sen}\,x + \cos x + C$.
- $\int \ln\sqrt{x}\,dx$: como $\ln\sqrt{x} = \tfrac12\ln x$, faça $u = \ln x$, $dv = dx$: $\tfrac{x}{2}(\ln x - 1) + C$.
- $\int x^4\ln x\,dx$: $u = \ln x$, $dv = x^4dx$: $\tfrac{x^5}{25}(5\ln x - 1) + C$.
- $\int_0^1 (x^2+1)e^{-x}dx$: partes duas vezes (o polinômio desce de grau): $3 - \tfrac{6}{e}$.
- $\int_0^{\pi/3} \text{sen}\,x\,\ln(\cos x)\,dx$: troque $w = \cos x$ e depois partes em $\int \ln w\,dw$: $\tfrac{\ln 2}{2} - \tfrac12$ (negativo, porque $\ln(\cos x) < 0$ no intervalo).
- $\int_1^5 x e^{-x}dx$: $2e^{-1} - 6e^{-5}$.
- $\int e^{\sqrt{x}}dx$: troque $x = t^2$ ($dx = 2t\,dt$) e depois partes: $2(\sqrt{x} - 1)e^{\sqrt{x}} + C$.

Erros comuns: esquecer o sinal de $-\int v\,du$; escolher $u = e^x$ em $\int x e^x dx$ (a integral piora); esquecer de trocar os limites numa substituição.

**Verificação:** derive cada primitiva e compare com o integrando; as definidas foram calculadas com SymPy em `test_lista4_partes`.
