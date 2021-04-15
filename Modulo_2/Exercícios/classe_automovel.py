class Automovel:
    
    def __init__(self, tipo, modelo, ano, quilometragem):
        self.tipo = tipo
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem

    def exibir(self):
        print(
            f'Tipo: {self.tipo}.\n'
            f'Modelo: {self.modelo}.\n'
            f'Ano: {self.ano}\n'
            f'Km rodado: {self.quilometragem} '
        )

class Carro(Automovel):
    pass
    #Nesses casos dá para fazer a herança com o super ou sem ele

class Moto(Automovel):
    def __init__(self, tipo, modelo, ano, quilometragem):
        super().__init__(tipo, modelo, ano, quilometragem)
    pass
    #Aqui fiz com o super para testar


#carro = Carro('Carro', 'Uno com escada', 1988, 5000000000)

#carro.exibir()

moto = Moto('Moto', 'CB-500', 2020, 12000)
#moto.exibir()
