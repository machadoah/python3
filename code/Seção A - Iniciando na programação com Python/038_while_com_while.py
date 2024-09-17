qtd_linhas = 5
qtd_colunas = 5

linha_atual = 1
coluna_atual = 1

while linha_atual <= qtd_linhas:
    coluna_atual = 1

    while coluna_atual <= qtd_colunas:
        coluna_atual += 1
        print("x", end="")

    linha_atual += 1
    print("\n", end="")
