---
id: projsw-padroes-criacao-factory-builder-singleton
titulo: Padrões de criação — Factory Method (conta corrente ou poupança), Builder (pedido montado passo a passo e validado) e Singleton (uma só configuração)
assunto: projsw-05-regras-de-projeto
tipo: notas
questao: projeto 2 (aplicação bancária) e pedidos do comércio eletrônico
resolucao: sim
fonte: Lista de projetos de software orientado a objetos usada no 4º período de Engenharia de Computação (Software_Projects.pdf, IC-UFAL), com o tópico de padrões de projeto da disciplina
curso: Engenharia de Computação (UFAL), Engenharia de Software (ECOM021) / Projeto de Software, 4º período
fontes_catalogo: ufal-ecom-lista-projetos-oo
autoria: Lista de projetos da disciplina (autor não identificado no arquivo), citada em paráfrase; explicação e código Java da equipe TutorON
licenca: Não declarada (lista da disciplina); paráfrase, PDF não versionado; código próprio
publicacao_transcricao: não autorizada; o bloco traz paráfrase e código próprio
curadoria: aprovado
natureza: material_da_disciplina
verificacao: conferida_por_codigo
status_resolucao: validada
revisao_humana: pendente
---
Lista de projetos de Projeto/Engenharia de Software do 4º período de Engenharia de Computação (IC-UFAL), projeto 2 (aplicação bancária) e pedidos do comércio eletrônico. Status da resolução: validada. A explicação e o código são da equipe TutorON e não é gabarito do professor; o código está em `tests_acervo/projsw_java/criacao` e é compilado e executado no teste.

Os três escondem **como** um objeto é criado, cada um por um motivo.

**Factory Method:** o cliente pede um tipo abstrato e o método escolhe a classe concreta, então o cliente não usa `new Poupanca()`. Na aplicação bancária, `Conta c = criarConta("poupanca")` devolve uma `Poupanca`; tipo desconhecido gera `IllegalArgumentException`. Uma conta nova muda só a fábrica.

**Builder:** para objetos com muitos campos opcionais, em vez de construtores com dez parâmetros:
```java
Pedido p = new Pedido.Builder().cliente("Ana").itens(3).presente().build();
```
O construtor de `Pedido` é privado e `build()` valida: sem cliente, lança `IllegalStateException("pedido invalido")`. Campos não informados ficam com o padrão (`itens = 1`, `presente = false`). O objeto pronto pode ter campos `final` (imutável).

**Singleton:** uma só instância (configuração, registro):
```java
static final class Configuracao {
    private static final Configuracao UNICA = new Configuracao();
    private Configuracao() { }
    static Configuracao instancia() { return UNICA; }
}
```
`instancia() == instancia()` dá `true`. Cuidado: Singleton é estado global, dificulta testes e esconde dependências; prefira passar o objeto quando der.

**Verificação:** `test_padroes_de_criacao` compila e roda o exemplo e confere a saída.
