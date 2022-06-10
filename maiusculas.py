def maiusculas(frase):
    frase1 = ""
    for letra in frase:
        if 65 <= ord(letra) <= 90:
            frase1 += str(letra)
        else:
            continue

    return frase1
