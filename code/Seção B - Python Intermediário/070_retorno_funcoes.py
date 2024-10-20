# Aula: 110. Retorno de valores das funções (return

"""
Retorno de valores das funções (return).
"""


# Imprime meu nome na tela
variavel = print("Antonio")

# Retorno
print(variavel)


def soma(x, y):
    """
    :return: toda função por padrão retorna None
    """
    ...


variavel = int("1")
print(variavel)


def soma_v2(x, y):
    return x + y


print(soma_v2(10, 10))
