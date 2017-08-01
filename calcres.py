resistores = []
resarr = []
resreg = []
i = 0
#---------------------------------------------------------------------------------
#-------receive data from file and passes to list 'resistores'
#---------------------------------------------------------------------------------
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
numero = 0
#---------------------------------------------------------------------------------
#-------calculates equivalent resistance of all possible pairs writes them in another list
#---------------------------------------------------------------------------------

while i<24:
    while j<24:
        aux = (resistores[i]*resistores[j])/(resistores[i]+resistores[j])
        resarr.append(aux)
        prim = str(resistores[i])
        seg = str(resistores[j])
        resreg.append(prim + ' + ' + seg)
        j+=1
        numero += 1
    i+=1
    j=i+1

    #list1, list2 = zip(*sorted(zip(list1, list2)))
resarr, resreg = zip(*sorted(zip(resarr, resreg)))

'''
for item in resistores:
    resarr.append(float(item))'''

i=0
with open('result.txt', 'w') as result:
    while i < numero:
        result.write(str(resarr[i]) + ' = ' + str(resreg[i]) + '\n')
        i += 1