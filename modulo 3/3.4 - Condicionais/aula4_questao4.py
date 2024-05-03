# 4) Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso 
# do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa 
# deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
# Distância até 100 km: R$1 por kg.
# Distância entre 101 e 300 km: R$1.50 por kg.
# Distância acima de 300 km: R$2 por kg.
# Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

kg = int(input("Digite o peso do pacote em quilogramas: "))
km = int(input("Digite a distância da entrega em quilômetros: "))
pacote = float(0)

if kg > 10:
    pacote = float(10)

if km <= 100:
    pacote += float(kg)

if km > 100 and km <= 300:
    pacote += float(kg * 1.5)

if km > 300:
    pacote += float(kg * 2)

print("O valor do frete é de R$%.2f" % pacote)