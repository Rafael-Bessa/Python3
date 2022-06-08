import random

print()
print("Lei dos Grandes Números (Law of Large Numbers)")
print()
print("*"*50)
print()

soma_de_lancamentos = 0
i = 1
media = 0

n = int(input("Quantos vezes você vai lançar o dado? >>> "))

while i <= n:
    valor_lancamento = random.randrange(1, 7)
    soma_de_lancamentos += valor_lancamento
    i += 1

media = (soma_de_lancamentos / n)
print("A média aritmética de {} lançamentos é \033[1:36m{}\033[m".format(n, media))
print("Quanto maior o número de lançamentos é possível concluir que a média converge para o número 3.5")
