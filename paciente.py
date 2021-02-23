def exame(resultado):
    if resultado >= 7 and resultado <= 10:
        return print('Seu resultado está bom. Contine assim!')
    elif resultado >= 4 and resultado < 7:
        return print('Sua resultado não está muito bom. Busque se cuidar mais e fazer acompanhamento médico.')
    else:
        return print('Sua saúde não está boa. Procure a equipe médica!')

paciente1 = 10
paciente2 = 6.9
paciente3 = 3.9

exame(paciente1)
exame(paciente2)
exame(paciente3)