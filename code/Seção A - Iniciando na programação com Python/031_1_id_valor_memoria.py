"""
Flag (Bandeira) - Marcar um local
None = Não valor

is e is not = é ou não é (tipo, valor, identidade)
id = IDENTIDADE
"""

# ambas variáveis apostam para o mesmo local da memória

v1 = "a"
v2 = "a"
print(id(v1))  # valor igual a v2
print(id(v2))  # valor igual a v1
