""" Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão) e dois números, e então execute a operação escolhida com os números. """
print("""
        --Menu--
        (1)Adiçao
        (2)Subtração
        (3)Multiplicação
        (4)Divisão
        -------------
        """)
command = int(input('Digite o número da operação que deseja: '))

def command_line():
    if command == 1:
        adicao()
    elif command == 2:
        subtracao()       
    elif command == 3:
        multiplicacao()
    elif command == 4:
        divisao()    
    else:
        print("Opcão inválida. Programa terminado.")

def adicao():
    print('Voce escolheu adição!') 
    x=int(input('Digite o primeiro número da operação: '))
    y=int(input('Digite o segundo número da operação: '))
    print(f'A soma de ({x}) + ({y}) resulta em: {x+y}')
    
def subtracao():
    print('Voce escolheu subtração!') 
    x=int(input('Digite o primeiro número da operação: '))
    y=int(input('Digite o segundo número da operação: '))
    print(f'A subtração de ({x}) - ({y}) resulta em:  {x-y}')

def multiplicacao():
    print('Voce escolheu multiplicação!') 
    x=int(input('Digite o primeiro número da operação: '))
    y=int(input('Digite o segundo número da operação: '))
    print(f'A multiplicação entre ({x}) e ({y}) resulta em:  {x*y}')    
    
def divisao():
    print('Voce escolheu divisão!') 
    x=int(input('Digite o primeiro número da operação: '))
    y=int(input('Digite o segundo número da operação: '))
    print(f'A divisão entre ({x}) e ({y}) resulta em:  {int(x/y)}')      
    
    
command_line()