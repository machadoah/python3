"""
Calculadora com while
"""

while True:
    numero_1 = input("Digite o primeiro número: ")
    numero_2 = input("Digite o segundo número: ")
    operador = input("Digite o operador\n(+) ou (-) ou (*) ou (/): ")

    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)

        match operador:
            case "+":
                print(numero_1 + numero_2)
            case "-":
                print(numero_1 - numero_2)
            case "*":
                print(numero_1 * numero_2)
            case "/":
                print(numero_1 / numero_2)
    except Exception as error:
        print(error)

    sair = input("Quer sair? \n[s]im / [n]ão: ").lower().startswith("s")

    if sair is True:
        break
