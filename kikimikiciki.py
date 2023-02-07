from random import randint

ff={}
pp=1000000
for ii in range(pp):
    a=randint(1,101)
    b=randint(1,101)
    c=int(str(a**b)[0])
    ff[c]=ff.get(c,0)+1
print ff
for i in ff:
    print(i, ff[i], (ff[i]/pp)*100)
