# Introdução f-string

nome = 'Antonio'
altura = 1.87837297432

linha_1 = f'{nome} possui {altura:.2f} m de atura'
linha_2 = '{0} possui {1:.2f} m de atura'.format(nome, altura)

print(linha_1)
print(linha_2)