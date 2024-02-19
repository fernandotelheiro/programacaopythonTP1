""" Desenvolva um programa que aplique descontos diferentes com base no valor da compra: desconto de 10% para compras acima de R$100, 15% para compras acima de R$200, etc. """
valor = int(input("Digite o valor de sua compra: "))
if valor>=100:
    print('Desconto de 10% adquirido!')
    print(f'valor atual é de {valor * (10 / 100)}')
if valor>=200:
    print('Desconto de 15% adquirido!')
    print(f'valor atual é de {valor * (15 / 100)}')
