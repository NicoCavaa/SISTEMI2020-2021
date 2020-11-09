#partendo dal primo elemento , si ricerca quello più piccolo e lo si scambia con l’elemento di partenza.

lista = [9,2,4,1,8,3,56] 
print (lista)
i=0
n=100
while True:
    min = i
    j=i+1
    while True:
        if lista[j] < lista[min]:
            min = j
        j= j+1
        if not(j>n): break
    temp=lista[min]
    lista[min]=lista[i]
    i=i+1
    if not(i<n-1): break
print (lista)