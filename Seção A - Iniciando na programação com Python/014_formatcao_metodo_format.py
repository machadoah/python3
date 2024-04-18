a = 'A'
b = 'B'
c = 1.1

formato = 'a={}\t ---\t b={}\t ---\t c={:.2f}'.format(a, b, c)
print(formato)

formato = 'a={0}\t ---\t b={2:.2f}\t ---\t c={1}'.format(a, b, c)
print(formato)

formato = 'a={nome2}\t ---\t b={nome:.2f}\t ---\t c={nome1}'.format(nome1 = a, nome2 = b, nome = c)
print(formato)
