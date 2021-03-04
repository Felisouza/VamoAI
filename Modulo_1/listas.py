##append, pop, remove, count, reverse, insert, len, lista com repartição
nomes = ["Felipe", "Lina", "Julia", "Karina", "Rafael", "Gabriel", "Lourdes", "Arthur", "Felipe"]

nomes.append('Carolina')

nomes.pop()

nomes.remove(nomes[0])

print('O nome Felipe aparece',nomes.count('Felipe'),'vezes')

nomes.sort(reverse=True)

nomes.insert(0,'Felipe')

print('Essa lista tem',len(nomes), 'elementos')

nomes[0:5:2]

nomes[1:5]

print(nomes)