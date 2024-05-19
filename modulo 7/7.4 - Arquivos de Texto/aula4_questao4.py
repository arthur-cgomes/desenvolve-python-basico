import random

def carregar_palavras():
    with open("gabarito_forca.txt", "r") as arquivo:
        palavras = arquivo.read().splitlines()
    return palavras

def carregar_enforcado():
    with open("gabarito_enforcado.txt", "r") as arquivo:
        estagios = arquivo.read().split("=====\n")
    return estagios

def escolher_palavra(palavras):
    return random.choice(palavras)

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

def jogar():
    palavras = carregar_palavras()
    estagios = carregar_enforcado()
    palavra_secreta = escolher_palavra(palavras)
    letras_acertadas = ["_"] * len(palavra_secreta)
    tentativas = 6
    erros = 0
    letras_digitadas = set()

    print("Bem-vindo ao jogo da Forca!")
    print("A palavra tem", len(palavra_secreta), "letras.")
    print(" ".join(letras_acertadas))

    while erros < tentativas:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_digitadas:
            print("Você já digitou essa letra. Tente outra.")
            continue

        letras_digitadas.add(letra)

        if letra in palavra_secreta:
            for i, l in enumerate(palavra_secreta):
                if l == letra:
                    letras_acertadas[i] = letra
            print("Boa! A letra", letra, "está na palavra.")
        else:
            erros += 1
            imprime_enforcado(erros, estagios)
            print("A letra", letra, "não está na palavra. Você tem", tentativas - erros, "tentativas restantes.")

        print(" ".join(letras_acertadas))

        if "_" not in letras_acertadas:
            print("Parabéns! Você acertou a palavra:", palavra_secreta)
            break
    else:
        imprime_enforcado(erros, estagios)
        print("Você foi enforcado! A palavra era:", palavra_secreta)

if __name__ == "__main__":
    jogar()
