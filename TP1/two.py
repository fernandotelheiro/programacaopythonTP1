""" Faça um programa que converta um número fornecido de minutos em horas e minutos, e depois faça o inverso, convertendo horas e minutos de volta para minutos totais. """

def minutos_para_horas_e_minutos(total_minutos):
    """ Recebe um número total de minutos e retorna o equivalente em horas e minutos. """
    horas = total_minutos // 60
    minutos = total_minutos % 60
    return horas, minutos

def horas_e_minutos_para_minutos(horas, minutos):
    """ Recebe o número de horas e minutos e retorna o total de minutos correspondentes. """
    total_minutos = horas * 60 + minutos
    return total_minutos

# Conversão de minutos para horas e minutos
total_minutos = int(input('Digite o total de minutos que serão transformados em horas e minutos: '))
horas, minutos = minutos_para_horas_e_minutos(total_minutos)
print('***********')
print(f'{total_minutos} minutos correspondem a {horas} horas e {minutos} minutos.')
print('***********\n')
print('--Agora a segunda parte--\n')

# Conversão de horas e minutos para minutos totais
horas = int(input('Digite o total de horas: '))
minutos = int(input('Digite o total de minutos: '))
total_minutos = horas_e_minutos_para_minutos(horas, minutos)
print('***********')
print(f'{horas} horas e {minutos} minutos correspondem a {total_minutos} minutos.')
print('***********\n')
