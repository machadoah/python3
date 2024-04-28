contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        # continue pula a execusão do código quando contador for 6
        continue

    print(contador)

    if contador == 40:
        break

print("Acabou!")
