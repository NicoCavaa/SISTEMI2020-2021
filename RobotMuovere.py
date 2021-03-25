import pygame
import sys

sur_obj=pygame.display.set_mode((400,300))
White=(255,255,255)

NERO = (0, 0, 0 )       
BIANCO = (255, 255, 255)
ROSSO = (255, 0, 0)


pavimento = [[0, 0, 0, -1, -1, 0, -1], 
                [-1, 0, 0, 0, -1, -1, 0], 
                [0, 0, -1, -1, -1, 0, 0], 
                [-1, 0, 0, 0, -1, -1, 0], 
                [-1, 0, 0, 0, 0, -1, -1], 
                [-1, -1, -1, 0, 0, 0, -1]] 

dimensione = 100

ALTEZZA = len(pavimento) * dimensione
LARGHEZZA = len(pavimento[0]) * dimensione

def disegnaOstacoli():
    for cy in range(0, len(pavimento)):
            for cx in range(0, len(pavimento[cy])):
                

                if pavimento[cy][cx] == -1:
                    cx = cx * dimensione
                    cy = cy * dimensione 

                    pieno = pygame.Rect(cx, cy, dimensione, dimensione)
                    pygame.draw.rect(screen, ROSSO, pieno)

                    cx = int(cx / dimensione)
                    cy = int(cy / dimensione) 

def numeraPavimento():
    global pavimento
    NumCelle = 0

    for cy in range(0, len(pavimento)):
        for cx in range(0, len(pavimento[0])):

            if pavimento[cy][cx] == 0:             
                pavimento[cy][cx] = NumCelle
                NumCelle += 1
                
                numeri = pygame.font.SysFont("Calibri", 40)
                testo = numeri.render(str(NumCelle), True, (BIANCO))
                screen.blit(testo, (cx * dimensione + 43, cy * dimensione + 35))

def drawGrid():
    dimensione = 100
    for x in range(0, LARGHEZZA, dimensione):
        for y in range(0, ALTEZZA, dimensione):
            piastrella = pygame.Rect(x, y, dimensione, dimensione)  
            pygame.draw.rect(screen, BIANCO, piastrella, 1) 


def MuoviRobot():
    passo=5
    sur_obj.fill(White)
    pygame.draw.rect(sur_obj, (255,0,0), (passo, passo, 70, 65))
    for k in range(0, len(pavimento)):
        for eve in pygame.event.get(): 
            key_input = pygame.key.get_pressed()

            if key_input[pygame.K_LEFT]:
                print("Ti sei spostato a sinistra")
                pavimento[y][x-passo]
            if key_input[pygame.K_UP]:
                print("Ti sei spostato in alto")
                pavimento[y+passo][x]
            if key_input[pygame.K_RIGHT]:
                print("Ti sei spostato a destra")
                pavimento[y][x+passo]
            if key_input[pygame.K_DOWN]:
                print("Ti sei spostato in basso")
                pavimento[y-passo][x]


def creaDizionario():
        dizCoordinate = {}
        Liberi = []
        numeraPavimento()

        for y in range (0, len(pavimento)):
            for x in range (0, len(pavimento[y])):

                if pavimento[y][x] != -1:

                    if x != 0:
                        if pavimento[y][x - 1] != -1:
                            Liberi.append(pavimento[y][x - 1])
                    
                    if x != len(pavimento[y]) - 1:
                        if pavimento[y][x + 1] != -1:
                            Liberi.append(pavimento[y][x + 1])
                    
                    if y != 0:
                        if pavimento[y - 1][x] != -1:
                            Liberi.append(pavimento[y - 1][x])
                    
                    if y != len(pavimento) - 1:
                        if pavimento[y + 1][x] != -1:
                            Liberi.append(pavimento[y + 1][x])
        
                    dizCoordinate[pavimento[y][x]] = Liberi
                    Liberi = [] 
        
        print(dizCoordinate)



        

def main():
    global screen
    pygame.init()  #parte pygame
    screen = pygame.display.set_mode((LARGHEZZA, ALTEZZA))  #dimensioni schermo
    screen.fill(NERO)

    
    creaDizionario()

    while True:
        drawGrid()
        disegnaOstacoli()
        for event in pygame.event.get():        #ascolta eventi (mouse, tastiera ecc)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
     
        pygame.display.update()


if __name__ == "__main__":
    main()