# Precedencia de operadores matemáticos

"""
1º parenteses                                       ->  (n + n)
2º potenciação                                      ->  **
3º multiplicação, divisão, divisão inteira, módulo  ->  / // %
4º adição e subtração                               ->  + -
"""

conta_1 = 1 + 1 ** 5 + 5
#         1 +   1    + 5
#            2       + 5
#               [7] 🎉

print(conta_1)

