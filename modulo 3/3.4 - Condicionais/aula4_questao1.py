# 1) Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão do número 
# por 2 for 0, o número é par, caso contrário é ímpar. Lembre-se do operador do python % que retorna o resto de uma divisão.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

n3 = int(n1 + n2)

n3 = n3 % 2

if n3 != 0:
    print("A soma dos números é ímpar.")
else:
    print("A soma dos números é par.")