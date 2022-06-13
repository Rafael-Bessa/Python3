def busca(lista, elemento):
    j = 0
    for i in lista:
        if i == elemento:
            return j
        else:
            j += 1

    if j == len(lista):
        return False


