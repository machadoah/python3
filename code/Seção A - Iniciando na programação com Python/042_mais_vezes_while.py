frase = """aaaooo""".lower()

i = 0
quantidade_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ""

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == " ":
        i += 1
        continue

    quantas_vezes_apareceu_mais_atual = frase.count(letra_atual)

    if quantidade_apareceu_mais_vezes < quantas_vezes_apareceu_mais_atual:
        quantidade_apareceu_mais_vezes = quantas_vezes_apareceu_mais_atual
        letra_que_apareceu_mais_vezes = letra_atual

    i += 1

print(
    f"A letra que apareceu mais vezes foi '{letra_atual}' e apareceu {quantidade_apareceu_mais_vezes}x"
)
