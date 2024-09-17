"""
For + range

    range -> (start, stop, step)

    ⚠️ -> step representa o passo!
"""

numbers = range(10)  # de 0 até menor do que 10 (9)
numbers = range(5, 10)  # de 5 até menor do que 10 (9)
numbers = range(0, 10, 2)  # de 0 até menor do que 10 (9), pares

print(numbers)

for num in numbers:
    print(f"{num} é par!")
