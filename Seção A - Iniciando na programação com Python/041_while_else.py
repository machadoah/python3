"""
while / else
"""

string = "AntonioSHenrique"
i = 0

while i < len(string):
    letra = string[i]

    if letra == " ":
        break

    print(letra)
    i += 1
else:
    # só é executado quando o laço for até o fina
    print("O else foi executado\nCódigo não parou em nenhum break")
