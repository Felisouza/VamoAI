class Pessoa:
    def __init__(self, nome, CPF, telefone, RG):
        self.nome = nome
        self.CPF = CPF
        self.telefone = telefone
        self.RG = RG
    
    def exibir(self):
        return print(
            f'Nome: {self.nome}\n'
            f'CPF: {self.CPF}\n'
            f'Telefone: {self.telefone}\n'
            f'RG: {self.RG}\n'
        )

class Entregador(Pessoa):
    def __init__(self, nome, CPF, telefone, RG, automovel, nota):
        super().__init__(nome, CPF, telefone, RG)
        self.automovel = automovel
        self.nota = nota

    def exibir(self):
        return print(
            f'Nome: {self.nome}\n'
            f'CPF: {self.CPF}\n'
            f'Telefone: {self.telefone}\n'
            f'RG: {self.RG}\n'
            f'Veículo: {self.automovel}\n'
            f'Nota: {self.nota}'
        )

entregador = Entregador('Felipe', '12345678', '123456', '1234565', 'Moto', '5')

entregador.exibir()