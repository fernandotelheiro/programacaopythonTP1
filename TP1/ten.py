""" Escreva um programa que combine elementos aleatórios de listas diferentes (personagens, ações, locais) para criar uma história curiosa.  """
from random import randint
rand_num = randint(0,2)

personagens = ['João', 'Carlos', 'Maria']
acoes = ['pescou','dançou','dormiu']
locais = ['na praia', 'na discoteca','no parque']

perso = personagens[rand_num]
rand_num = randint(0,2)

action = acoes[rand_num]
rand_num = randint(0,2)

location = locais[rand_num]
print(f'{perso} {action} {location}')

