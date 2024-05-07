import random

numero_aleatorio = random.randint(1, 10)

while True:
    palpite = int(input("Adivinhe o número (entre 1 e 10): "))

    if palpite == numero_aleatorio:
        print("Parabéns! Você acertou o número", numero_aleatorio)
        break
    elif palpite < numero_aleatorio:
        print("O seu palpite é muito baixo.")
    else:
        print("O seu palpite é muito alto.")
