import random

def embaralha_palavra(a):
    lista = list(a)
    random.shuffle(lista)
    a = "".join(lista)
    print(a)

print(30*"*")
print(30*"~")
print("Embaralhador de palavras")
print()
palavra = input("Qual palavra? >>> ")
print()

embaralha_palavra(palavra)



