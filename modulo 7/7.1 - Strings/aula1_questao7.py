# Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. Regras:
# Chave de criptografia: gere um valor n aleatório entre 1 e 10
# Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)

import random

def encrypt(nomes):
    n = random.randint(1, 10)
    
    def criptografar_nome(nome, chave):
        nome_criptografado = ""
        for char in nome:
            novo_char = chr(((ord(char) - 33 + chave) % 94) + 33)
            nome_criptografado += novo_char
        return nome_criptografado

    nomes_criptografados = [criptografar_nome(nome, n) for nome in nomes]
    
    return nomes_criptografados, n

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave_aleatoria = encrypt(nomes)

print(f"Chave de criptografia: {chave_aleatoria}")
print(f"Nomes criptografados: {nomes_criptografados}")
