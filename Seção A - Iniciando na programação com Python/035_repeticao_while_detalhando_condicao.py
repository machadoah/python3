"""
Repetições
While (enquanto)

Executa uma ação enquanto uma condição for verdadeira
"""

import time


contador = 0
tempo_inicio = time.time()

while True:
    contador += 1
    print(f"EITA - {contador} ª vez")

    if contador == 10000:
        tempo_fim = time.time()
        break

print(f"o tempo total foi de {(tempo_fim - tempo_inicio):.2f} segundos")

print("Acabou")
