# 1) Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). Escreva um programa que solicite 
# as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos, indicando que podem entrar no bar, e False 
# caso contrário.

jl = int(input("Insira a idade de Juliana: "))
cr = int(input("Insira a idade de Cris: "))

if jl > 17 and cr > 17:
    print(True)
else:
    print(False)