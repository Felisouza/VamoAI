n1 = 1024
n2 = 2048

soma = n1+n2
multi = n1*n2
div = n2/n1
sub = n2-n1

print('\033[1;35m')
print(f'{"Atividade 2":^70}')
print('\033[33m')
print('A soma entre %d e %d é: %d.'%(n1,n2,soma))
print('A multiplicação entre %d e %d é: %d.'%(n1,n2,multi))
print('A divisão entre %d e %d é: %d.'%(n2,n1,div))
print('A subtração entre %d e %d é: %d.'%(n2,n1,sub))
print('\033[m')
