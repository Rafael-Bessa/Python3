import webbrowser as web

print(":*"*20)
lista_sites = ['1 - Github', '2 - Globo Esporte', '3 - Twitter', '4 - Alura', '5 - Steam']
print("Qual site você quer acessar?")
print(*lista_sites, sep="\n")

while True:
    site = int(input(">>> "))
    if 1 <= site <= 5:
        break
    print("Valor invalido. Digite novamente ", end="")

if site == 1:
    web.open("https://github.com/Rafael-Bessa")
elif site == 2:
    web.open("https://ge.globo.com")
elif site == 3:
    web.open("https://twitter.com/home")
elif site == 4:
    web.open("https://www.alura.com.br")
else:
    web.open("https://steamcommunity.com")
