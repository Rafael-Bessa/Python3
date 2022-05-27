"""Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por 
exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura 
relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se 
como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça 
uma texto e transforme-o para a grafia leet speak. """

print("-=" * 30)
print()
leet = input("Digite uma palavra para ser transformada: >>> ")

while "a" or "e" or "i" or "o" in leet:
    if "a" in leet:
        leet = leet.replace("a", "4")
    elif "e" in leet:
        leet = leet.replace("e", "3")
    elif "i" in leet:
        leet = leet.replace("i", "1")
    elif "o" in leet:
        leet = leet.replace("o", "0")
    else:
        break

print(f"A palavra transformada fica: {leet}")
