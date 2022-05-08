palavra = input("Palavra que você quer inverter >>> ")

lista = []
lista2 = []

for letra in palavra:
    #print(letra)
    lista.append(letra)

print(lista)

for i in range (1,len(lista)+1):
    lista2.append(lista[len(palavra)-i])

print(lista2)

