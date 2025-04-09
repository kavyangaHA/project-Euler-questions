def prime(n):
    for x in range(2,n):
        if n%x==0:
            break
    else:
        if n==1:
            pass
        else:
            return(True)
L=[]
n=0
s=0
x=1
while n<10**6:
    p=prime(x)
    if p==True:
        L=L+[x]
        s=s+x
        if prime(s)==True:
            n=s
            print(n)
    x=x+1
print()    
print(n)    
