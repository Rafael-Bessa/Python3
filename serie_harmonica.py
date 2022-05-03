print("*****************")

def serie_harmonica(n):
    soma = 0
    for x in range(1,n+1):
        soma += 1/x
    print(soma)

n = int(input("Qual número? >>> "))

while(n<1):
    print("Por favor digite um número maior que zero")
    n = int(input("Qual número? >>> "))

serie_harmonica(n)




