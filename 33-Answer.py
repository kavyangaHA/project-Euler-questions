#Answer
import time
Start=time.time()
product_numerators=1
product_denominators=1
for x in range(10,100):
    for y in range(x+1,100):
        #print(x,y)
        t1=x/y
        numerator=set(str(x))
        denominator=set(str(y))-set('0')
        #print(numerator,denominator)
        for i in numerator:
            for j in denominator:
                if i==j:
                    numerator=numerator-set(i)
                    denominator=denominator-set(j)|set('1')
                    for n in numerator:
                        for d in denominator:
                            t2=int(n)/int(d)
                            if t2==t1:
                                print(x,y)
                                print(n,d)
                                product_numerators=product_numerators*int(n)
                                product_denominators=product_denominators*int(d)
                                print()
print(product_numerators)                        
print(product_denominators)
print('product_denominators/product_numerators=',product_denominators/product_numerators)
End=time.time()
print('Total time=',End-Start)
