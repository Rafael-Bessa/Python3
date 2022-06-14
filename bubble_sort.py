def bubble_sort(lista):

    for j in range(0, len(lista)):
        k = 0
        for i in range(1, len(lista)):
            if lista[k] > lista[i]:
                lista[i], lista[k] = lista[k], lista[i]
                print(lista)
                k += 1
            else:
                k += 1
                continue
    return lista


