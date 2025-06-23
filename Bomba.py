# Função para calcular o somatório dos valores de K multiplicados pela quantidade de componentes
def calcular_K(componentes):
    total_K = 0  # Inicializa a variável para acumular o K total
    for nome, (qtd, k_unit) in componentes.items():  # Itera sobre os componentes: nome, quantidade e K unitário
        total_K += qtd * k_unit  # Soma o K total: quantidade vezes o K unitário
    return total_K  # Retorna o K total do conjunto de componentes

# Função para calcular a perda de carga localizada na sucção e no recalque
def perda_localizada(vr):
    g = 9.81  # Aceleração da gravidade (m/s²)

    # Dicionário com os componentes da linha de recalque e seus respectivos valores de (quantidade, K)
    componentes_recalque = {
        "joelho_90_raio_curto": (3, 6.4),
        "valvula_retenção": (1, 25.0),
        "registro_gaveta": (1, 1.4)
    }

    # Cálculo do K total na linha de recalque
    K_r = calcular_K(componentes_recalque)

    # Cálculo da perda localizada no recalque (hlr = K*v²/(2g))
    hlr = K_r * (vr ** 2) / (2 * g)

    # Exibe os resultados formatados com 4 casas decimais
    print(f"Perda localizada no recalque (hlr): {hlr:.4f} m")

    # Retorna as perdas como uma tupla
    return hlr

def perda_distribuida(L, D, v, f):
    # L = comprimento (m), D = diâmetro (m), v = velocidade (m/s), f = fator de atrito (adimensional)
    g = 9.81
    return f * (L / D) * (v**2 / (2 * g))  # em metros

def calculo_principal():
    altura_recalque = 14.90        # m
    comprimento_recalque = 20.90   # m
    Dr_m = 0.23493652093855966     # m (exemplo do cano de recalque)
    vr = 1.845436215937695         # m/s
    
    # 2) Altura geométrica
    Hg = altura_recalque

    # 3) Perdas localizadas
    P_r_loc = perda_localizada(vr)

    # 4) Perdas distribuídas (exemplo com f fixo)
    f = 0.02  # valor típico
    P_r_dist = perda_distribuida(comprimento_recalque, Dr_m, vr, f)

    # 5) Altura Manométrica Total
    Hm = Hg + P_r_loc + P_r_dist

    # 6) Resultado
    print(f"\nAltura Geométrica (Hg): {Hg:.2f} m\n")
    print(f"Perda localizada recalque: {P_r_loc:.2f} m")
    print(f"Perda distribuída recalque: {P_r_dist:.2f} m")
    print(f"\n>>> Altura Manométrica Total (Hm): {Hm:.2f} m\n")

calculo_principal()
    
    