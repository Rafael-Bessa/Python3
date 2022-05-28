def vertical(a):
    for i in a:
        print(i)


def escadinha(a, b):
    for i in a:
        b = b + i
        print(b)


def escadinha_invertida(a):
    while len(a) >= 1:
        print(a)
        a = a[:-1]


print("-=" * 30)
nome = input("Qual nome? >>> ")
palavra = ""
print("-=" * 30)
print()
print("Digite 1, para VERTICAL")
print("Digite 2, para ESCADINHA")
print("Digite 3, para ESCADINHA INVERTIDA")
print()

while True:
    tipo = int(input(">>> "))
    if tipo != 1 and tipo != 2 and tipo != 3:
        print("Número inválido. Digite novamente")
    else:
        break

if tipo == 1:
    vertical(nome)
elif tipo == 2:
    escadinha(nome, palavra)
else:
    escadinha_invertida(nome)
