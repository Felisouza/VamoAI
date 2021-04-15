class Fila:
    def __init__(self):
        self.queue = []

    def chegada(self, item):
        return self.queue.append(item)

    def tamanho(self):
        return len(self.queue)

    def partida(self):
        primeiro = self.queue[0]
        self.queue.pop(0)
        return primeiro 

banco = Fila()

banco.chegada('primeiro')
print(banco.queue)

banco.chegada('segundo')
print(banco.queue)

banco.chegada('último')
print(banco.queue)

banco.partida()
print(banco.queue)
