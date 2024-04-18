adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 2        # o retorno é sempre float
print('Divisão', divisao)

divisao_inteira = 10 // 2
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciacao', exponenciacao)

modulo = 55 % 2         # resto da divisão
print('Módulo', modulo)

"""
módulo é utilizado por exemplo, para saber se um nº é para ou impar!

    se n for multiplo de 2 é par!
"""

numero = 932839793274732

print(f' {numero} é par ou impar?')

print('é par!' if numero % 2 == 0 else 'False')
