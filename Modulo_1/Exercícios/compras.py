##Cabeçalho
print('\033[;32m')
print('='*60)
print(f'{"Vamos as compras":^60}')
print('='*60, '\033[m')

##Variáveis
produto1 = input('Qual o nome do primeiro produto? ')
preco1 = float(input('Qual o valor do primeiro produto? '))
produto2 = input('Qual o nome do segundo produto? ')
preco2 = float(input('Qual o valor do segundo produto? '))
produto3 = input('Qual o nome do terceiro produto? ')
preco3 = float(input('Qual o valor do terceiro produto? '))

##Algoritmo
if preco1 < preco2 and preco1 < preco3:
    barato = preco1
    barato_nome = produto1
elif preco2 < preco1 and preco2 < preco3:
    barato = preco2
    barato_nome = produto2
else:
    barato = preco3
    barato_nome = produto3
print(f'\nO produto mais barato é {barato_nome}, pois custa apenas R${barato:.2f}\n')

