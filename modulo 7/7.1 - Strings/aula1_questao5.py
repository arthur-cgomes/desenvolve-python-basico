# Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. Dica: letra in "aeiou". Exemplo:

def main():
    frase = input("Digite uma frase: ").lower()
    vogais = "aeiou"
    indices_vogais = []

    for i, letra in enumerate(frase):
        if letra in vogais:
            indices_vogais.append(i)

    quantidade_vogais = len(indices_vogais)
    
    print(f"{quantidade_vogais} vogais")
    print(f"Índices {indices_vogais}")

if __name__ == "__main__":
    main()
