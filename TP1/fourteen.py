""" Escreva um programa que permita ao usuário votar em três opções diferentes e, no final, exiba o número de votos de cada opção """
amarelo = 0
azul = 0
vermelho = 0 

amarelo = 0
azul = 0
vermelho = 0 

def exibir_menu():
    print(f'''
      --Menu--
      (1) Vote em Azul  -- Atualmente com {azul}
      (2) Vote em Amarelo -- Atualmente com {amarelo}
      (3) Vote em Vermelho -- Atualmente com {vermelho}
      (4) Para sair da votação.
      ''')

def pedir_voto():
    global amarelo, azul, vermelho, status
    try:
        voto = int(input('Digite seu voto:'))
        if voto == 1:
            azul += 1
        if voto == 2:
            amarelo += 1
        if voto == 3:
            vermelho += 1
        if voto == 4:
            print(f'Você encerrou a votação! \n Os votos finais foram:\n Azul: {azul}\n Amarelo: {amarelo}\n Vermelho: {vermelho} ')
            print('\n--Sistema de votos encerrado--\n')
            raise SystemExit
    except:
        print('Opção invalida \n')
        input('Digite qualquer tecla e volte ao menu: ')
exibir_menu()

while True:
    pedir_voto()
    exibir_menu()
