"""
Exercicio 01)
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input("digite um numero inteiro: ")

if numero.isdigit():
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print("O número é par")
    else:
        print("O número é impar")
else:
    print("o número digitado não foi um número intero!")
