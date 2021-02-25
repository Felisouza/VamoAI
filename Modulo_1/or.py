mascara = input('Você sempre sai de máscara? ')
isolamento = input('Você está fazendo o isolamento social? ')

if mascara.lower() == 'sim' or isolamento.lower() == 'sim' or mascara.lower() == 's' or isolamento.lower() == 's':
    print('Parabéns! Continue se cuidando contra a Covid19!')
else:
    print('Você deveria se cuidar mais contra a Covid19')

