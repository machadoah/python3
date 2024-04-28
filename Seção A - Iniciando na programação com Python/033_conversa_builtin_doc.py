"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = "Antonio Henrique"
# trocando 'o' por 'blit'
outra_variavel = f"{string[:6]}blit{string[7:]}"
print(string)
print(outra_variavel)

print(string.zfill(30))
