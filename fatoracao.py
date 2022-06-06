n = int(input("Digite um número inteiro maior do que 1: >>> "))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade += 1
        n = n / fator
    if multiplicidade > 0:
        print(f'O fator \033[1:32m{fator}\033[m , tem multiplicidade \033[1:31m{multiplicidade}\033[m')
    fator += 1
    multiplicidade = 0
