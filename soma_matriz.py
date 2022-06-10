def soma_matrizes(m1, m2):
    row1 = len(m1)
    col1 = len(m1[0])

    row2 = len(m2)
    col2 = len(m2[0])
    soma = []
    valor = 0
    for x in range(row1):
        linha = []
        for y in range(col1):
            linha.append(valor)
        soma.append(linha)

    if row1 == row2 and col1 == col2:

        for j in range(0, row1):
            for i in range(0, col1):
                soma[j][i] = (m1[j][i] + m2[j][i])

        return soma
    else:
        return False


matriz1 = [[1, 7, 3],
           [4, 0, 6]]

matriz2 = [[2, 3, 4],
           [3, 6, 7]]

soma_matrizes(matriz1, matriz2)
teste = soma_matrizes(matriz1, matriz2)
print(teste)
