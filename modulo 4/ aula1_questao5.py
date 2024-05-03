cont = 0
soma_idades = 0

while True:
    x = int(input("Digite a idade (digite 0 para finalizar): "))
    
    if x == 0:
        break
    
    soma_idades += x
    cont += 1

if cont != 0:
    media = soma_idades / cont
    print("Média das idades:", media)
else:
    print("Nenhuma idade foi inserida")