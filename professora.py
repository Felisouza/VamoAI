'''Uma professora deseja desenvolver um sistema para automatizar seu trabalho. 
    Ela precisa criar uma solução onde seus alunosconsigam inserir suas notas
    (seja a média geral de todas asmatérias ou a média de uma única disciplina),
    receber a média, esaber sua situação (aprovação, reprovação ou recuperação).'''

##Função que retorna a média de 4 matérias
def media_geral(nota_matematica, nota_história, nota_sociologia, nota_português):
    return (nota_história + nota_matematica + nota_português + nota_sociologia)/4

##Função que define se o aluno está aprovado, de recuperação ou reprovado.
def situacao(nota):
    if nota > 6 and nota <= 10:
        return print('\nParabéns, você foi aprovado\n')
    elif nota >= 4 and nota < 6:
        return print('\nVocê precisa estudar mais, está de recuperação\n')
    else:
        return print('\nUma pena, você foi reprovado\n')

##Cabeçalho que pede a informação do usuário, se quer informar a média de uma matéria ou de 4.
print('='*60)
print(
    f'{"Digite 1 para média geral":^60}',
    f'{"Digite 2 para média de uma matéria":^60}',
     sep='\n')
print('='*60)
geral_unitario = float(input(''))

##O algorítimo em si. Chama as duas funções acima, caso queira a média geral ou apenas a função da situação do aluno
##Descobri fuçando que poderia colocar input dentro dos parâmetros da função!!
if geral_unitario == 2:
   situacao(float(input('Digite a média da matéria: ')))
else:
    geral = media_geral(
    nota_matematica = float(input('Digite a nota de matemática: ')),
    nota_história = float(input('Digite a nota de matemática: ')),
    nota_sociologia = float(input('Digite a nota de matemática: ')),
    nota_português = float(input('Digite a nota de matemática: '))
    )
    situacao(geral)

