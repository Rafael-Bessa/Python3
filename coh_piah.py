import re


def le_assinatura():
    """A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os
    textos fornecidos """
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))  # 4.51
    ttr = float(input("Entre a relação Type-Token: "))  # 0.693
    hlr = float(input("Entre a Razão Hapax Legomana: "))  # 0.55
    sal = float(input("Entre o tamanho médio de sentença: "))  # 70.82
    sac = float(input("Entre a complexidade média da sentença: "))  # 1.82
    pal = float(input("Entre o tamanho medio de frase: "))  # 38.5

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    """A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento"""
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair): ")

    return textos


def separa_sentencas(texto):
    """A funcao recebe um texto e devolve uma lista das sentencas dentro do texto"""
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    """A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca"""
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    """A funcao recebe uma frase e devolve uma lista das palavras dentro da frase"""
    return frase.split()


def n_palavras_unicas(lista_palavras):
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez"""
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas"""
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    soma = 0
    i = 0

    while i < len(as_a):
        soma += abs(as_a[i] - as_b[i])
        i += 1

    s = soma / 6

    return s


def calcula_assinatura(texto):
    # resolução do sac

    n = len(separa_sentencas(texto))
    x = separa_sentencas(texto)
    soma1 = 0
    for y in x:
        z = separa_frases(y)
        soma1 += len(z)

    sac = soma1 / n

    # resolucao do sal

    pontuacao_sentenca = [".", "!", "?"]

    for y in pontuacao_sentenca:
        if y in texto:
            texto = texto.replace(y, "")
        else:
            continue

    sal = len(texto) / n

    # resolucao do wal, ttr, hlr

    pontuacao = [",", ":", ";"]

    for x in pontuacao:
        if x in texto:
            texto = texto.replace(x, "")
        else:
            continue

    e = separa_palavras(texto)
    # print(len(e))
    soma2 = 0

    for x in e:
        soma2 = soma2 + len(x)

    # print(soma2)
    wal = soma2 / len(e)
    ttr = n_palavras_diferentes(e) / len(e)
    hlr = n_palavras_unicas(e) / len(e)

    pontos = [".", "!", "?", ",", ":", ";"]
    for r in pontos:
        if r in texto:
            texto = texto.replace(r, "")
        else:
            continue

    m = len(texto)
    pal = m / soma1

    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    menor = 10000
    lista_comparacao = []
    for i in textos:
        prova = calcula_assinatura(i)
        comparador = compara_assinatura(prova, ass_cp)
        lista_comparacao.append(comparador)

    for j in lista_comparacao:
        if menor > j:
            menor = j
        else:
            continue

    posicao = lista_comparacao.index(menor)
    return posicao + 1
