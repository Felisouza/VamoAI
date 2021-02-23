##Cabeçalho
print('\033[;32m',)
print('='*60)
print(f'{"Ingressos para clube de festas":^60}')
print('='*60, '\033[m')

##Variáveis
nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
padrao = 35
vip = 60

##Algoritmo
if idade >= 18:
    entrada = input('Você deseja entrada padrão ou VIP? ')
    estudante = input('É estudante de Python? [Sim/Não] ')
    if entrada.lower() == 'padrão' or entrada.lower() == 'padrao':
        ingresso = padrao
    else:
        ingresso = vip
    if estudante.lower() == 'sim' or estudante.lower() == 's':
        desconto = 0.5
        print(
            f'\n{nome}, você escolheu o ingresso {entrada}. '
            f'Ganhou {desconto:.0%} de desconto por ser estudante de Python. '
            f'Seu ingresso ficou R${ingresso-(ingresso*desconto):.2f}\n'
            )
    else:
        print()
        print(
            f'\n{nome}, você escolheu o ingresso {entrada}. '
            f'Seu ingresso ficou R${ingresso:.2f}\n'
            )    
else:
    print(
        f'\nApenas maiores de 18 anos podem reservar ingressos para o clube de festas. '
        f'Volte daqui {18-idade} anos.\n'
        )
