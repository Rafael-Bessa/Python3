import random

a = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

jogada = 0
velha = False


def computador(jogada, velha):
    if (a[0][0] == a[0][1] == a[0][2] or a[1][0] == a[1][1] == a[1][2] or a[2][0] == a[2][1] == a[2][2]) or \
            a[0][0] == a[1][0] == a[2][0] or a[0][1] == a[1][1] == a[2][1] or a[0][2] == a[1][2] == a[2][2] or \
            a[0][0] == a[1][1] == a[2][2] or a[0][2] == a[1][1] == a[2][0]:
        print("\033[1:31mAcabou\033[m")
        velha = True
    else:

        '''if (jogada == 9):
            velha = True
            print("Acabou aqui")
            print(velha)'''

        # else:
        pc = (a[random.randrange(0, 3)][random.randrange(0, 3)])
        while pc == "O" or pc == "X":
            pc = (a[random.randrange(0, 3)][random.randrange(0, 3)])
        else:

            if 4 > int(pc) > 0:
                if int(pc) == 1:
                    a[0][0] = "X"
                    print(*a, sep="\n")
                    jogada += 1
                    pessoa(jogada, velha)
                elif 2 == int(pc):
                    a[0][1] = "X"
                    print(*a, sep="\n")
                    jogada += 1
                    pessoa(jogada, velha)
                else:
                    a[0][2] = "X"
                    print(*a, sep="\n")
                    jogada += 1
                    pessoa(jogada, velha)

            elif 3 < int(pc) < 7:
                if int(pc) == 4:
                    a[1][0] = "X"
                    print(*a, sep="\n")
                    jogada += 1
                    pessoa(jogada, velha)

                elif int(pc) == 5:
                    a[1][1] = "X"
                    print(*a, sep="\n")
                    jogada += 1
                    pessoa(jogada, velha)
                else:
                    a[1][2] = "X"
                    print(*a, sep="\n")
                    jogada += 1
                    pessoa(jogada, velha)

            elif 6 < int(pc) < 10:
                if 7 == int(pc):
                    a[2][0] = "X"
                    print(*a, sep="\n")
                    jogada += 1
                    pessoa(jogada, velha)
                elif 8 == int(pc):
                    a[2][1] = "X"
                    print(*a, sep="\n")
                    jogada += 1
                    pessoa(jogada, velha)
                else:
                    a[2][2] = "X"
                    print(*a, sep="\n")
                    jogada += 1
                    pessoa(jogada, velha)

        return jogada
    return velha


def pessoa(jogada, velha):
    if (a[0][0] == a[0][1] == a[0][2] or a[1][0] == a[1][1] == a[1][2] or a[2][0] == a[2][1] == a[2][2]) or \
            a[0][0] == a[1][0] == a[2][0] or a[0][1] == a[1][1] == a[2][1] or a[0][2] == a[1][2] == a[2][2] or \
            a[0][0] == a[1][1] == a[2][2] or a[0][2] == a[1][1] == a[2][0]:
        print("\033[1:31mAcabou\033[m")
        velha = True

    if jogada == 9:
        velha = True
        print(velha)
        print("Acabou la")
    else:

        # velha == False
        while not velha:
            print("Onde você quer jogar? ")
            print(*a, sep="\n")
            print("Digite o número do local desejado ")
            x = int(input("Já pensou? Digite aqui >>> "))

            if 4 > x > 0:
                if x == 1:
                    a[0][0] = "O"
                    print(*a, sep="\n")
                    print()
                    jogada += 1
                    computador(jogada, velha)
                elif x == 2:
                    a[0][1] = "O"
                    print(*a, sep="\n")
                    print()
                    jogada += 1
                    computador(jogada, velha)
                else:
                    a[0][2] = "O"
                    print(*a, sep="\n")
                    print()
                    jogada += 1
                    computador(jogada, velha)

            elif 3 < x < 7:
                if x == 4:
                    a[1][0] = "O"
                    print(*a, sep="\n")
                    print()
                    jogada += 1
                    computador(jogada, velha)

                elif x == 5:
                    a[1][1] = "O"
                    print(*a, sep="\n")
                    print()
                    jogada += 1
                    computador(jogada, velha)
                else:
                    a[1][2] = "O"
                    print(*a, sep="\n")
                    print()
                    jogada += 1
                    computador(jogada, velha)

            elif 6 < x < 10:
                if x == 7:
                    a[2][0] = "O"
                    print(*a, sep="\n")
                    print()
                    jogada += 1
                    computador(jogada, velha)
                elif x == 8:
                    a[2][1] = "O"
                    print(*a, sep="\n")
                    print()
                    jogada += 1
                    computador(jogada, velha)
                else:
                    a[2][2] = "O"
                    print(*a, sep="\n")
                    print()
                    jogada += 1
                    computador(jogada, velha)

            if (a[0][0] == a[0][1] == a[0][2] or a[1][0] == a[1][1] == a[1][2] or a[2][0] == a[2][1] == a[2][2]) or \
                    a[0][0] == a[1][0] == a[2][0] or a[0][1] == a[1][1] == a[2][1] or a[0][2] == a[1][2] == a[2][2] or \
                    a[0][0] == a[1][1] == a[2][2] or a[0][2] == a[1][1] == a[2][0]:
                print("\033[1:31mAcabou\033[m")
                break

        return jogada
    return velha


pessoa(jogada, velha)
