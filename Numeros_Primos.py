print("*************************************")

divisores = 0
i = 1

numero = int(input("Qual número? >>> "))

while i <= numero:
    if numero % i == 0:
        print(f"\033[1:33mDividiu por {i}")
        divisores += 1
        i += 1
    else:
        i += 1

if i == numero + 1 and divisores == 2:
    print("\033[1:32mÉ Primo")
else:
    print("\033[1:31mNão é Primo")
