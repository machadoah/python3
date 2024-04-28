"""
Iterando strings com while
"""

nome = "Antonio Henrique Machado"

indice = 0
fim_string = len(nome)
new_string = ""

while indice < fim_string:
    new_string += nome[indice].upper()
    indice += 1
print(new_string)

indice = 0
new_string = ""

while indice < fim_string:
    new_string += "*" + nome[indice]
    indice += 1
print(new_string + "*")
