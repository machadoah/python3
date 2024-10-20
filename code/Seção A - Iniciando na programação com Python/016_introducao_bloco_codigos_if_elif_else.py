# if / elif/ else

entrada = input(
    'Você quer entrar no sistema?\nDigite "s" para sair e "e" para entrar!: '
)

if entrada == "e":
    print("Você entrou no sistema")
    print("📎")
elif entrada == "s":
    print("Você saiu do sistema")
else:
    print("Você não digitou nem entrar nem sair")
