t=0
for x in range(1,1000):
    if x%3==0 or x%5==0:
        #print(x)
        t=t+x
print(t)        

t=0
for x in range(1,1000):
    if x%3==0: 
        t=t+x
    elif x%5==0:
        t=t+x
print(t)        
