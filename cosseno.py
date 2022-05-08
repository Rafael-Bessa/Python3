import math

print(30*"*")
print("Programa para calcular o \033[1:31mCosseno\033[m de um ângulo entre 0° e 360°")
print("Quanto maior o número de iterações, maior a precisão do valor")
print(30*"~")

x = float(input("Qual ângulo? >>> "))

if(x > 360):
    x = x - 360

angulo = (x*math.pi)/180
float(angulo)
soma = 1

n = int(input("Quantas iterações? >>> "))

for i in range (1,n+1):
    soma = soma + ((-1)**i*((angulo**2)**i)/math.factorial(2*i))

if(soma < 0.001 and soma > 0):
    soma = 0
print(f"O \033[1:31mCosseno\033[m do ângulo é \033[1:32m{soma}")

