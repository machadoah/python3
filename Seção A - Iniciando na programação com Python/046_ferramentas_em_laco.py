for i in range(10):
    if i == 2:
        print("i é 2 PULA!")
        continue

    if i == 8:
        print("fim do código, o else não é executado!")
        break

    for j in range(1, 3):
        print(i, j)

else:
    print("for completo!")
