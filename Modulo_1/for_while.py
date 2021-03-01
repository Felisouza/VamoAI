login = input('Digite seu login: ')
senha = input('Digite sua senha: ')

while login != 'vamoai' or senha != '123':
    print('Acesso negado! ')
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
print('Acesso autorizado')

cont = 0
for i in range (1,11):
    cont += 2
    print(cont)
