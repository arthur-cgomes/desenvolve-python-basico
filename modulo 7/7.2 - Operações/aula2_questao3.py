# 3) Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando até que o usuário digite "Fim".Ex:

# Digite uma frase (digite "fim" para encerrar): Radar
# "Radar" é palíndromo
# Digite uma frase (digite "fim" para encerrar): Bom dia!
# "Bom dia!" não é palíndromo
# Digite uma frase (digite "fim" para encerrar): Ame o poema
# "Ame o poema" é palíndromo
# Digite uma frase (digite "fim" para encerrar): A Daniela ama a lei? Nada!
# "A Daniela ama a lei? Nada!" é palíndromo
# Digite uma frase (digite "fim" para encerrar): fim

def verificar_palindromo(frase):
    frase_formatada = ''.join(caractere.lower() for caractere in frase if caractere.isalnum())
    return frase_formatada == frase_formatada[::-1]

def main():
    while True:
        entrada = input("Digite uma frase (digite 'fim' para encerrar): ")
        
        if entrada.lower() == "fim":
            break
        
        if verificar_palindromo(entrada):
            print(f'"{entrada}" é palíndromo')
        else:
            print(f'"{entrada}" não é palíndromo')

if __name__ == "__main__":
    main()
