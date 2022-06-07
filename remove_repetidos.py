lista = [7, 3, 33, 12, 3, 3, 3, 7, 12, 100]


def remove_repetidos(a):
    lista_nova = []
    for i in a:
        if i in lista_nova:
            continue
        else:
            lista_nova.append(i)

    lista_nova.sort()
    return lista_nova


remove_repetidos(lista)

