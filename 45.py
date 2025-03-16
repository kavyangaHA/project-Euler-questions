t=0
n=1
while t<=2:
    Tn=n*(n+1)/2
    Pn=n*(3*n-1)/2
    Hn=n*(2*n-1)
    if Tn==Pn==Hn:
        t=t+1
        print(n)
    if t==2:
        break
    
    n+=n
