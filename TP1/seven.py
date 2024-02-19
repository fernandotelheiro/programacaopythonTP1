""" Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso). """

#programa feito em aula.

# Entrada dos dados
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m):"))

# Processamento
imc = peso / (altura**2)

# Classificação do resultado
if imc < 18.5:
    resultado = "baixo peso"

elif imc >= 18.5 and imc < 25:
    resultado = "peso adequado"

elif imc >= 25 and imc < 30:
    resultado = "sobrepeso"

else:
    resultado = "obesidade"

# Saída do dado
print(f"O seu IMC está em {imc}, classificando-o como {resultado}.")

