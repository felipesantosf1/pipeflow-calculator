import math  # Importa o módulo 'math' para usar funções matemáticas como sqrt e pi.

# Função para converter diferentes unidades de vazão para m³/s
def calcular_vazao(Q_valor, unidade='m³/h'):
    if unidade == 'm³/s':
        return Q_valor  # Se já estiver em m³/s, retorna o valor direto
    elif unidade == 'm³/h':
        return Q_valor / 3600  # Converte m³/h para m³/s
    elif unidade == 'L/s':
        return Q_valor / 1000  # Converte L/s para m³/s
    else:
        raise ValueError("Unidade de vazão inválida.")  # Erro se a unidade for desconhecida

# Função para calcular o diâmetro de recalque (tubulação) com base na vazão e no tempo de funcionamento
def calcular_diametro_recalque(Q_m3s, T):
    Dr_m = 1.3 * (T / 24) ** (1 / 4) * math.sqrt(Q_m3s)  # Fórmula empírica para diâmetro em metros
    Dr_mm = Dr_m * 1000  # Converte para milímetros
    Dr_pol = Dr_m / 0.0254  # Converte para polegadas (1 pol = 0,0254 m)
    return Dr_m, Dr_mm, Dr_pol  # Retorna todas as formas

# Função para calcular a velocidade do fluido na tubulação
def calcular_velocidade(Q_m3s, Dr_pol):
    Dr_m = Dr_pol * 0.0254  # Converte polegadas para metros
    A = math.pi * (Dr_m ** 2) / 4  # Área da seção transversal do tubo (A = πd²/4)
    V = Q_m3s / A  # Velocidade = Vazão / Área
    return V  # Retorna velocidade em m/s

# Função para verificar se a velocidade está dentro dos limites recomendados
def verificar_limite_velocidade(V, limite_eco=2.5, limite_max=3.0):
    if V <= limite_eco:
        return f"→ Atende ao limite econômico (≤ {limite_eco:.1f} m/s)\n"
    elif V <= limite_max:
        return f"→ Ultrapassou o limite econômico, mas está dentro do máximo (≤ {limite_eco:.1f} m/s)\n"
    else:
        return "→ ⚠️ Velocidade acima do limite máximo! Redimensione o diâmetro.\n"

# Função principal para exibir os resultados de cálculo
def exibir_resultados(Q_valor, unidade, T):
    Q_m3s = calcular_vazao(Q_valor, unidade)  # Converte vazão para m³/s
    Dr_m, Dr_mm, Dr_pol = calcular_diametro_recalque(Q_m3s, T)  # Calcula diâmetro
    V = calcular_velocidade(Q_m3s, Dr_pol)  # Calcula velocidade
    mensagem_limite = verificar_limite_velocidade(V)  # Verifica limites da velocidade

    # Impressão dos resultados no terminal
    print("\n=== CÁLCULO TEÓRICO (RECALQUE) ===")
    print(f"Vazão: {Q_valor} {unidade}")
    print(f"Tempo de funcionamento: {T} h/dia")
    print(f"\nDiâmetro de recalque:")
    print(f"- Em metros: {Dr_m:.2f} m")
    print(f"- Em milímetros: {Dr_mm:.2f} mm")
    print(f"- Em polegadas: {Dr_pol:.2f} pol")
    print(f"\nVelocidade no recalque: {V:.2f} m/s")
    print(mensagem_limite)

# Bloco de execução principal
if __name__ == "__main__":
    # Parâmetros de entrada definidos manualmente
    Q_valor = 288         # Valor da vazão (por exemplo, 288 m³/h)
    unidade = 'm³/h'      # Unidade da vazão ('m³/s', 'm³/h' ou 'L/s')
    T = 3                 # Tempo de funcionamento diário (em horas)

    exibir_resultados(Q_valor, unidade, T)  # Chama a função que mostra os resultados

