count=0
for x in range(2,10000):
    for y in range(2,x):
        if x%y==0:
            break
    else:
        count=count+1
    if count==10001:
        print(x)
        break
    x=x+1
    



##count=0
##x=3
##while True:
##    for y in range(2,x):
##        if x%y==0:
##            break
##    else:
##        count=count+1
##    if count==10001:
##        break
##    x=x+1
##print(x)    
