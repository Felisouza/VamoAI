##Cabeçalho
print('\033[;31m')
print('='*90)
print(f'{"Irmã Mary Kenneth Keller":^90}')
print('='*90, '\033[m')

#Variaveis
pontuacao = 0
texto = "Irmã Mary Kenneth Keller foi uma das primeiras pessoas a receber o título de doutorado em ciências da computação nos EUA. Sendo a primeira mulher do país a alcançar tal feito. \nFoi uma das principais desenvolvedoras da linguagem BASIC (Beginner's All-purpose Symbolic Instruction Code). Uma linguagem voltada para o ensino. Criada com uma linguagem mais próxima a nossa a fim de facilitar a aprendizagem. E ampliar o campo de ensino para além dos campos da ciência e da matemática. \nSeu foco, de sua carreira, foi o ensino de tecnologia para as pessoas. Ela fomentou a inserção de mais mulheres nesse campo e trabalhou duro para que todos pudessem ter acesso a esse conhecimento."

##Pergunta 1
print('\033[;1m')
print('Ela foi a primeira mulher a receber titulação de douturado em ciencias de computação? ', '\033[m')
print(
    f'1) Sim, ganhou a titulação na universidade de  Universidade Washington em St. Louis \n' 
    f'2) Não, ela não chegou a tanto \n'
    f'3) Sim, e foi uma das primeiras pessoas a receber a titulação no país, em 1965 \n'
    )
pergunta1 = int(input('Digite o número da alternativa correta: \n'))
if pergunta1 == 1 or pergunta1 == 3:
    print('Certa resposta!!')
    pontuacao += 1
else:
    print('Infelizmente você errou! =( ')

##Pergunta 2
print('\033[;1m')
print('Ela foi uma das criadoras da linguagem BASIC. Uma linguagem que:', '\033[m')
print(
    f'1) Usada por estudantes que estavam começando a aprender sobre programação \n' 
    f'2) Utilizada por décadasd para fins didáticos. \n'
    f'3) O embrião da linguagem Visual Basic. \n'
    )
pergunta2 = int(input('Digite o número da alternativa correta: \n'))

if pergunta2 == 1 or pergunta2 == 2:
    print('Certa resposta!!')
    pontuacao += 1
else:
    print('Infelizmente você errou! =( ')

##Pergunta 3
print('\033[;1m')
print('A Irmã Mary Kenneth Keller acreditava que:', '\033[m')
print(
    f'1) A programação deveria ser ampliada. Não deveria ficar restrita apenas ao \n campo matemático e científico \n' 
    f'2) Todos deveriam ter acesso ao ensino de tecnologia e incentivou o ingresso de mulheres na área. \n'
    f'3) O ensino de tecnologia deveria ser algo restrito para homens das altas classes sociais. \n'
    )
pergunta3 = int(input('Digite o número da alternativa correta: \n'))

if pergunta3 == 1 or pergunta3 == 2:
    print('Certa resposta!!')
    pontuacao += 1
else:
    print('Infelizmente você errou! =( ')

##Algoritmo
if pontuacao == 3:
    print(f'Parabéns, você acertou todas as questões! \n \n', texto)
elif pontuacao == 2 or pontuacao == 1:
    print(f'Você acertou {pontuacao}! \n \n', texto)
else:
    print(
        f'Você não acertou nenhuma questão, mas \n'
        f'não desanime! Vamos aprender mais sobre a Irmã Mary Kenneth Keller \n \n ', texto
        )
    print('Mais um teste')


