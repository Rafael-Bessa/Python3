print("*"*45)

palavra = input("Qual palavra? >>> ")
palavra = palavra.upper()
separador = set(palavra)

for letra in separador:
    print(letra, end="")
    print(" - ", end="")
    print(str.count(palavra, letra))
