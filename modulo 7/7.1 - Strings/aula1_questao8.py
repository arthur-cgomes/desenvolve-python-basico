# Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima "Válido" ou "Inválido". 
# O primeiro passo é calcular o primeiro dígito verificador. Separamos os primeiros 9 dígitos do CPF (ex: 111.444.777) e multiplicamos cada um dos números, da direita para a esquerda por números crescentes a partir do número 2, como no exemplo abaixo:

def calcular_digito_verificador(cpf, multiplicadores):
    soma = sum(int(cpf[i]) * multiplicadores[i] for i in range(len(multiplicadores)))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def validar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    cpf_base = cpf[:9]
    
    multiplicadores_primeiro_digito = list(range(10, 1, -1))
    primeiro_digito_calculado = calcular_digito_verificador(cpf_base, multiplicadores_primeiro_digito)
    
    cpf_base += str(primeiro_digito_calculado)
    
    multiplicadores_segundo_digito = list(range(11, 1, -1))
    segundo_digito_calculado = calcular_digito_verificador(cpf_base, multiplicadores_segundo_digito)
    
    return cpf == (cpf_base + str(segundo_digito_calculado))

def main():
    cpf = input("Digite um CPF na forma XXX.XXX.XXX-XX: ")
    if validar_cpf(cpf):
        print("Válido")
    else:
        print("Inválido")

if __name__ == "__main__":
    main()
