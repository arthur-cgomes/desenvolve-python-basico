import random
from math import sqrt

n = int(input("Digite o valor de n: "))

valores = [random.randint(0, 100) for _ in range(n)]

soma = sum(valores)
raiz_quadrada_soma = sqrt(soma)

print("A raiz quadrada da soma dos valores é:", raiz_quadrada_soma)
