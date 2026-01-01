def prime(n):
    for x in range(2,n):
        if n%x==0:
            break
    else:
        if n==1:
            pass
        else:
            return(True)
R=[]        
for x in range(10,10000):
    v=prime(x)
    if v==True:
        R=R+[x]
#print(R)        
        
        
#Testing        
##m=3797
##M=str(m)
##x=0
##L=[]
##l=[]
##while x<len(M):
##    n1=M[x::]
##    n2=M[:len(M)-x]
##    #print(n1,n2)
##    L=L+[n1]+[n2]
##    x=x+1
##print()    
##for y in L:
##    p=prime(int(y))
##    if p==True:
##        #print(y)
##        l=l+[y]
##L=set(L)
##l=set(l)
##if len(L)-len(l)==0:
##    print(m)

#########

#Answer        
m=10#=R[i]
s=0
while s<=20:
    for i in range(len(R)):
        p1=R[i]
        #if p1==True:
        M=str(R[i])
        x=0
        L=[]
        l=[]
        while x<len(M):
            n1=M[x::]
            n2=M[:len(M)-x]
            #print(n1,n2)
            L=L+[n1]+[n2]
            x=x+1
        #print()    
        for y in L:
            p2=prime(int(y))
            if p2==True:
                #print(y)
                l=l+[y]
        #L=set(L)
        #l=set(l)
        if len(L)-len(l)==0:
            print(R[i])
            s=s+1
            #break
        
