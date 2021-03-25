import turtle

robot = turtle.Turtle()
win = turtle.Screen()

def up():
    robot.forward(50)
    print("up")

def left():
    robot.left(90)
    print("left")

def right():
    robot.right(90)
    print("right")

def down():
    robot.backward(50)
    print("down")


win.title("My game")
win.bgcolor("green")
win.setup(width=800, height=800)

win.listen() #mette la finestra in ascolto di eventi (es: pressione tasti)
win.onkey(up, "Up")
win.onkey(left, "Left")
win.onkey(right, "Right")
win.onkey(down, "Down")

win.mainloop()

variabili globali:
		- piu' le evitiamo meglio e'

		si dichiara all'inizio del programma, fuori dalle funzioni
		qualora una funzione debba modificare una variabile globale, si usa la parola chiave global