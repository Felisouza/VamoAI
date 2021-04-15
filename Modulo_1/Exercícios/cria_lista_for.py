#Lista com idades aleatórias
idades = [2,4,18,25,55,33,29,25,85,50,57,31]
jovem = []
adulto = []
idoso = []

for i in idades:
    if i < 30:
        jovem.append(i)
    elif i > 30 and i < 60:
        adulto.append(i)
    else:
        idoso.append(i)

#Separei as idades em 3 faixas diferentes
print(jovem, adulto, idoso)