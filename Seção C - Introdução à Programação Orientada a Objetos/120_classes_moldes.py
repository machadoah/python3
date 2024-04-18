# class - Classes são moldes para criar novos objetos

"""
As classes geram novos objetos (instâncias) que  podem ter seus próprios atributos e métodos.

Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.

Por convenção, usamos PascalCase para nomes de classes.
"""

# string = 'Antonio'

# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    
p1 = Pessoa('Antonio', 'Macahdo')
print(f'p1 possui {p1.nome=} e {p1.sobrenome=}')

p2 = Pessoa('Isadora', 'Souza')
print(f'p2 possui {p2.nome=} e {p2.sobrenome=}')
