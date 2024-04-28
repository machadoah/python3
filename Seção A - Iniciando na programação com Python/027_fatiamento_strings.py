# Fatiamento de strings

"""
    0123456789
    Olá mundo!
   -9876543210

Fatiamento [inicio:fim:passo] [::]
"""

# Obs.: a função len retorna a quantidade de catacteres da str

variavel = "Olá mundo!"
print(variavel[4:])
print(variavel[:5])

# quantos caracteres possui a valor da variável?
print(len(variavel))
print(variavel[0 : len(variavel) : 1])

# inverter
print(variavel[::-1])
print(variavel[-1:-11:-1])
