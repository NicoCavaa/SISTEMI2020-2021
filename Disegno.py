from turtle import *

n = int(input("inserisci il numero dei lati: "))
angolazione = int(input("inserisci l'angolazione: "))
cnt=0

while cnt < n:
    forward(100)
    right(angolazione)
    cnt = cnt+1
