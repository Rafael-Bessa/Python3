import random

print()
print("Lei dos Grandes Números (Law of Large Numbers)")
print()
print("**************************")
print()

soma_de_lançamentos = 0
i = 1
media = 0

n = int(input("Quantos vezes você vai lançar o dado? "))

while(i <= n):
    valor_lançamento = random.randrange(1,7)
    soma_de_lançamentos = soma_de_lançamentos + valor_lançamento
    i += 1


media = (soma_de_lançamentos/n)
print("A média aritmética de {} lançamentos é {}".format(n,media))
print("Quanto maior o número de lançamentos é possível concluir que a média converge para o número 3.5")
