# Aula: 116. Closure e funções que retornam outras funções

"""
Closure e funções que retornam outras funções.
"""


def criar_saudacao(saudacao):

    def saudar(nome):
        return f"{saudacao}, {nome}!"

    return saudar


s1 = criar_saudacao("Bom dia")
s2 = criar_saudacao("Bom noite")

print(s1)
print(s2)
# <function criar_saudacao.<locals>.saudar at 0x7f4f448cf380>
# <function criar_saudacao.<locals>.saudar at 0x7f4f448cf420>

print(s1("Antonio"))
print(s2("Isadora"))
# Bom dia, Antonio!
# Bom noite, Isadora!
