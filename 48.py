#Support
##s=0
##for x in range(1,11):
##    s=s+x**x
##print(s)    


s=0
for x in range(1,1001):
    s=s+x**x
#print(s)    
s=str(s)
s1=s[::-1]
s2=s1[:10:]
s=s2[::-1]
print(s)

