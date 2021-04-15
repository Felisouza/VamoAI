def podio_olimpico(tempo_chegada1,tempo_chegada2,tempo_chegada3):
    tempos = [tempo_chegada1,tempo_chegada2,tempo_chegada3]
    tempos.sort()
    primeiro = tempos[0]
    segundo = tempos[1]
    terceiro = tempos[2]
    podio = (
            f"1 - {primeiro} minutos\n"
            f"2 - {segundo} minutos\n"
            f"3 - {terceiro} minutos\n"
        )
    return print(podio)


podio_olimpico(10,20,5)
