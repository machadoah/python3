# Aula: 105. "def" define uma função personalizada - Introdução às funções em Python

"""
Introdução às fuinções (def) em Python

Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e retomar um valor específico.

Por padrão, funções Python retornam None (nada).

"""


def Print_v1():
    print("Várias")


# Imprimindo Várias 3x
Print_v1()
Print_v1()
Print_v1()


def imprimir(a, b, c):
    print("Eu")


# imprimir()
# TypeError: imprimir() missing 3 required positional arguments: 'a', 'b', and 'c'

# Sendo assim, os parametros que uma função possui, devem ser obrigatoriamente passados!

imprimir(1, 2, 3)


def saudacao(nome="Sem nome"):
    # Sem nome representa o valor padrão
    print(f"Olá, {nome}")


saudacao("Antonio")

# Posso chamar sem nenhum argumento, pois existe uma valor padrão definido.
saudacao()
