---
id: sd-nota-vhdl
titulo: Nota — VHDL sintetizável: entidade, arquitetura, processos, registrador e FSM em dois processos
assunto: sd-11-hdl-vhdl
tipo: material_estudo
resolucao: sim
fonte: Nota da equipe TutorON (não é material do professor)
fontes_catalogo: free-range-vhdl,sim-digital-hneemann
autoria: Equipe TutorON, redigida com auxílio de IA; revisada pela responsável pela curadoria em 21/10/2026
licenca: Texto original da equipe TutorON
curadoria: aprovado
natureza: nota_da_equipe_ia
verificacao: nao_verificada
revisao_humana: feita
revisao_humana_em: 2026-10-21
revisao_humana_por: responsável pela curadoria (revisão interna; não é aprovação do professor)
---
VHDL para Sistemas Digitais (o essencial para as provas)

Estrutura: library ieee; use ieee.std_logic_1164.all; use ieee.numeric_std.all; a entity declara as portas (in/out, std_logic ou std_logic_vector(n−1 downto 0)) e a architecture descreve o comportamento.

Combinacional:
- Atribuição concorrente: y <= a and b; s <= a xor b xor cin;
- MUX: y <= i1 when sel = '1' else i0;  ou with sel select y <= i0 when "00", i1 when "01", i2 when others;
- Em process combinacional, ponha todas as entradas na lista de sensibilidade (ou use process(all) no VHDL-2008) e atribua todas as saídas em todos os caminhos; senão o sintetizador cria latches indesejados.

Registrador (vira flip-flops):
process(clk, rst) begin
  if rst = '1' then q <= (others => '0');
  elsif rising_edge(clk) then
    if ld = '1' then q <= d; end if;
  end if;
end process;

Soma: s <= std_logic_vector(unsigned(a) + unsigned(b)); para obter o vai-um, estenda para n + 1 bits antes de somar.

FSM em dois processos:
type estado_t is (S0, S1, S2); signal estado, prox : estado_t;
- Processo síncrono: if rst = '1' then estado <= S0; elsif rising_edge(clk) then estado <= prox; end if;
- Processo combinacional, process(estado, entradas): prox <= estado; saídas com valor padrão '0'; case estado is when S0 => if comece = '1' then prox <= S1; end if; … end case;
Saídas de Moore calculadas nesse processo combinacional aparecem no mesmo ciclo do estado. Se forem atribuídas dentro de rising_edge, ficam registradas e saem um ciclo depois.

Simulação: um testbench gera clock (clk <= not clk after 5 ns) e estímulos; ferramentas como GHDL ou o simulador Digital permitem testar antes de sintetizar.
