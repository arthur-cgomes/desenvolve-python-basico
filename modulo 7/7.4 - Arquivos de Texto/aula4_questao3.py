def processar_roteiro():
    nome_arquivo = "estomago.txt"
    
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        
        print("Primeiras 25 linhas do arquivo:")
        for linha in linhas[:25]:
            print(linha, end="")
        print("\n")
        
        numero_de_linhas = len(linhas)
        print(f"Número de linhas do arquivo: {numero_de_linhas}\n")
        
        linha_maior_numero_caracteres = max(linhas, key=len)
        print(f"Linha com maior número de caracteres ({len(linha_maior_numero_caracteres)} caracteres):")
        print(linha_maior_numero_caracteres)
        
        mentions_nonato = sum(1 for linha in linhas if "nonato" in linha.lower())
        mentions_iria = sum(1 for linha in linhas if "íria" in linha.lower())
        print(f"\nNúmero de menções ao nome 'Nonato': {mentions_nonato}")
        print(f"Número de menções ao nome 'Íria': {mentions_iria}")
    
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")

if __name__ == "__main__":
    processar_roteiro()
