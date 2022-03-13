import time



nick = str(input("qual sera o nome do Protagonista? ")) 

time.sleep(1)

print(f'\nEssa historia se passa antes da extincao da magia, ela e sobre {nick} e sua busca por conhecimento magico!\n')
time.sleep(6)

prj = int(input(f'{nick}, qual o caminho deseja seguir\n[1]-Curto\n[2]-Longo\n'))


# caminho mais curto
while prj == 1:
    print('\n'f'{nick} - Estou indo em uma aventura, em busca de um conhecimento perdido no vasto Espaco Tempo,\nsigo em frente mesmo sem saber oque irei encontrar!\n')
    time.sleep(6)
    print(f'{nick} partiu ao amanhecer para sua jornada pelos vales perdidos, indo em direcao a torre do oraculo, ao qual {nick} esperava ter a resposta de onde encontrar MERLIN O MAGO\n')
    time.sleep(12)
    print(f'{nick} estava caminhando pelo sombrio vale perdido, quando avistou ao longe uma criatura enorme meio aranha e meio Humana portando um cajado vampirico!\n')
    time.sleep(12)
    d1=int(input('enfrentar a criatura [1]\nignorar a criatura e seguir viagem[2]\n'))
    time.sleep(1)
    if d1 ==1:
        time.sleep(1)
        print(f'{nick} usou contra a criatura sua unica magia de ataque\nRAIO DE CHAMAS - exclamou {nick}\n')
        time.sleep(5)
        print(f'A criatura defendeu seu ataque! Mas antes que pudesse revidar, ouve um estrondo e no ceu surgiu um raio que atingiu em cheio a criatura a deixando atordoada e enquanto a criatura se recuperava, {nick} viu a silhueta de uma pessoa vindo em sua direcao, quando aquela pessoa se aproximou {nick} o reconheceu das historias, era MERLIN O MAGO ao qual estava procurando.\n')
        print(f'MERLIN conjurou um relampago tao forte q desintegrou a criatura!\nApos esse momento de espanto {nick} caminhou ate MERLIN para se oferecer como dicipulo e aprendiz\n assim podendo aprender novas magias e se aperfeicoar nas artes misticas as quais ele ja conhecia')
    if d1 == 2:
        time.sleep(1)
        print(f'voce descidiu seguir seu caminho e nao enfrentar a criatura')
        time.sleep(2)
        print(f'Logo a frente encontrou o fim daquele lugar sombrio')
        time.sleep(1)
        print(f'Seguiu ate encontrar uma estrutura na encosta da montanha\n')
        time.sleep(1)
        print(f'Tinha a forma de uma torre de pedra coberta de musgo e vinhas\n')
        time.sleep(1)
        print(f'voce decide explora-la!\nE ao chegar ao topo tem uma surpresa.\nencontra merlin sentado em meio a muitos de seus grimorios.')
        time.sleep(1)
        print(f'Voce se aproxima chamando seu nome " merlim " e voce\n antes mesmo de ouvir a resposta ele voi logo dispondo-se a ser seu pupilo')
        time.sleep(2)
        print(f'assim termina a historia de {nick}\nCom um belo final! ADEUS')
        break

# caminho mais longo
while prj == 2:
    time.sleep(1)
    print(f'{nick} usou contra a criatura sua unica magia de ataque\nRAIO DE CHAMAS - exclamou {nick}\n')
    time.sleep(5)
    print(f'A criatura defendeu seu ataque! Mas antes que pudesse revidar, ouve um estrondo e no ceu surgiu um raio que atingiu em cheio a criatura a deixando atordoada e enquanto a criatura se recuperava, {nick} viu a silhueta de uma pessoa vindo em sua direcao, quando aquela pessoa se aproximou {nick} o reconheceu das historias, era MERLIN O MAGO ao qual estava procurando.\n')
    print(f'MERLIN conjurou um relampago tao forte q desintegrou a criatura!\nApos esse momento de espanto {nick} caminhou ate MERLIN para se oferecer como dicipulo e aprendiz\n assim podendo aprender novas magias e se aperfeicoar nas artes misticas as quais ele ja conhecia')
    time.sleep(3)
    print(f'mas antes que {nick} pudesse aproximar-se do mago, ele desaparecera no ar do mesmo modo ao qual apareceu')
    print(f'Entao mesmo confuso {nick} seguiu viagem por entre as montanhas no vim do vale perdido')



    break