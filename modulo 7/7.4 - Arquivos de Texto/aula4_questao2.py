# 2) Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".
# Ex:
# Bom
# dia
# meu
# nome
# é
# Davi

import os
import re

def processar_frase():
    arquivo_entrada = "frase.txt"
    arquivo_saida = "palavras.txt"
    
    if not os.path.exists(arquivo_entrada):
        print(f"O arquivo {arquivo_entrada} não foi encontrado.")
        return
    
    with open(arquivo_entrada, "r") as arquivo:
        conteudo = arquivo.read()
    
    palavras = re.findall(r'\b[a-zA-Z]+\b', conteudo)
    
    with open(arquivo_saida, "w") as arquivo:
        for palavra in palavras:
            arquivo.write(palavra + "\n")
    
    with open(arquivo_saida, "r") as arquivo:
        conteudo_saida = arquivo.read()
    
    print("Conteúdo do arquivo 'palavras.txt':")
    print(conteudo_saida)

if __name__ == "__main__":
    processar_frase()
