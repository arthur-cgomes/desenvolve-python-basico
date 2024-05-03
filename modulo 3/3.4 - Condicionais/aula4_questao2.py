# 2) Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. Escreva um programa em Python 
# que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5. O programa deve imprimir uma mensagem 
# correspondente à classificação do filme:

# Se a avaliação for 5, imprima "Excelente!"
# Se a avaliação for 4, imprima "Muito Bom!"
# Se a avaliação for 3, imprima "Bom!"
# Se a avaliação for 2, imprima "Regular."
# Se a avaliação for 1, imprima "Ruim."

avaliacao = int(input("Digite a avaliação do filme (1 a 5): "))

if avaliacao <= 0:
    print("Avaliação inválida, digite um número entre 1 e 5.")

if avaliacao == 1:
    print("Avaliação: Ruim")

if avaliacao == 2:
    print("Avaliação: Regular")

if avaliacao == 3:
    print("Avaliação: Bom")

if avaliacao == 4:
    print("Avaliação: Muito Bom")

if avaliacao == 5:
    print("Avaliação: Excelente")

if avaliacao > 5:
    print("Avaliação inválida, digite um número entre 1 e 5.")