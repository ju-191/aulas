salario = float(input('Qual é o seu salário bruto? R$'))

#Cálculo do desconto de INSS
if salario <= 1412:
  inss = salario * 0.075
elif salario <= 2666.68:
  inss = salario * 0.09 - 21.18
elif salario <= 4000.03:
  inss = salario * 0.12 - 101.18
elif salario <= 7786.02:
  inss = salario * 0.14 - 181.18
else:
  inss = 908.86

print(f'O desconto de INSS é de R${round(inss,2)}.')

salario -= inss

#Cálculo do desconto do IR
if salario <= 2259.20:
  ir = 0
elif salario <= 2826.65:
  ir = salario * 0.075 - 169.44
elif salario <= 3751.05:
  ir = salario * 0.15 - 381.44
elif salario <= 4664.68:
  ir = salario * 0.225 - 662.77
else:
  ir = salario * 0.275 - 896

print(f'O desconto do IR é de R${round(ir,2)}')
salario -= ir
print(f'O seu salário líquido é de R${round(salario,2)}')
