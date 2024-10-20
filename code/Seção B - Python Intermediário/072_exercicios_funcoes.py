# Aula: 113. Exercícios com funções + Solução (prepare-se para pausar)

import math

"""
Crie uma função que multiplica todos os argumentos não nomeados recebidos.

Retorne o total para uma variável e mostre o valor da variável.
"""


def multiplica_v1(*args):
    return math.prod(args)


print(multiplica_v1(10, 20, 5))


def multiplica_v2(*args):
    total = 1

    for num in args:
        total = total * num

    return total


print(multiplica_v2(10, 20, 5))

"""
Crie uma função que fala se um número é paraou impar. 

Retorne se ele e par ou impar.
"""


def par_impar(num):
    return "PAR" if num % 2 == 0 else "IMPAR"


print(par_impar(7))
print(par_impar(20))
