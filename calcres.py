resistores = []
resarr = []
i = 0

with open('calcres.txt', 'r') as source:
    for line in source:
        resistores.append(line.strip('\n'))
source.close()

while i < 24:
    aux = float(resistores[i])
    resistores[i] = aux
    i=i+1

i=0
j=1


while i<24:
    while j<24:
        aux = (resistores[i]*resistores[j])/(resistores[i]+resistores[j])
        resarr.append(aux)
        j+=1
    i+=1
    j=i+1


for item in resistores:
    resarr.append(float(item))

resarr.sort()

with open('result.txt', 'w') as result:
    for item in resarr:
        result.write(str(item) + '\n')
