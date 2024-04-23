disciplina = input('O que você quer cotar? ')
largura = float(input('Qual é a largura do quarto? '))
comprimento = float(input('Qual é o comprimento do quarto? '))
num_quartos = int(input('Existem quantos quartos desse tamanho? '))
area = largura*comprimento
valor_unit = float(input(f'Qual é o valor por m²  de {disciplina}? '))
valor_final = area*num_quartos*valor_unit
print(f'O valor final de {disciplina} para {num_quartos} quarto(s) será de R${valor_final}.')
