# Aula: 109. (Parte 2) Escopo de funções e módulos em Python + global

"""
Escopo de funções em Python

Escopo significa o local onde aquele código pode atingir.

Existe o escopo global e local:
- O escopo global é aquele onde todo o código é alcançavel.
- O escopo local é aquele onde apenas nome do mesmo local podem ser alcançados.

Não temos acesso nomes de escopos internos nos escopos externos.

A palavra 'global' faz uma variável do escopo externo ser a mesma no escopo interno.
"""


def get_idade(idade: int = None) -> str:
    if idade >= 18:
        return "Maior de idade"

    if idade >= 0 and idade < 18:
        return "Menor de idade"


def get_nome_torcedor(time: str = None) -> str:
    times = {
        "São Paulo": "são paulino",
        "Santos": "santista",
        "Palmeiras": "palmeirense",
        "Corinthians": "corintiano",
    }

    return times[time]


resultado = get_idade(20)

resultado = get_nome_torcedor("São Paulo")

print(resultado)
