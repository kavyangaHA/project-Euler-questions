import time
t1=time.time()

#Support

###Method 1
##n=585
##b=str(bin(n))
##B=b[2::]
##N=str(n)
###b=str(b)
##if N==N[::-1]:
##    if B==B[::-1]:
##        print('yep')
##t2=time.time()
##print('Total Time=',t2-t1)
##
###Method 2
##t3=time.time()
##n=585
##b=str(bin(n))
##B=b[2::]
##N=str(n)
###b=str(b)
##if N==N[::-1] and B==B[::-1]:
##    print('yep')
##
##t4=time.time()
##print('Total time=',t4-t3)

#Answer
n=1
s=0
while n<10**6:
    b=str(bin(n))
    B=b[2::]
    N=str(n)
    if N==N[::-1] and B==B[::-1]:
        s=s+n
    n=n+1    
print(s)        
t2=time.time()
print('Total Time=',t2-t1)
#answer=872187      
