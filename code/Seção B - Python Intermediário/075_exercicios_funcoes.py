# Aula: 117. Exercício com funções

"""
Exercicios

Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.
"""


def multiplica(multiplicador):

    def executa(numero):
        return numero * multiplicador

    return executa


duplica = multiplica(2)
triplica = multiplica(3)
quadruplica = multiplica(4)


print(duplica(2))
print(triplica(2))
print(quadruplica(2))
