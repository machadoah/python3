# receba dois valores e traga quem é maior ou menor!

primeiro_numero = input("digite um valor: ")
segundo_numero = input("digite outro valor: ")

if primeiro_numero > segundo_numero:
    print(f"{primeiro_numero=} é maior que {segundo_numero=}")
elif primeiro_numero == segundo_numero:
    print("São iguais!")
else:
    print(f"{segundo_numero=} é maior que {primeiro_numero}")
