# d455baef2cdf-q3-3

Fonte: materiais\Disponiveis\RAG PAA\PAA_L3.pdf | página(s): 4

3. Escreva um algoritmo de divis˜ao-e-conquista (n log n) para computar an em
que n ´e um inteiro positivo.

Solu¸c˜ao:


[OCR parcial do recorte p4-fig1.png; conferir símbolos na imagem]
long fast_exp(inta,intb)
if(b==θ)return 1;//Caso base,expoente=0
long result =fast_exp(a,b/2);// Computa a~([b']/2) em tog (b'),
result *=result;// Computa a^([b']/2)*a([b']/2),tempoconstante
//ondeb'éoexpoenteparaestesubproblema
if(b&i) result *=a;//Se expoente impar,corrige o resultado
//e.g.:b=3=>a^b=a^3=a*α^2
returnresult;
