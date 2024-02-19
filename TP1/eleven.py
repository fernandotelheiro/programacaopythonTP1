""" Faça um programa que simule o lançamento de um dado. O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados. """

from random import randint
rand_num = randint(1,6)
qtd_dados = int(input('Digite quantos dados quer jogar nesta rodada: '))
if qtd_dados>0:
    for n in range(qtd_dados):
        print(f'O dado número {n+1} apresentou o valor de: {rand_num}')
        rand_num = randint(1,6)
