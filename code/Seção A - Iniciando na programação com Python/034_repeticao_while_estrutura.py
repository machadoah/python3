"""
Repetições
While (enquanto)

Executa uma ação enquanto uma condição for verdadeira
"""

condicao = True
vezes = 0

while condicao:
    print(1)
    print(2)
    print(3)
    vezes += 1
    # condicao = True if vezes <= 10 else False
    if vezes == 10:
        break
