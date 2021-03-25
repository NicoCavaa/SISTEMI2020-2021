import string

def criptare(stringa):
    for cnt in range(len(stringa)):
        x=ord(stringa[cnt])  
        if(x<=107):
            x=x+15
            print(chr(x)) 
        else:
            x=97+(122-x)
            print(chr(x)) 


def decriptare(stringa):
    for cnt in range(len(stringa)):
        x=ord(stringa[cnt])  
        if(x>=112):
            x=x-15
            print(chr(x)) 
        else:
            x=122-(x-97)
            print(chr(x)) 




print("1 criptare\n2 decriptare")
n=input()
if(n==1):
    stringa=input("stringa da criptare ")
    criptare(stringa)
else:
    stringa=input("stringa da decriptare ")
    decriptare(stringa)