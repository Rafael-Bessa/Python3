# media aritmética
# media geométrica
# media harmônica

p1 = float(input("Primeira nota: >>> "))
p2 = float(input("Segunda nota: >>> "))
p3 = float(input("Terceira nota: >>> "))
p4 = float(input("Quarta nota: >>> "))

ma = (p1 + p2 + p3 + p4) / 4
mg = abs(p1 * p2 * p3 * p4) ** 0.25
mh = 4 / ((1 / p1) + (1 / p2) + (1 / p3) + (1 / p4))

print(f"A média aritmética é \033[1:34m{ma}\033[m, a média geométrica é \033[1:32m{mg}"
      f"\033[m e a média harmônica é \033[1:31m{mh}\033[m")

medias = (ma, mg, mh)

print("~"*90)
print(f"A maior média é {max(medias)} e a menor média é {min(medias)}")
print("Comprovando que a média aritmética quase sempre é a maior mesmo, e a harmônica a menor")
