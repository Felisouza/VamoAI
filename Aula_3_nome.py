nome = 'Felipe Batista'
animal_estimacao = 'Theo'
comida_favorita = 'Hamburguer'
pais = 'França'
idade = 29
altura = 1.82

print('\033[1;33m')
print(f'{"Atividade 1":^70}')
print()
print('\033[35m' 'Olá, meu nome é %s, tenho um gatinho chamado %s,'%(nome,animal_estimacao))
print('gosto muito de comer %s, gostaria muito de visitar a %s,'%(comida_favorita,pais))
print('tenho %d anos e %.2fm de altura.'%(idade,altura), '\033[m')

print()