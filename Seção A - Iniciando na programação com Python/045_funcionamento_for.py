"""
Iterável    ->  str, range, etc (__iter__)
Iterador    ->  quem sabe entregar uma coisa por vez
next        ->  me entregue o próximo valor
iter        ->  me entregue seu iterador
"""

texto = "Antonio"

# torna um iterável a variavel texto
texto = texto.__iter__()

# printa o iterator
print(texto)

while True:
    try:
        # printa os valores que são iteraveis
        print(next(texto))
        print(next(texto))
        print(next(texto))
        print(next(texto))
        print(next(texto))
        print(next(texto))
        print(next(texto))
        print(next(texto))
    except StopIteration:
        break
