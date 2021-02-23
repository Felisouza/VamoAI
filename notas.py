nota_port = float(input('Digite sua nota de português: '))
nota_mat = float(input('Digite sua nota de matemática: '))
nota_bio = float(input('Digite sua nota de biologia: '))
nota_fis = float(input('Digite sua nota de física: '))
nota_media = (nota_bio + nota_fis + nota_mat + nota_port)/4

if nota_media >= 6:
    print(f'Parabéns! Sua nota foi {nota_media:.0f} e você está aprovado!')
else:
    print(f'Sua nota foi {nota_media:.0f} e você foi reprovado!')

