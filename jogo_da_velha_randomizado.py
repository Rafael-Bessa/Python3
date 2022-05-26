import random

a = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


def computador():
    if (a[0][0] == a[0][1] == a[0][2] or a[1][0] == a[1][1] == a[1][2] or a[2][0] == a[2][1] == a[2][2]) or \
            a[0][0] == a[1][0] == a[2][0] or a[0][1] == a[1][1] == a[2][1] or a[0][2] == a[1][2] == a[2][2] or \
            a[0][0] == a[1][1] == a[2][2] or a[0][2] == a[1][1] == a[2][0]:
        print("\033[1:31mAcabou\033[m")
        print("\033[1:36mHumano Venceu\033[m")

    else:
        jogo = True
        pc = (a[random.randrange(0, 3)][random.randrange(0, 3)])

        if pc == "O" or pc == "X":
            if ((a[0][0] == "X" or a[0][0] == "O") and (a[0][1] == "X" or a[0][1] == "O") and
                    (a[0][2] == "X" or a[0][2] == "O") and (a[1][0] == "X" or a[1][0] == "O")
                    and (a[1][1] == "X" or a[1][1] == "O") and (a[1][2] == "X" or a[1][2] == "O") and (
                            a[2][0] == "X" or a[2][0] == "O") and (a[2][1] == "X" or a[2][1] == "O")
                    and (a[2][2] == "X" or a[2][2] == "O")):
                print("\033[1:31mDEU VELHA!\033[m")
                jogo = False

            else:
                while True:
                    pc = (a[random.randrange(0, 3)][random.randrange(0, 3)])
                    if pc == "O" or pc == "X":
                        continue
                    else:
                        pc = int(pc)
                        break
        if jogo:
            pc = int(pc)
            if 4 > pc > 0:
                if int(pc) == 1:
                    a[0][0] = "X"
                    print(*a, sep="\n")
                    pessoa()
                elif 2 == int(pc):
                    a[0][1] = "X"
                    print(*a, sep="\n")
                    pessoa()
                else:
                    a[0][2] = "X"
                    print(*a, sep="\n")
                    pessoa()

            elif 3 < pc < 7:
                if int(pc) == 4:
                    a[1][0] = "X"
                    print(*a, sep="\n")
                    pessoa()

                elif int(pc) == 5:
                    a[1][1] = "X"
                    print(*a, sep="\n")
                    pessoa()
                else:
                    a[1][2] = "X"
                    print(*a, sep="\n")
                    pessoa()

            elif 6 < int(pc) < 10:
                if 7 == int(pc):
                    a[2][0] = "X"
                    print(*a, sep="\n")
                    pessoa()
                elif 8 == int(pc):
                    a[2][1] = "X"
                    print(*a, sep="\n")
                    pessoa()
                else:
                    a[2][2] = "X"
                    print(*a, sep="\n")
                    pessoa()


def pessoa():
    if (a[0][0] == a[0][1] == a[0][2] or a[1][0] == a[1][1] == a[1][2] or a[2][0] == a[2][1] == a[2][2]) or \
            a[0][0] == a[1][0] == a[2][0] or a[0][1] == a[1][1] == a[2][1] or a[0][2] == a[1][2] == a[2][2] or \
            a[0][0] == a[1][1] == a[2][2] or a[0][2] == a[1][1] == a[2][0]:
        print("\033[1:31mAcabou\033[m")
        print("\033[1:34mComputador Venceu\033[m")

    else:
        print("Onde você quer jogar? ")
        print(*a, sep="\n")
        print("Digite o número do local desejado ")
        x = int(input("Já pensou? Digite aqui >>> "))

        if 4 > x > 0:
            if x == 1:
                a[0][0] = a[0][0].replace("1", "O")
                print(*a, sep="\n")
                print()
                computador()
            elif x == 2:
                a[0][1] = a[0][1].replace("2", "O")
                print(*a, sep="\n")
                print()
                computador()
            else:
                a[0][2] = a[0][2].replace("3", "O")
                print(*a, sep="\n")
                print()
                computador()

        elif 3 < x < 7:
            if x == 4:
                a[1][0] = "O"
                print(*a, sep="\n")
                print()
                computador()

            elif x == 5:
                a[1][1] = "O"
                print(*a, sep="\n")
                print()
                computador()
            else:
                a[1][2] = "O"
                print(*a, sep="\n")
                print()
                computador()

        elif 6 < x < 10:
            if x == 7:
                a[2][0] = "O"
                print(*a, sep="\n")
                print()
                computador()
            elif x == 8:
                a[2][1] = "O"
                print(*a, sep="\n")
                print()
                computador()
            else:
                a[2][2] = "O"
                print(*a, sep="\n")
                print()
                computador()


pessoa()
