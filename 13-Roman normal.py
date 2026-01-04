s="MCMXCIV"
mydic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
Sum=0
x=0
p=0
while x<len(s)-1:
    #if x!=len(s)-1:
    if s[x]=="I" and s[x+1]=="V":
        Sum+=4  
        x+=2
        print(s[x],s[x+1],Sum)
    if s[x]=="I" and s[x+1]=="X":
        Sum+=9 
        x+=2
        print(s[x],s[x+1],Sum)
    if s[x]=="X" and s[x+1]=="L":
        Sum+=40 
        x+=2
        print(s[x],s[x+1],Sum)
    if s[x]=="X" and s[x+1]=="C":
        Sum+=90
        x+=2
        print(s[x],s[x+1],Sum)
    if s[x]=="C" and s[x+1]=="D":
        Sum+=400
        x+=2
        print(s[x],s[x+1],Sum)
    if s[x]=="C" and s[x+1]=="M":
        Sum+=900 
        x+=2
        print(s[x],s[x+1],Sum)
    else:
        Sum+=mydic[s[x]] 
        x+=1
        print(s[x],s[x+1],Sum)

if x==len(s)-1:
    Sum+=mydic[s[x]]
    print(s[x],s[x+1],Sum)
print(Sum)

