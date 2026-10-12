"""Sanidade dos regex do checklist com textos sintéticos (não são respostas do Gemini)."""
import json
from run_demo import avaliar_checkpoints
Q = {q["id"]: q for q in json.load(open("questoes.json", encoding="utf-8"))}

casos = {
 "Q1": ("""O algoritmo retorna o **maior elemento** do vetor. Prova por **indução forte** no tamanho do subvetor
$n = fim - inicio + 1$. **Caso base:** se $inicio = fim$, retorna $A[inicio]$.
**Hipótese de indução:** X funciona para todo $k < n$. **Passo indutivo:** as metades têm tamanho
estritamente menor que $n$; na linha 8 compara $a < b$ e retorna o maior.""", 7),
 "Q2": ("""Seja $A(n)$ o número de asteriscos. Recorrência: $A(0) = 0$ e $A(n) = 2\\cdot A(n-1) + n$.
Desenvolvendo: ... logo $A(n) = 2^{n+1} - n - 2$. Conferindo: A(4) = 26. Número exato.""", 6),
 "Q2b": ("""$$T(n) = 2T(n - 1) + n,\\quad T(0)=0$$ Expandindo a recorrência obtemos
$T(n) = 2^{n+1} - (n+2)$; para n=3 temos 11 asteriscos.""", 6),
 "Q3": ("""O tamanho da entrada é o número de bits $b = \\log_2 n$, logo $n = 2^b$ e o tempo é exponencial em b:
o algoritmo é **pseudo-polinomial**. (Aliás, pelo AKS, PRIMES está em P.)""", 4),
 "Q4": ("""**P**: problemas de decisão resolvidos em tempo polinomial. **NP**: um certificado para SIM pode ser verificado
em tempo polinomial. $P \\subseteq NP$. **NP-completo**: está em NP e todo problema de NP se reduz polinomialmente a ele.
Atenção: o material [c09] diz que NP são problemas em que ninguém conseguiu comprovar se são polinomiais, o que é impreciso.""", 6),
}
falhou = False
for k, (txt, esperado) in casos.items():
    r = avaliar_checkpoints(Q[k[:2]], txt, "estruturado")
    ok = sum(1 for c in r if c["tipo"] != "info" and c["ok"])
    faltando = [c["rotulo"] for c in r if c["tipo"] != "info" and not c["ok"]]
    print(f"{k}: {ok}/{esperado}", "OK" if ok == esperado else f"FALTOU {faltando}")
    falhou |= ok != esperado
# o erro do material deve ser detectado quando repetido sem ressalva
r = avaliar_checkpoints(Q["Q4"], "NP inclui os problemas em que ninguém conseguiu até hoje comprovar se são polinomiais.", "generico")
print("Q4 detecta cópia do erro:", [c["ok"] for c in r if c["tipo"] == "nao_deve"] == [False])
