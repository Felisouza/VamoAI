#Função que calcula a média da nota de cada aluno.
def media_aluno(portugues, fisica, matematica, sociologia):
    media_aluno = (portugues+fisica+matematica+sociologia)/4
    return media_aluno
    
#Calculando a nota de cada aluno
aluno1 = media_aluno(10,2.2,3,8)
aluno2 = media_aluno(10,5,5.5,9)
aluno3 = media_aluno(5,5.5,8,9)
aluno4 = media_aluno(10,10,9,8)
aluno5 = media_aluno(7,5,6,8)

#Calculando a media das notas da sala
media_sala = (aluno1+aluno2+aluno3+aluno4+aluno5)/5
print('\033[32m') #Colorir parte da string. 'A média da sala' em verde e a nota sem formatação.
print(f'A média da sala é: ' '\033[m' f'{media_sala:.2f}\n')
