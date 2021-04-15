idades = {'Felipe': 29, 'Lina': 25, 'Arthur': 4, 'Julia':53, 'Rafael': 33, 'Renata': 32, 'Luiza': 2}
sexo = {'Felipe': 'masculino', 'Lina': 'feminino', 'Arthur': 'masculino', 'Julia':'feminino', 'Rafael': 'masculino', 'Renata': 'feminino'}
escolaridade = {'Felipe': 'superior completo', 'Lina': 'superior completo', 'Arthur': 'pré escola', 'Julia':'superior incompleto', 'Rafael': 'superior completo', 'Renata': 'superior completo'}

#criando um novo didionário, pegando elemento de outros dois dicionários.
Felipe = {idades['Felipe'], sexo['Felipe']}

#adicionando um novo elemento num dicionário já existente
idades['Guilherme'] = 25

#Adicionando várias chaves e valores de uma só vez. Unindo 2 dicionários para complementar o primeiro.
idades2 = {'Lourdes': 52, 'Carlos': 59, 'Karina': 30, 'Bianca': 26, 'Gabriel': 18}
idades.update(idades2)

#Testando métodos
idades.pop('Guilherme')
print(idades.get('Felipe'))
print(idades.items())
print(idades.keys())
print(idades.values())

habilidade = {
    f"Cloroquiner": "Cloroquina não é eficaz contra o Corona Vírus, muito menos contra reptilianos\n",
    f"Ivermectiner": 'Ivermectina não é eficaz contra o Corona Vírus, muito menos contra reptilianos\n',
    f"Chazinho de gengibrer": 'Chá de gengibre é uma delícia, mas não é eficaz contra Corona vírus muito menos contra reptilianos\n'}

vitoria_derrota = {
    f'derrota': '\33[91m\nVocê perdeu!\33[m\nEla estava te enganando o tempo todo!\nEla é a rainha dos reptilianos!\nVocê se descuidou e ela te transformou em jacaré!\n',
    f'vitoria': '\n\33[92m\nParabéns você ganhou!\33[m\nEla era a rainha dos reptilianos e queria te transformar em jacaré!\nMas, vc é muito inteligente e não deixou!\nVocê não se deixa enganar por qualquer um!\n'
    }
