# Aula: 107. Valores padrão para parâmetros em funções Python + NoneType e None

"""
Valores padrão para parâmetros

Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
"""


def soma_v1(x, y):
    """
    Realiza a soma de dois números.
    """
    print(f"Se {x=} e {y=} então x + y resulta em {x + y}")


soma_v1(1, 2)
soma_v1(7, 5)


def soma_v2(x, y, z=None):
    """
    Realiza a soma de números
    """
    if z is None:
        print(f"Se {x=} e {y=} então x + y resulta em {x + y}")
    else:
        print(f"Se {x=}, {y=} e {z=} então x + y + z resulta em {x + y + z}")


soma_v2(1, 5, 8)
soma_v2(1, 5, 0)
soma_v2(1, 5)
