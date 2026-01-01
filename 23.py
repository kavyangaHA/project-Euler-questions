L=[]
for x in range(1,28123):
    t=0
    for y in range(1,x):
        if x%y==0:
            t=t+y
    if t>x:
        L=L+[x]
        #print(x)
print(L)
##L=[12, 18, 20, 24]
M=[]

for x in L:
    for y in L:
        #print(x,y,x+y)
        M=M+[x+y]
##M=set(M)
##N=[x for x in range(1,28123)]
##N=set(N)
##P=N-M
##s=0
##for x in P:
##    s=s+p
##print(s)    
