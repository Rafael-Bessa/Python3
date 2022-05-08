def funcao(a,b,c,d,x):
    f = a*(x**3) + b*(x**2) + c*x + d
    return f

def funcao_derivada(a,b,c,x):
    fd = 3*a*(x**2) + 2*b*x + c
    return fd

print(30*"*")
print(30*"~")
print("Método de Newton-Raphson")
print("Exercício para uma equação de\033[1:31m TERCEIRO GRAU\033[m")
erro = 1

a = int(input("O valor para o termo que multiplica x³: >>> "))
b = int(input("O valor para o termo que multiplica x²: >>> "))
c = int(input("O valor para o termo que multiplica x: >>> "))
d = int(input("O valor para o termo independente: >>> "))
x = float(input("Qual seu chute inicial para começar? >>> "))

while(erro > 0.005):
    y = x - (funcao(a, b, c, d, x)/funcao_derivada(a,b,c,x))
    erro = abs((y-x)/y)
    x = y
    #print(erro)

print(f"Uma das raízes é \033[1:35m{x}\033[m")



