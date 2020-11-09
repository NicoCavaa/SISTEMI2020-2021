#partendo dal primo elemento , si ricerca quello più piccolo (o più grande) e lo si scambia con l’elemento di partenza.

vettore = [0] *(100)
i=0
n=100
while True:
    min = i
    j=i+1
    while True:
        if vettore[j] < vettore[min]:
            min = j
        j= j+1
        if not(j>n): break
    temp=vettore[min]
    vettore[min]=vettore[i]
    i=i+1
    if not(i<n-1): break
    print(f"vettore è: {vettore[]}")