t=0
x=1
#for x in range(7000,8000):             #(trang.no,divisors)=(24552528,240)
while True:                                                #=(2162160 fac= 320)   
    t=0
    for y in range(1,x+1):
        t=t+y #t;trangle num
    fac=0
    for z in range(1,t+1):
        if t%z==0:
            fac+=1
    if fac>100:        
        print('t=',t,'fac=',fac)        
    if fac>500:
        print('*',t,'*')
        break
    x=x+1
'''
n=24552528
t=0
for x in range(1,n+1):
    if n%x==0:
        t=t+1
        #print(x,end=',')
'''        
