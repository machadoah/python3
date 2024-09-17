# Interpolação básica de strings

"""
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = "Antonio "
preco = 1000.95897643
variavel = "%s, o preço é R$%.2f" % (nome, preco)
print(variavel)


# convertendo em hexadecimal
print("O hexadecimal de %d é %08X" % (1500, 1500))

"""
Conversão para hexadecimal:

    10:X -> terá como retorno 10 em Hexademal, ou seja A!
"""

print("o henxadecimal de %d é %X" % (10, 10))

print("%X" % (15))
print(f"O hexadecimal de 27 é {27:08X}")
