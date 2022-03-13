import random

qs = 0
qs = int(input("digite [1] para jogar: "))
tt = 0
while qs == 1:
    tt = 0
    num = random.randint(10, 100)
    while tt < 3:

        tt = tt + 1

        print(tt, " chance!")

        player = int(input("chute um numero entre 10 e 100: "))
        if player > 100:
            tt = 3

        if player == num:
            print("parabens voce acertou!!!")
            break

        elif (num > player):
            print("mais")

        elif (num < player):
            print("menos")

        # elif (num != player):
        #     print("muito alto")

        if tt == 3:
            print("o numero era: ", num)
            print("mais sorte na proxima vez\n")

        print("tente novamente!\n")

    qs = int(input("digite [0]Sair ou [1]Continuar\n"))
