# 4) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de 
# notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada 
# exatamente como indicado. 

# Entrada:
# 576

# Saída:
# 5 nota(s) de R$100,00
# 1 nota(s) de R$50,00
# 1 nota(s) de R$20,00
# 0 nota(s) de R$10,00
# 1 nota(s) de R$5,00
# 0 nota(s) de R$2,00
# 1 nota(s) de R$1,00

v = int(input("Insira um valor: "))

c = v//100
v -= (c*100)
print(c, "nota(s) de R$100,00")

b = v//50
v -= (b*50)
print(b, "nota(s) de R$50,00")

n = v//20
v -= (n*20)
print(n, "nota(s) de R$20,00")

r = v//5
v -= (r*5)
print(r, "nota(s) de R$10,00")

a = v//10
v -= (a*10)
print(a, "nota(s) de R$5,00")

s = v//2
v -= (s*2)
print(s, "nota(s) de R$2,00")

f = v//1
v -= (f*1)
print(f, "nota(s) de R$1,00")