# 2) Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".
# Ex:
# Digite uma frase: O rato roeu a roupa do rei
# Frase modificada: * r*t* r*** * r**p* d* r**

def substituir_vogais_por_asterisco(frase):
    vogais = 'aeiouAEIOU'
    frase_modificada = ''
    for char in frase:
        if char in vogais:
            frase_modificada += '*'
        else:
            frase_modificada += char
    return frase_modificada

def main():
    frase = input("Digite uma frase: ")
    frase_modificada = substituir_vogais_por_asterisco(frase)
    print("Frase modificada:", frase_modificada)

if __name__ == "__main__":
    main()
