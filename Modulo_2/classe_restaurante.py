class Restaurante:
    def __init__(self, dia_semana, cardapio):
        self.dia_semana = dia_semana
        self.cardapio = cardapio

class MC_donalds(Restaurante):
    def __init__(self, nome, pagamento, dia_semana, cardapio ):
        super().__init__(dia_semana, cardapio)
        self.nome = nome
        self.pagamento = pagamento

class Burguer_King(Restaurante):
    def __init__(self, nome, pagamento, dia_semana, cardapio ):
        super().__init__(dia_semana, cardapio)
        self.nome = nome
        self.pagamento = pagamento

class Bobs(Restaurante):
    def __init__(self, nome, pagamento, dia_semana, cardapio ):
        super().__init__(dia_semana, cardapio)
        self.nome = nome
        self.pagamento = pagamento
