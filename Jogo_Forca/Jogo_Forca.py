import random


arquivo = open("Palavras.txt", "r")
lista_de_palavras = []

for linha in arquivo:
    linha.strip()
    lista_de_palavras.append(linha)

index = random.randrange(0,len(lista_de_palavras))
palavra_secreta = lista_de_palavras[index]
palavra_secreta.strip()
palavra_secreta = palavra_secreta.upper()
#print(palavra_secreta)


arquivo.close()

print("**************************")
print("Bem vindo ao jogo da Forca")
print("As palavras são nomes de animais em inglês")
print("**************************")
print()
print()

enforcou = False
ganhou = False
morte = 7

#palavra_secreta = "rafael"
#palavra_secreta = palavra_secreta.upper()

forca = ["_"]
forca = forca * len(palavra_secreta.strip())
print(forca)



while(enforcou == False and ganhou == False):

    chute = input("Qual Letra? ")
    chute = chute.strip().upper()

    if(chute in palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
            if(chute == letra):
                #print("Encontrei a letra {} na posição {}".format(chute,posicao))
                forca[posicao] = chute
            posicao += 1
        print(forca)

    else:
        morte -= 1
        print("Não tem a letra {}".format(chute))
        print("Você tem mais {} tentativas".format(morte))
        print(forca)


    if(morte == 0):
        enforcou = True
        print()
        print("Você se enforcou amigo")
        print("A palavra era {}".format(palavra_secreta))
        print("Rest In Peace")
    elif(morte != 0 and "_" not in forca):
        ganhou = True
        print("Você ganhou, Parabéns")
    else:
        pass

print(forca)
print("*********************")
print("Fim de jogo")


