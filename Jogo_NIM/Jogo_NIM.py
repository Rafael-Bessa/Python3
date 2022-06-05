def usuario_escolhe_jogada(m, n):
    a = int(input("Quantas peças você quer tirar humano? "))

    while m < a:
        print("Não pode, você só pode tirar até " + str(m) + " peças")
        int(m)
        a = int(input("Quantas peças você quer tirar humano? "))

    print("Você tirou " + str(a) + " peças")
    print("Restam " + str(n - a) + " peças")

    if (n - a) != 0:
        n = (n - a)
        computador_escolhe_jogada(m, n)

    else:
        print("O jogo acabou, e você venceu!")
    int(n)
    int(m)


def computador_escolhe_jogada(m, n):
    b = n % (m + 1)
    n = n - b

    print("O computador tirou " + str(b) + " peças")
    print("Restaram " + str(n) + " peças")

    if n == 0:
        print("COMPUTADOR VENCEU!")
    else:
        usuario_escolhe_jogada(m, n)

    int(n)
    int(m)


print("Bem vindo ao jogo NIM, você vai perder para o computador!")
print()
print("Digite 1 para jogar uma partida isolada")
print("Digite 2 para jogar um campeonato contra o computador")
print()
escolha_de_modalidade = input()

while escolha_de_modalidade != "1" and escolha_de_modalidade != "2":
    print("Escolha somente entre o número 1 e 2, por favor!")
    escolha_de_modalidade = input()

if escolha_de_modalidade == "1":
    print("Você escolheu uma partida isolada")
else:
    print("Você escolheu um campeonato")

if escolha_de_modalidade == "1":

    print()
    print("***** RODADA ÚNICA *****")
    n = int(input("Quantas peças? >>> "))
    m = int(input("Limite de peças por jogada? >>> "))

    while m < 1 or n < 1:
        print("Opa, aceitamos apenas números inteiros e positivos, tenta de novo ai")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))

    while n >= 1 and m >= 1:
        if m > n:
            print("Calma ai, não se pode tirar mais peças do que as que existem")
            n = int(input("Quantas peças? "))
            m = int(input("Limite de peças por jogada? "))
        else:
            print()
            if n % (m + 1) == 0:
                print("Você começa, humano")

                usuario_escolhe_jogada(m, n)
            else:
                print("Deixa que eu começo")

                computador_escolhe_jogada(m, n)
            break

else:
    i = 1
    while i <= 3:
        print()
        print("***** RODADA " + str(i) + " de 3 *****")
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))

        while m < 1 or n < 1:
            print("Opa, aceitamos apenas números inteiros e positivos, tenta de novo ai")
            n = int(input("Quantas peças? "))
            m = int(input("Limite de peças por jogada? "))

        while n >= 1 and m >= 1:
            if m > n:
                print("Calma ai, não se pode tirar mais peças do que as que existem")
                n = int(input("Quantas peças? "))
                m = int(input("Limite de peças por jogada? "))
            else:
                print()
                if n % (m + 1) == 0:
                    print("Você começa, humano")

                    usuario_escolhe_jogada(m, n)
                else:
                    print("Deixa que eu começo")

                    computador_escolhe_jogada(m, n)
                break

        i = i + 1
    print("***** Placar Final ******")
    print()
    print("Você 0 x 3 Computador")
