# 5) De acordo com uma pesquisa do linguista Matt Davis, o cérebro humano consegue ler palavras com as letras embaralhadas, contanto que a primeira e a última letra estejam no lugar correto. Implemente uma função chamada embaralhar_palavras() para ajudar a testar a hipótese do Matt Davis. Sua função vai receber uma frase, embaralhar as letras internas de cada palavra e retornar a frase modificada. Dica: use a biblioteca random.

# Complete o seguinte código:
# def embaralhar_palavras(frase):
#     #### Escreva a função

# # Exemplo de uso:
# frase = "Python é uma linguagem de programação"
# resultado = embaralhar_palavras(frase)
# print(resultado)
# # Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"

import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    frase_embaralhada = []
    
    for palavra in palavras:
        if len(palavra) <= 3:
            frase_embaralhada.append(palavra)
        else:
            primeira_letra = palavra[0]
            ultima_letra = palavra[-1]
            caracteres_internos = list(palavra[1:-1])
            random.shuffle(caracteres_internos)
            palavra_embaralhada = ''.join(caracteres_internos)
            palavra_embaralhada = primeira_letra + palavra_embaralhada + ultima_letra
            frase_embaralhada.append(palavra_embaralhada)
    
    return ' '.join(frase_embaralhada)
