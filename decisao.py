import random
import time

start = 0
start = int(input("deseja iniciar?\nsim[1] nao[0]\n"))
while start == 1:
    time.sleep(1)
    input("qual sua duvida?")
    resp = ["Sim, Vai la!", "Claro! por que nao?", "Com certeza!", "Sim!", "Nao!",
            "Talves seja melhor Nao!", "Melhor nao!", "Outro dia!", "Em breve!", "Espere."]
    rp = random.choice(resp)
    print(rp, "\n")
    time.sleep(2)
    start = int(input("\nmais alguma duvida?\n[1]Sim\n[0]Nao\n\n"))
    if start == 0:
        print("\nO AJUDANTE agradece a confianca!\nAte breve.\n")
