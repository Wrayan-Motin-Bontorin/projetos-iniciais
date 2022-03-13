import random

print("Ola!\nBem Vindo ao Dado Eletronico\nSelecione uma opcao!")
RR = int(input("Sair [0]     Jogar [1]\n"))
if RR > 1:
    print("\nEste numero nao e valido!\nPor favor reinicie o \nscript e tente novamente\n\n")
while RR == 1:
    lados = random.randint(1, 6)

    if RR == 1:
        print(f'o numero e {lados}')

    elif RR == 0:
        print("muito obrigado por usar o DADO ELETRONICO")

    RR = int(input("Sair [0]     Jogar novamente [1]\n"))

    if RR > 1:
        print("\nEste numero nao e valido!\nPor favor reinicie o \nscript e tente novamente\n\n")