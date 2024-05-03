n = int(input("Digite o número de experimentos feitos: "))
cont = 0
coe = 0
rat = 0
sap = 0

while cont < n:

    quantia = int(input("Quantas cobaias foram utilizadas? "))  
    tipo = (input("Qual espécie foi usada? (c, r, s) " ))


    if tipo == 'c':
        coe += quantia
    
    elif tipo == 's':
        sap += quantia

    elif tipo == 'r':
        rat += quantia

    cont += 1

psap = sap/1
prat = rat/1
pcoe = coe/1

print("Total de cobaias :", sap + coe + rat)
print("Total de sapos: ", sap)
print("Total de ratos: ", rat)
print("Total de coelhos: ", coe)
print("Porcentagem de coelhos: ", pcoe, "%")
print("Porcentagem de ratos: ", prat, "%")
print("Porcentagem de sapos: ", psap, "%")
