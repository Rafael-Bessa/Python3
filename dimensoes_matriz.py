def dimensoes(matriz):
    linha = len(matriz)
    coluna = len(matriz[0])

    print(str(linha) + "X" + str(coluna))


m = [[1, 2, 3], [4, 5, 6]]

dimensoes(m)