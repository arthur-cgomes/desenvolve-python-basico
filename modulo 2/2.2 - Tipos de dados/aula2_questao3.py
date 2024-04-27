# 3) Dadas duas variáveis v1 = 10 e v2 = 20, utilize uma terceira variável para trocar os valores entre as duas variáveis. Ou seja, ao final v1 terá o valor de v2, 
# e v2 o valor de v1. Você deve usar uma variável auxiliar de troca, não podendo atribuir os novos valores diretamente.

var1 = 10
var2 = 20

auxiliar = var1
var1 = var2
var2 = auxiliar

print("var1:", var1)
print("var2:", var2)