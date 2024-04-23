valor_final = 0
alteracao = int(input('Quantos valores diferentes você pagou esse ano? '))
if (alteracao == 1) :
  valor = float(input('Qual foi o valor mensal? '))
  print(f'O valor total pago no final do ano foi R${valor*12}')
else :
  i = 1
  while (i <= alteracao ) :
    valor = float(input(f'Qual foi o {i}° valor pago? R$'))
    repeticao = int(input('Quantos meses tiveram esse valor? '))
    valor_final += (valor * repeticao)
    i += 1
  print(f'O valor total pago no final do ano foi R${valor_final}.')
