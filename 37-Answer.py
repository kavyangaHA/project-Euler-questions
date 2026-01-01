def prime(n):
    for x in range(2,n):
        if n%x==0:
            break
    else:
        if n==1:
            pass
        else:
            return(True)
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
m=10
s=0
while s<=11:
    p1=prime(m)
    if p1==True:
        M=str(m)
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
            print(m)
            s=s+1
            #break
    m=m+1
