def podio_olimpico(tempo_chegada1,tempo_chegada2,tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3):
    if tempo_chegada1 < tempo_chegada2 and tempo_chegada1 < tempo_chegada3:
        primeiro = tempo_chegada1
        primeiro_nome = nome_corredor1
    elif tempo_chegada2 < tempo_chegada1 and tempo_chegada2 < tempo_chegada3:
        primeiro = tempo_chegada2
        primeiro_nome = nome_corredor2
    else:
        primeiro = tempo_chegada3
        primeiro_nome = nome_corredor3
    
    if tempo_chegada1 > tempo_chegada2 and tempo_chegada1 > tempo_chegada3:
        terceiro = tempo_chegada1
        terceiro_nome = nome_corredor1
    elif tempo_chegada2 > tempo_chegada1 and tempo_chegada2 > tempo_chegada3:
        terceiro = tempo_chegada2
        terceiro_nome = nome_corredor2
    else:
        terceiro = tempo_chegada3
        terceiro_nome = nome_corredor3

    if tempo_chegada1 > primeiro and tempo_chegada1 < terceiro or :
        segundo = tempo_chegada1
        segundo_nome = nome_corredor1
    elif tempo_chegada2 > primeiro and tempo_chegada1 < terceiro:
        segundo = tempo_chegada2
        segundo_nome = nome_corredor2
    else:
        segundo = tempo_chegada3
        segundo_nome = nome_corredor3  
    
    podio = (
            f"1 - {primeiro_nome} - {primeiro} minutos\n"
            f"2 - {segundo_nome} - {segundo} minutos\n"
            f"3 - {terceiro_nome} - {terceiro} minutos\n"
        )
    return print(podio)

podio_olimpico(1, 7, 3, "fulano1", "fulano2", "fulano3")
