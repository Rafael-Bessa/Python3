# evitar usar if, e usar a ideia de tuples


lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
         'dezoito', 'dezenove', 'vinte')

print("~" * 60)

while True:
    numero = int(input("Digite um número entre 0 e 20: >>> "))
    if 0 <= numero <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número \033[1:36m{lista[numero]}\033[m')
