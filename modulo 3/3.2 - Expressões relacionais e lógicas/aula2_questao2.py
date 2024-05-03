# 2) Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade 
# (ficando responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, 
# mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário.

jl = int(input("Insira a idade de Juliana: "))
cr = int(input("Insira a idade de Cris: "))

if jl > 17 or cr > 17:
    print(True)
else:
    print(False)