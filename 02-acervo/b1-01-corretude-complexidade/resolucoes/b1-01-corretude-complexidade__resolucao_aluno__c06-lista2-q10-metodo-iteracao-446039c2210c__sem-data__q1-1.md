# c06

Fonte: materiais\c06_lista2_q10_metodo_iteracao.md | página(s): não informada na transcrição

Versão derivada corrigida por agente; original SHA-256: f0ab5240d45bb64978c5a1f95d54db4eddfe40ba626d3375c27549c2626eeaab. Não é aprovação do professor.

Método da iteração: T(n)=T(n-1)+n, T(1)=1.
Iterando k vezes, T(n)=T(n-k)+sum(j,n-k+1,n). Para k=n-1 resulta T(n)=1+2+...+n=n(n+1)/2. Assim T(n)=Theta(n^2), e em particular O(n^2). Para n>=1, T(n)<=n^2. Não há necessidade de uma quarta equação não apresentada na transcrição.
