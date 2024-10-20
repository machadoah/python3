# Aula: 114. Higher Order Functions - Funções de primeira classe

"""
Higher Order Functions

Funções de primeira classe

Termos técnicos: 

Higher Order Functions e First-Class Functions

Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.
"""


def saudacao(msg, nome):
    return f"{msg}, {nome}"


def executa(funcao, *args):
    return funcao(*args)


saudacao_v2 = saudacao

v = executa(saudacao_v2, "Bom dia", "Antonio")

print(v)
