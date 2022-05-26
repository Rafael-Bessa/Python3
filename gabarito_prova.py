"""Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao
aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
aluno vai utilizar o sistema. Após todos os alunos terem respondido informar: - Maior e Menor Acerto; - Total de
Alunos que utilizaram o sistema; - A Média das Notas da Turma. - Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A"""

print(30 * "*")
print(30 * "~")
respostas = []
gabarito = "ABCDEEDCBA"
acertou = 0
usando = True
banco_dados = []
media = 0

while usando:
    nome = input("Qual o nome do aluno? >>> ")
    nome = nome.title()

    for nota in range(1, 11):
        respostas.append(input(f"O que colocou na questão {nota} ? >>> "))
        respostas_arrumadas = "".join(respostas)
        respostas_arrumadas = respostas_arrumadas.upper()

        if gabarito[nota - 1] == respostas_arrumadas[nota - 1]:
            print(f"Acertou a questão de número {nota}")
            acertou += 1
        else:
            print(f"Errou a questão de número {nota}")

    print(f"O aluno \033[1:32m{nome}\033[m acertou ao todo {acertou} questão(ões)")
    print()
    continuar = input("Outro aluno vai usar o programa agora? Digite 1 para SIM ou 2 para NÃO >>> ")
    if continuar == "1":
        usando = True
        banco_dados.append((nome, acertou))
        acertou = 0
        respostas = []
    elif continuar == "2":
        usando = False
        banco_dados.append((nome, acertou))
    else:
        print("Digite somente 1 ou 2")
        banco_dados.append((nome, acertou))
        print("Recomece o programa")
        usando = False

print()
print(banco_dados)
print(f"O número de alunos que usaram o sistema foi \033[1:32m{len(banco_dados)}\033[m")

for i in range(0, len(banco_dados)):
    media = media + (banco_dados[i][1])

print(f"E a média das notas foi: \033[1:32m{media / len(banco_dados)}\033[m")
