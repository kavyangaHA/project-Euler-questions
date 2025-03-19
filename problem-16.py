###problem-16
#common 
#for x in range(4):
    s=float(input('number:'))#in here we must put a number such as 32,not like 2**5
    #print(s)
    total=0
    for i in s:
        total=total+int(i)
    print(total)    

#Method-01(fast,mine)      
s=2**1000
total=0
for i in str(s):
    total=total+int(i)
print(total)    
  
#Method-02(Not mine,too slow)
sum(int(digit) for digit in str(2**1000))
