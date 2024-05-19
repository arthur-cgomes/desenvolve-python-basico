# 1) Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local do seu script. Imprima em seguida o caminho completo do arquivo salvo.
# Ex: 
# Digite uma frase: Bom dia, meu nome é Davi.

import os

def salvar_frase_em_arquivo():
    frase = input("Digite uma frase: ")
    nome_arquivo = "frase.txt"
    
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(frase)
    
    caminho_completo = os.path.abspath(nome_arquivo)
    
    print(f"O arquivo foi salvo em: {caminho_completo}")

if __name__ == "__main__":
    salvar_frase_em_arquivo()
