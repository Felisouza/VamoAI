class Cachorro:
    def __init__(self, nome, cor, raca, porte, n_patas):
        self.nome = nome
        self.cor = cor
        self.raca = raca
        self.port = porte
        self.n_patas = n_patas

    def comer(self, racao):
        self.racao = racao
    
    def dormir(self, cama):
        self.dormir = cama
    
    def fazer_coco(self, local):
        self.local = local

    def fazer_xixi(self, local):
        self.local = local

    