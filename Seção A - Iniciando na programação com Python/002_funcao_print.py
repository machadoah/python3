#[\r\n] -> quebra de linha padrão CRLF (Windows)
#[\n]   -> quebra de linha padrão LF (Unix)

print(12, 34, sep='-', end='[fim]\n')
print(56, 78, sep='-')
