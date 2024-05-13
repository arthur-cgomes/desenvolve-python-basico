def intercalar_listas(lista1, lista2):
    resultado = []
    tamanho_min = min(len(lista1), len(lista2))

    for i in range(tamanho_min):
        resultado.append(lista1[i])
        resultado.append(lista2[i])
    if len(lista1) > len(lista2):
        resultado.extend(lista1[len(lista2):])
    elif len(lista2) > len(lista1):
        resultado.extend(lista2[len(lista1):])
    return resultado

quantidade_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = [int(input("Digite os elementos da lista 1:\n")) for _ in range(quantidade_lista1)]

quantidade_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = [int(input("Digite os elementos da lista 2:\n")) for _ in range(quantidade_lista2)]

lista_intercalada = intercalar_listas(lista1, lista2)
print("Lista intercalada:", ' '.join(map(str, lista_intercalada)))
