##p='s' in 'sring'
##if p==True:
##    print(True)
##p1=str(input())
##p2=str(2*int(p1))
##
##for x in p1:
##    r=x in p2
##    if r!=True:
##        break
##else:
##    print(True)
##    
    
##def same_digits(d):
##    d=str(d)
##    n=2
##    t=0
##    while n<=3:
##        d2=str(int(d)*n)
##        for x in d:
##            r=x in d2
##            if r!=True:
##                break
##        else:
##            n=n+1
##            t=t+1
##    if t==2:
##        return(True)
##    else:
##        return(False)
##    
##for y in range(1,1000):
##    m=same_digits(y)
##    if m==True:
##        print(y)
