# Aula: 108. (Parte 1) Escopo de funções e módulos em Python + global

"""
Escopo de funções em Python

Escopo significa o local onde aquele código pode atingir.

Existe o escopo global e local:
- O escopo global é aquele onde todo o código é alcançavel.
- O escopo local é aquele onde apenas nome do mesmo local podem ser alcançados.
"""

# incio do escopo local do módulo


def escopo_v1():
    # inicio do escopo da função 'escopo_v1'
    x = 1
    print(x)
    # fim do escopo da função 'escopo_v1'


# retornara 1
escopo_v1()

# print(x) -> NameError: name 'x' is not defined


# x do módulo
x = 5


def escopo_v2():
    global x  # define que o x usado aqui será o global
    x = 10

    def funcao_interna():
        x = 11
        y = 2
        print(x, y)

    funcao_interna()
    print(x)


escopo_v2()

# imprime o x do módulo, pois está fora da função.
print(x)


# fim do escopo local do módulo
