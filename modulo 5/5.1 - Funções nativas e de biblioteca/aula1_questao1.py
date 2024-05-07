# Solicita ao usuário para inserir dois números decimais
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

diferenca_absoluta = abs(numero1 - numero2)
diferenca_absoluta_arredondada = round(diferenca_absoluta, 2)

print("A diferença absoluta entre os números é:", diferenca_absoluta_arredondada)
