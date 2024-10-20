# Aula: 106. Argumentos nomeados e argumentos posicionais (não nomeados) em funções

"""
Argumentos nomeados e não nomeados em funções Python

- Argumento nomeado tem nome com sinal de igual.
- Argumento não nomeado recebe apenas o argumento (valor).
"""


def soma_v1(x, y):
    """
    Realiza a soma de dois numeros.
    """
    print(f"Se {x=} e {y=} então x + y é igual a {x + y}.")


# argumentos não nomeados
soma_v1(1, 2)

# argumentos nomeados
soma_v1(y=5, x=3)


def soma_v2(x, y, z):
    """
    Realiza a soma de numeros.
    """
    print(f"Se {x=} e {y=} e {z=} então x + y + z é igual a {x + y + z}.")


# Nesse caso o parametro 'y' foi nomeado, assim todos os seguidos também devem ser.
soma_v2(1, y=3, z=2)
