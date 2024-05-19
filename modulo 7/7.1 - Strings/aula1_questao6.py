# Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.

def main():
    from collections import Counter

    def encontrar_anagramas(frase, palavra_objetivo):
        frase = frase.lower()
        palavra_objetivo = palavra_objetivo.lower()

        contador_objetivo = Counter(palavra_objetivo)
        tamanho_palavra = len(palavra_objetivo)
        anagramas = []

        palavras = frase.split()

        for palavra in palavras:
            if len(palavra) == tamanho_palavra and Counter(palavra) == contador_objetivo:
                anagramas.append(palavra)

        return anagramas

    frase = input("Digite uma frase: ")
    palavra_objetivo = input("Digite a palavra objetivo: ")
    anagramas = encontrar_anagramas(frase, palavra_objetivo)

    print(f"Anagramas: {anagramas}")

if __name__ == "__main__":
    main()
