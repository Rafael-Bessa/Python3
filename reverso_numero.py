"""Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.
 Por exemplo: 127 -> 721."""


def reverse(n):
    n = list(n)
    n.reverse()
    n = "".join(n)
    print(n)


print("*" * 30)

numero = input("Qual número? >>> ")

reverse(numero)
