texto = "python"

for letra in texto:
    print(letra)

novo_texto = ""
for letra in texto:
    novo_texto += f"*{letra}"
print(novo_texto + "*")
