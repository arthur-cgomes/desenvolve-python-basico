# Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.
# Digite o número: 97651234
# Número completo: 99765-1234
# Digite o número: 980876543
# Número completo: 98087-6543 

def main():
    numero = input("Digite o número: ")
    
    if len(numero) == 8:
        numero = '9' + numero
    elif len(numero) == 9 and numero[0] != '9':
        print("O número deve começar com 9 se tiver 9 dígitos.")
        return
    
    numero_completo = numero[:5] + '-' + numero[5:]
    
    print(f"Número completo: {numero_completo}")

if __name__ == "__main__":
    main()
