"""
CONSTANTE = São 'variáveis' que não vão mudar

    Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61  # velocidade atual do carro
local_carro = 101  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # a distância onde o radar pega

velocidade_carro_passou_velocidade_radar_1 = velocidade > RADAR_1
range_radar_min = LOCAL_1 - RADAR_RANGE
range_radar_max = LOCAL_1 + RADAR_RANGE
delta_radar = local_carro >= range_radar_min and local_carro <= range_radar_max

if velocidade_carro_passou_velocidade_radar_1:
    print("O carro passou a velocidade permitida no radar")

if velocidade_carro_passou_velocidade_radar_1 and delta_radar:
    print("O carro foi multado")
