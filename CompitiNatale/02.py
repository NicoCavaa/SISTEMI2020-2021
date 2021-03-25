import random

def mac():
    cardisponibili=('A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9')
    mac= ''
    for cnt in range(1,18):
        if(cnt%3==0):
            mac += ':'
        else:
            mac += random.choice(cardisponibili)
    return mac;

indirizzo= mac()
print(indirizzo);