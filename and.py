print('='*60)
print(f'{"Saiba em que você se transformará após a vacina":^60}')
print('='*60)
altura = float(input('Informe sua altura? '))

if altura < 2.00 and altura > 1.50:
    print('Você se transformará em um jacaré')
elif altura < 1.50:
    print('Você se transformará em lagartixa!')
else:
    print('Você se transformará em crocodilo')
print() 