# Escreva um script que dado uma frase conta os espaços em branco.
# Digite a frase: Meu amor mora em Roma e me deu um ramo de flores
# Espaços em branco: 11

def main():
    frase = input("Digite a frase: ")
    espacos_em_branco = frase.count(' ')
    print(f"Espaços em branco: {espacos_em_branco}")

if __name__ == "__main__":
    main()
