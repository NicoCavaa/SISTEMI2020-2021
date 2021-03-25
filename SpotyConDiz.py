file = open("song.csv","r")

playlist = []
dizionario = {}

for riga in file:
    if (riga[1] == "\n"):                  
        r = riga[0:1].split(",") #serve per dividere dove ce una virgola   
    else:
        r = riga.split(",")          
    dizionario["numero"]=r[0] #si va fino alla prima virgola e si legge il numero     
    dizionario["titolo"]=r[1] #fino alla seconda virgola si legge il titolo        
    dizionario["autore"]=r[2] #fino alla fine per leggere l'autore       
    Diz = dizionario.copy()#faccio una copia altrimenti non mi stampa niente
    playlist.append(Diz)                    

for elemento in (playlist):
    print(elemento["numero"], elemento["titolo"], elemento["autore"])
    
file.close()