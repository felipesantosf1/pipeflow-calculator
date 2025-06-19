import math

T = 3   # Horas de funcionamento por dia
Q_m3h = 288 # m³/h
Q_m3s = Q_m3h / 3600 # m³/s

#Calculo de diametro de recalque
def Diametro_Recalque():
    # Fórmula ABNT NB-92/66 (resultado em METROS)
    Dr_m = 1.3 * (T / 24) ** (1 / 4) * math.sqrt(Q_m3s)

    Dr_mm = Dr_m * 1000   # metros para milímetros
    Dr_pol = Dr_m / 0.0254 # metros para polegadas

    print("\n=== CÁLCULO TEÓRICO (RECALQUE) ===")
    print(f"- Em metros: {Dr_m:.2f} m")
    print(f"- Em milimetros: {Dr_mm} mm")
    print(f"- Em polegadas: {Dr_pol:.2f} pol")

    return Dr_pol

def Velocidade_Recalque(Dr_pol): 
    Dr_m = Dr_pol * 0.0254  # Conversão de polegadas para metros
    A = math.pi * (Dr_m ** 2) / 4  # Área da seção transversal em m²
    V = Q_m3s / A  # Velocidade em m/s
    
    print(f"\nVelocidade no recalque: {V:.2f} m/s\n")

    # Verificação dos limites 
    if V <= 2.5:
        print("→ Atende ao limite econômico (≤ 2,5 m/s)\n")
    elif V <= 3.0:
        print("→ Ultrapassou o limite econômico, mas está dentro do máximo (≤ 3,0 m/s)\n")
    else:
        print("→ ALERTA: Velocidade acima do limite máximo! Redimensione o diâmetro.\n")
    
# Execução dos cálculos
Dr_pol = Diametro_Recalque()
Velocidade_Recalque(Dr_pol)   