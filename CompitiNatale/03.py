def fibo(num, cnt, x, y):
    if(cnt<num):
        cnt=cnt+1
        k=x+y
        x=y
        y=k
        print(k)
        fibo(num, cnt, x, y)

print("numero degli elementi")
num=input()
x=1
y=1
print(x)
print(y)
fibo(num, 2, x, y)