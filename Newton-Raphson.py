def funcao(a1, b1, c1, d1, x1):
    f = a1 * (x1 ** 3) + b1 * (x1 ** 2) + c1 * (x1 ** 1) + d1
    return f


def funcao_derivada(a2, b2, c2, x2):
    fd = 3 * a2 * (x2 ** 2) + 2 * b2 * (x2 ** 1) + c2
    return fd


print(30 * "*")
print(30 * "~")
print("Método de Newton-Raphson")
print("Exercício para uma equação de\033[1:31m TERCEIRO GRAU\033[m")
erro = 1
zero = True

a = int(input("O valor para o termo que multiplica x³: >>> "))
b = int(input("O valor para o termo que multiplica x²: >>> "))
c = int(input("O valor para o termo que multiplica x: >>> "))
d = int(input("O valor para o termo independente: >>> "))
x = float(input("Qual seu chute inicial para começar? >>> "))

while erro > 0.005:
    try:
        y = x - (funcao(a, b, c, d, x) / funcao_derivada(a, b, c, x))
        erro = abs((y - x) / y)
        x = y
    except ZeroDivisionError:
        zero = False
        print("Parece que você está tentando dividir por \033[1:34mZERO\033[m")
        break

if zero:
    print(f"Uma das raízes é \033[1:35m{x}\033[m\nEssa é a raíz mais próxima do seu chute")
