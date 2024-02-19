""" Desenvolva um programa que verifique se uma palavra ou frase inserida pelo usuário é um palíndromo (lê-se igual de trás para frente). """
palavra = input(f'Digite sua palavra para checar se é um palíndromo: ')

palavra = palavra[0].lower() + palavra[1:] #concatenando primeira letra em lower case + resto da palavra
print(palavra)
palavra = list(palavra)
inverso = palavra.copy()
inverso.reverse()
print(inverso)
print(palavra)
if palavra == inverso:
    print('Sim! A palavra é um palíndromo!!')

