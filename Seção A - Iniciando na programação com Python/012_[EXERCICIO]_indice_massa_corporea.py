# IMC
"""
PESO / ALTURA * ALTURA
"""

nome = 'Antonio Henrique'
altura = 1.76
peso = 87
# imc = ...
imc = peso / (altura ** 2)

print(f"""
      {nome} tem {altura} de altura,
      pesa {peso} quilos e seu IMC é
      {imc:.2f}
      """) 
