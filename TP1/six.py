""" Escreva um programa onde o usuário deve adivinhar um número secreto. O programa deve dizer se o palpite está correto, muito alto ou muito baixo. """
#programa feito em aula.
from random import randint
pc_num = randint(0,9)

tentativas = 3

while tentativas > 0:
  user_num = int(input('Escolha um número de 0 a 9:'))

  if user_num == pc_num:
    print('parabens!')
    break
  else:
    if user_num < pc_num:
      print('O número secreto é maior.')
    else:
      print('O número secreto é menor')

  tentativas -= 1

  print(f'Agora você tem {tentativas} tentativa(s)!')

print('Você gastou todas as tentativas e perdeu!')