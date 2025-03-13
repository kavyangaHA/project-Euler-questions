import time
t1=time.time()
def fib(x):
    if x==1:
        return 1
    elif x==2:
        return 2
    else:
        return fib(x-1)+fib(x-2)
##for x in range(1,10):
##    print(fib(x),end=',')
n=1
Sum=0
while fib(n)<4*10**6:
    if fib(n)%2==0:
        Sum+=fib(n)
    n+=1
print(Sum)            
t2=time.time()
print('Time taken =',t2-t1)

#####
t3=time.time()
L=[1,2]
n1=1
n2=2
Sum2=2
while n1+n2<4*10**6:
    t=n1+n2
    n1=n2
    n2=t
    if n2%2==0:
        Sum2+=n2
    #L+=[n2]
#print(L)
print(Sum2)   
t4=time.time()
print('Time taken =',t2-t1)
