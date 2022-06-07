"""Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à 
largura e à altura de um retângulo, respectivamente. O programa deve imprimir, usando repetições encaixadas (laços 
aninhados), uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída. """

largura = int(input("Qual a largura do retângulo? >>> "))
altura = int(input("Qual a altura do retângulo? >>> "))

for i in range(1, altura + 1):
    for j in range(1, largura + 1):
        print("#", end="")
    print()
