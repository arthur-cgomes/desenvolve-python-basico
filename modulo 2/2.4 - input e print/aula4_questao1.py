# 1) Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado 
# da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir.

# O terreno possui 250m2 e custa R$512,490.50

# Comente na linha acima de cada instrução uma breve descrição da instrução.

# Fórmulas:
# area_m2 = comprimento * largura
# preco_total = preco_m2 * area_m2

# Solicitação dos dados
comprimento = int(input("Digite o comprimento do terreno em metros: "))
largura = int(input("Digite a largura do terreno em metros: "))
preco_m2 = float(input("Digite o preço do metro quadrado da região: "))

# Calcula a área do terreno multiplicando o comprimento pela largura.
area_m2 = comprimento * largura

# Calcula o preço total do terreno multiplicando o preço por metro quadrado pela área do terreno.
preco_total = preco_m2 * area_m2

# Imprime o valor do terreno formatado com duas casas decimais e separador de milhares, usando o formato monetário brasileiro.
print(f"O terreno possui {area_m2}m² e custa R${preco_total:,.2f}.")
