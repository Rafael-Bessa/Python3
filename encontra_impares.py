def encontra_impares(lista, impares=None):
    if impares is None:
        impares = []
    if len(lista) == 0:
        return impares
    else:
        if lista[0] % 2 == 1:
            impares.append(lista[0])
            lista = lista[1:]
            return encontra_impares(lista, impares)
        else:
            lista = lista[1:]
            return encontra_impares(lista, impares)
