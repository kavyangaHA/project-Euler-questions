f=[' ','one','two','three', 'four', 'five','six','seven','eight','nine','ten']
g=['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen','nineteen',' ']
h=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred']
l='hundred'
w=0
while True:
    if w==0:
        for x in f:
            print(x)
    if w==2:
        for y in g:
            print(y)
    if w==3:
        for z in h[:8:]:
           for x in f[:10:]:
               print(z,x)
    if w==4:
        for a in f[1:10]:
            for b in f:
                for c in g:
                    for r in h:
                        print(a,l,b,c,r)
                
        
                
    w=w+1
