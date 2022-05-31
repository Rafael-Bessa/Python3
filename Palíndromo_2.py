palavra = input("Qual palavra ou texto? >>> ")

pontuacao = [" ", ",", ".", ";", ":", "!", "?", "-", "_", '"']
acentuacao = ["é", "á", "í", "ã", "õ", "ó", "ú", "ô", "ê", "à"]

for ponto in pontuacao:
    if ponto in palavra:
        palavra = palavra.replace(ponto, "")

while not palavra.isascii():

    if "ê" in palavra:
        palavra = palavra.replace("ê", "e")
    elif "á" in palavra:
        palavra = palavra.replace("á", "a")
    elif "é" in palavra:
        palavra = palavra.replace("é", "e")
    elif "ã" in palavra:
        palavra = palavra.replace("ã", "a")
    elif "à" in palavra:
        palavra = palavra.replace("à", "a")
    elif "â" in palavra:
        palavra = palavra.replace("â", "a")
    elif "í" in palavra:
        palavra = palavra.replace("í", "i")
    elif "ô" in palavra:
        palavra = palavra.replace("ô", "o")
    elif "ó" in palavra:
        palavra = palavra.replace("ó", "o")
    elif "õ" in palavra:
        palavra = palavra.replace("õ", "o")
    elif "ç" in palavra:
        palavra = palavra.replace("ç", "c")
    elif "ú" in palavra:
        palavra = palavra.replace("ú", "u")
    else:
        break

palavra_invertida = palavra
palavra_invertida = list(palavra_invertida)
palavra_invertida.reverse()
print(palavra)
palavra_invertida = "".join(palavra_invertida)
print(palavra_invertida)
print()
palavra = palavra.upper()
palavra_invertida = palavra_invertida.upper()

if palavra_invertida == palavra:
    print("\033[1:35mÉ um palíndromo!\033[m")
else:
    print("\033[1:33mNão é um palíndromo\033[m")
