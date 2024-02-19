""" Crie um programa que classifique as palavras inseridas pelo usuário como curtas (menos de 5 letras) ou longas (5 letras ou mais). """
x = input('Digite a palavra a ser medida: ')
status = ''
chars = (len(x))
print(chars)
if chars < 5:
    status = 'curta'
    print(status)
if chars > 5:
    status = 'longa'
    print(status)
print(f'A palafra {x} possui {chars} de letras. Logo, ela é considerada {status} ')