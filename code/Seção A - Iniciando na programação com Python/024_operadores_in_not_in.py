# Operadores in e not in

"""
Strings são iteráveis
 0 1 2 3 4 5 6  <- indices
 A n t o n i o  <- valores
-7-6-5-4-3-2-1  <- indices negativos
"""

nome = 'Antonio'
print(nome[2])
print(nome[-4])
print('nio' in nome)
print('zero' in nome)
print(10 * '-')
print('nio' not in nome)
print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')