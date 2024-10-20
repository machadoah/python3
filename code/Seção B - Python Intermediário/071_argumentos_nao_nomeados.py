# Aula: 111. (Parte 1) *args para quantidade de argumentos não nomeados variáveis
# Aula: 112. (Parte 2) *args para quantidade de argumentos não nomeados variáveis

"""
args - Argumentos não nomeados

* - *args (empacotamento e desempacotamento)
"""


# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4

# 1 2 [3, 4]
print(x, y, resto)


def soma_v1(*args):

    total = 0

    for num in args:
        total += num

    return total


print(soma_v1(1, 2, 3, 4, 5, 6))


def soma_v2(*args):
    return sum(args)


print(soma_v2(1, 2, 3, 4, 5, 6))
