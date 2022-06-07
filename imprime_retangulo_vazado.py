largura = int(input("Qual a largura do retângulo? >>> "))
altura = int(input("Qual a altura do retângulo? >>> "))

x = 0
while x < altura:
    if x == 0 or x == altura - 1:
        print("#" * largura)
        x += 1
    else:
        print("#" + " " * (largura - 2) + "#")
        x += 1
