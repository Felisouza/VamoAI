tomate1 = float(input('Qual foi o valor do quilo do tomate há um ano atrás? '))
tomate2 = float(input('Qual é valor do quilo do tomate hoje? '))
diferenca = tomate2-tomate1
inflacao = int(diferenca*100)/tomate1

print()
print(f'A diferença do quilo do tomate foi de R${diferenca:.2f}')
print(f'A inflação no período foi de {inflacao:2.2%}')
print()