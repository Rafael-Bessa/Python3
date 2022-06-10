def menor_nome(nomes):
    resposta = ""
    menor = 10000
    for nome in nomes:
        if menor > len(nome.strip()):
            menor = len(nome.strip())
            resposta = nome.strip()
        else:
            continue

    return resposta.capitalize()

