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


auto = Automovel('Carro', 'Uno com escada', 1988, 5000000000)

auto.exibir()
