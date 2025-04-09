#Problem-21
'''
t=0
n=0
for x in range(2,10):
    for y in range(1,x):
        if x%y==0:
            #print(x,'%',y,'=',x%y)
            print(x,y)
            t=t+y
    for m in range(1,t):
        if t%m==0:
            n=n+m
    if x==n:
        print(x,n)
              
            
    print(x,t)        
    t=0        
    print()

x=220
t=0
n=0
for y in range(1,x):
    
    if x%y==0:
        #print(x,'%',y,'=',x%y)
        #print(x,y)
        t=t+y
    for m in range(1,t):
        if t%m==0:
            n=n+m
    if x==n:
        print(x,n)
'''
#harima code eka
t=0
n=0
s=0
for x in range(1,10000):#x=a
    #print('*'*5,x,'*'*5)
    for y in range(1,x):
        if x%y==0:
            t=t+y#t=d(a)
    for r in range(1,t):#t=b
        if t%r==0:
            n=n+r#n=d(b)
    if x==n and x!=t:
        print('*'*5,x,'*'*5)
        print(x,t)
        s=s+x
    else:
        pass
        #b=x
##        print('nope')
    #print()
    t=0
    n=0
print(s)

#harima code eka - without comments

t=0
n=0
s=0
for x in range(1,10000):
    for y in range(1,x):
        if x%y==0:
            t=t+y
    for r in range(1,t):
        if t%r==0:
            n=n+r#n=d(b)
    if x==n and x!=t:
        print('*'*5,x,'*'*5)
        print(x,t)
        s=s+x
    t=0
    n=0
print(s)    








