# Escreva um algoritmo que leia três números inteiros e posiAvos (a, b, c por exemplo) e calcule a seguinte expressão:
# 𝑑 = (r+s) / 2, onde
# 𝑟 = (𝑎 + 𝑏)^2 e 𝑠 = (𝑏 + 𝑐)^2

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c= '))

r = (a + b)**2
s = (b + c)**2
print(r, s)
print(f'Resultado da equação = {(r + s)/2}')

# Ler um caractere e imprimir se é: um dígito (0-9), letra maiúscula (A-Z), letra minúscula (a-z),espaço ou outro símbolo.
# Para a solução uAlizar o código ASCII dos caracteres.

c = input('Caracter: ')
if 47 < ord(c) < 58:
  print(f'{c} é um dígito.')
elif 64 <  ord(c) < 91:
  print(f'{c} é uma letra maiúscula.')
elif 96 < ord(c) < 123:
  print(f'{c} é uma letra minúscula.')
elif ord(c) == 32:
  print(f'O caracter digitado é um espaço.')
else:
  print(f'O caracter digitado é outro símbolo.')

  #Um sistema de equações lineares da forma:
# 𝑎𝑥 + 𝑏𝑦 = 𝑐
# 𝑑𝑥 + 𝑒𝑦 = 𝑓
# Pode ser resolvido uAlizando-se as seguintes fórmulas
# 𝑥 = (ce-bf)/(ae-bd)
# e
# y = (af-cd) / ae-bd)
# Ler o conjunto de coeficientes (a, b, c, d, e, f) e imprimir a solução x e y.
# Antes de efetuar a divisão, verificar se ela pode ser feita. Em caso negaAvo, imprimir uma mensagem de que o sistema não tem solução.

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
d = float(input('d = '))
e = float(input('e = '))
f = float(input('f = '))

if (a*e - b*d) == 0:
  print('O sistema não tem solução.')
else:
  print(f'x = {(c*e - b*f)/(a*e - b*d)} e y = {(a*f - c*d)/(a*e - b*d)}')

  # Escreva um programa que leia 2 valores (a e b), calcule e imprima o resultado do somatório:

a = int(input('a = '))
b = int(input('b = '))
soma = 0

for i in range(1, a + 1):
  for j in range(1, b + 1):
    soma += (a*b) * ((j+i)**2)

print(f'Resultado = {soma}')

# Construir um programa que faz leitura de N números inteiros, onde N também deve ser lido, e imprime apenas o Maior entre eles.

n = int(input('São quantos números? '))
lista = []

for i in range(n):
  num = int(input(f'Número {i+1}: '))
  lista.append(num)

print(f'O maior número é {max(lista)}')

# Elabore um algoritmo que receba, inicialmente, o valor de uma aplicação e de uma taxa de juros.
# Considerando que essa taxa de juros aumenta na razão de 0,025% ao mês, então armazene em vetores, com 12 elementos cada,
# o valor das taxas de juros, o valor dos juros e o valor da aplicação corrigida.
# Após, mostre o valor inicial da aplicação e o conteúdo dos vetores.

aplicacao = float(input('Valor da aplicação = '))
tx_juros = float(input('Taxa de juros inicial = '))
taxa = [0]*12
juros = [0]*12
ap_corrigida = [0]*12

for i in range (12):
  taxa[i] = round(tx_juros + 0.025*i, 3)
  juros[i] = round(aplicacao*(taxa[i]/100), 3)
  ap_corrigida[i] = round(aplicacao + juros[i], 2)

print(f'Valores anuais: \n Taxas: {taxa} \n Juros: {juros} \n Aplicação corrigida: {ap_corrigida}')

# Uma loja de automóveis comercializa sete marcas de veículos, sendo quatro nacionais e três importadas. Os veículos são idenAficados pelos códigos conAdos na tabela abaixo.
# Elabore um algoritmo, para acumular as vendas de cada veículo, por código.
# Procedimentos para cada veículo:
# a. Solicite e leia o Código do Veículo. Cada entrada de um código é relaAva à venda de uma unidade da marca.
# Atenção! O programa deverá encerrar quando o Código de Veículo informado for igual a Zero.
# b. Valide o Código do Veículo, que deve estar entre 1 e 7, inclusive, caso contrário, envie mensagem de erro: “Erro: Código do Veículo deve estar entre 1 e 7, inclusive!”,
# e solicite/leia/valide o código do veículo novamente.
# Após encerrar a entrada de dados sobre as vendas de veículos (ou seja, quando Código de Veículo for igual a Zeros), mostre os seguintes dados, de cada uma das oito marcas,
# somente se houve vendas da marca: Descrição da marca; Classe da marca; Total de veículos vendidos da marca.
# Após mostrar as vendas de todas as marcas, mostre: O total de veículos nacionais vendidos; o total de veículos importados vendidos; e o total geral de veículos vendidos
# (Nacionais + Importados)

codigo = 1
nacionais = 0
importados = 0
total = 0
entrada = []
carros = [0]*7
tabela = [['Ford', 'Nacional'], ['Toyota', 'Nacional'], ['Fiat', 'Nacional'], ['Volkswagen', 'Nacional'], ['Ferrari', 'Importado'], ['Mercedes', 'Importado'], ['Rolls Royce', 'Importado']]

#calcular total de código vendido
while codigo != 0:
  codigo = int(input('Código do Veículo: '))
  if 1 <= codigo <= 7:
    entrada.append(codigo)
  elif codigo == 0:
   print('Validação concluída.')
  else:
    print('Erro: Código do Veículo deve estar entre 1 e 7, inclusive!')

print(entrada)

# somar total de cada código
for n in entrada:
  carros[n-1]+= 1

print(carros)

# imprimir carros vendidos
for i in range(7):
  if carros[i] != 0:
    print(f'Descrição: {tabela[i][0]}, Classe: {tabela[i][1]}, Número vendido: {carros[i]}')

  if i < 4:
    nacionais += carros[i]
  else:
    importados += carros[i]

# imprimir totais
print(f'Nacionais vendidos: {nacionais}, Importados vendidos: {importados}, Total: {nacionais + importados}')

# Elabore uma função que receba um determinado valor em Graus Fahrenheit, e retorne o valor correspondente em Graus Celsius.
# A fórmula para conversão de Graus Fahrenheit para Celsius é:
# 𝐺𝑟𝑎𝑢𝑠𝐶𝑒𝑙𝑐𝑖𝑢𝑠 = 5 ∗ (𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 − 32)/9

def fahrenheit_celsius(fahrenheit):
  celsius = 5 * (fahrenheit - 32) / 9
  return round(celsius, 2)

# Elabore uma função que receba um determinado valor em Graus Fahrenheit, e retorne o valor correspondente em Graus Celsius.
# A fórmula para conversão de Graus Fahrenheit para Celsius é:
# 𝐺𝑟𝑎𝑢𝑠𝐶𝑒𝑙𝑐𝑖𝑢𝑠 = 5 ∗ (𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 − 32)/9

def fahrenheit_celsius(fahrenheit):
  celsius = 5 * (fahrenheit - 32) / 9
  return round(celsius, 2)

# Construa uma função que retorne o MDC – máximo divisor comum, de dois números informados
# (o máximo divisor comum de dois números informados é o maior número que os divide).

def mdc(x, y):
  for i in range(x, 1, -1):
    if (x % i == 0 and y % i ==0):
      return i
      break

print(mdc(6,12))
