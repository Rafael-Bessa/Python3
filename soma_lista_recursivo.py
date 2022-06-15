def soma_lista(lista, soma=0):
    if len(lista) == 0:
        return soma
    else:
        soma += lista[0]
        lista = lista[1:]
        return soma_lista(lista, soma)


a = [1,2,3,4]
print(soma_lista(a))