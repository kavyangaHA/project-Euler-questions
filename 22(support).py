L='COLIN MAGRET KAVYANGA RAJITHA YASONI SAMANTHA'
L=L.split(' ')
print(L)
L=sorted(L)
print(L)
#L=['COLIN', 'KAVYANGA', 'MAGRET', 'RAJITHA', 'SAMANTHA', 'YASONI']
s={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

##for x in L:
##    t=0
##    p=1
##    print(x)
##    for y in range(len(x)):
##        print(x[y],end=',')
##        t=t+s[x[y]]
##    print(t)
##    print()
##    
##print('*'*10)

Sum=0
for x in range(len(L)):
    t=0
    p=1
    print(L[x])
    name=L[x]
    for y in range(len(name)):
        print(name[y],end=',')
        t=t+s[name[y]]
    print(t)
    p=(x+1)*t
    print(p)
    Sum=Sum+p
    print()

print('Total=',Sum)    
