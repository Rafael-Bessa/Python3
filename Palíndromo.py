import webbrowser

print("Verificador de palíndromos")
print("******************")
print()
print()
print("Favor escrever sem pontuação!")

def verifica_palindromo(palavra):
    i = 0
    palindromo = False

    while(palavra[i] == palavra[len(palavra)-1-i]):
        i += 1

        #print(f"palindromo {i}")
        if(i == len(palavra)):
            print("É um palíndromo")
            palindromo = True
            break
    if(palindromo == False):
        print("Não é um palídromo")
        print()
        print("Quer saber o que é um palíndromo?")
        site = int(input("Digite 1 para SIM ou 2 para NÃO >>> "))
        if(site == 1):
            webbrowser.open("https://pt.wikipedia.org/wiki/Pal%C3%ADndromo")
        elif(site == 2):
            print("Até a próxima")
        else:
            print("Digite apenas 1 ou 2 amigo, que cara teimoso, vai ter que dar play de novo agora!")


sem_numero = True
palavra = input("Qual palavra ou frase? >>> ")
palavra = palavra.strip()
palavra = palavra.upper()
palavra = palavra.replace(" ","")

while(sem_numero):

    if(palavra.find("0") == -1 and palavra.find("1") == -1 and palavra.find("2") == -1 and palavra.find("3") == -1 and palavra.find("4") == -1 and palavra.find("5") == -1 and palavra.find("6") == -1 and palavra.find("7") == -1 and palavra.find("8") == -1 and palavra.find("9") == -1):
        #palavra_verificada = [palavra]
        sem_numero = False
        verifica_palindromo(palavra)

    else:
        print("Só é válido palavras amigo")
        palavra = input("Qual palavra? ")

list(palavra)






