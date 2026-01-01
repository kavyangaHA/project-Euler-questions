##for n in range(2,10):
##    for x in range(2,n):
##        if n%x==0:
##            break
##    else:
##        print(n)

def prime(n):
    for x in range(2,n):
        if n%x==0:
            break
    else:
        print(True)
m=3797
M=str(m)
x=0
L=[]
l=[]
while True:
    M=str(m)
    while x<len(M):
        n=M[x::]
        L=L+[n]
        x=x+1
    for y in L:
        p=prime(int(y))
        if p==True:
            l=l+[y]
    if len(L)==len(l):
        print(m)
    
        
##        p=prime(int(n))
##        if p==True:
##            x=x+1
##        else:
##            
        
