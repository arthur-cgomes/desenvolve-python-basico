print("Digite pelo menos 4 números inteiros (digite 'fim' para parar):")

numeros = []

while True:
    numero = input("Digite um número inteiro ou 'fim' para parar: ")
    if numero.lower() == 'fim':
        break
    numeros.append(int(numero))

if len(numeros) < 4:
    print("Pelo menos 4 números inteiros devem ser fornecidos.")
else:
    print("Lista original:", numeros)
    print("Os 3 primeiros elementos:", numeros[:3])
    print("Os 2 últimos elementos:", numeros[-2:])
    print("Lista invertida:", numeros[::-1])
    print("Elementos de índice par:", numeros[::2])
    print("Elementos de índice ímpar:", numeros[1::2])
