import random

nome = ''
classe_escolhida = ''
aventura_escolhida = ''

def pedir_nome():
    global nome
    nome = input('Digite seu nome: ')

def escolher_classe():
    global classe_escolhida
    print(f'Olá, {nome}!')
    print('Escolha sua classe:')
    print('(1) Cavaleiro')
    print('(2) Mago')
    print('(3) Paladino')
    escolha = int(input('Digite o número correspondente à classe desejada: '))
    if escolha == 1:
        classe_escolhida = 'Cavaleiro'
    elif escolha == 2:
        classe_escolhida = 'Mago'
    elif escolha == 3:
        classe_escolhida = 'Paladino'

def escolher_aventura():
    global aventura_escolhida
    print(f'Parabéns! Você é um {classe_escolhida}!')
    print('Agora, escolha sua aventura:')
    print('(1) Roubar o tesouro na caverna do Dragão')
    print('(2) Salvar a princesa das garras do malvado vilão Mau')
    print('(3) Ir à taverna')
    escolha = int(input('Digite o número correspondente à aventura desejada: '))
    if escolha == 1:
        aventura_escolhida = 'Roubar o tesouro na caverna do Dragão'
    elif escolha == 2:
        aventura_escolhida = 'Salvar a princesa das garras do malvado vilão Mau'
    elif escolha == 3:
        aventura_escolhida = 'Ir à taverna'

def jogar():
    if aventura_escolhida == 'Roubar o tesouro na caverna do Dragão':
        dado = random.randint(1, 20)
        print(f'Você rolou o dado e obteve {dado}.')
        if dado >= 15:
            print('Você conseguiu!! O dragão estava velho já e derrota-lo foi fácil! Toda sua fortuna agora é sua.')
        elif dado <= 5:
            print('Você não tinha chances... O dragão te comeu.')
        else:
            print('Lutar contra o dragão foi exaustivo mas você conseguiu! Agora está sem um braço mas está rico!!')
    elif aventura_escolhida == 'Salvar a princesa das garras do malvado vilão Mau':
        dado = random.randint(1, 20)
        print(f'Você rolou o dado e obteve {dado}.')
        if dado >= 15:
            print('Você conseguiu!! Salvou a princesa, ela é LINDA e ainda te deu um beijo de amor verdadeiro! Acho que alguém vai ser um Rei beeem feliz!')
        elif dado <= 5:
            print('Ao subir o castelo do malvado vilão Mau, to último degrau você escorrega e cai lá de cima. Que azar!')
        else:
            print('É errr, o malvado vilão mau acabou sendo bem fortinho... mas tudo bem. Você o derrotou e beijou a princesa. Mas ela tinha bafo.')
    elif aventura_escolhida == 'Ir à taverna':
        dado = random.randint(1, 20)
        print(f'Você rolou o dado e obteve {dado}.')
        if dado >= 15:
            print('Todos seus companheiros estavam lá te esperando para uma rodada de graça!!')
        elif dado <= 5:
            print('Assim que você entra na taverna um Ogro estava passando mal e te vomita inteiro.')
        else:
            print('Você estava devendo uma rodada aos seus companheiros que estavam lá... errr acontece.')

pedir_nome()
escolher_classe()
escolher_aventura()
jogar()
