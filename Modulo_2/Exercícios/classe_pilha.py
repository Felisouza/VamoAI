class Pilha:
    #iniciando a classe com o construtor __init__
    def __init__(self):
        self.itens = []
    
    #Método que tira o último elemento da lista. O pop sempre tira o último elemento, se eu não específicar. 
    ##Se a lista estiver vazia ele retorna nada (None)
    def pop(self):
        if self.tamanho() == 0:
            return None
        else:
            return self.itens.pop()

    #Método para adicionar elementos a lista
    def push(self, item):
        return self.itens.append(item)

    #Método para medir o tamanho da lista
    def tamanho(self):
        return len(self.itens)

livros = Pilha()

#os métodos são utilizados chamando a função com o ponto. Que nem as funções buit in ou de bibliotecas.
livros.push('O Tao da física')
livros.push('Harry Potter')
livros.push('Pense em Python')
livros.push('Tão alto, tão perto')

print(livros.itens)
print(livros.tamanho())
livros.pop()
print(livros.itens)
