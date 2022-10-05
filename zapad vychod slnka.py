ret=input('zadaj mi retazec (hh:mm):')
a,b,=ret.split(':')
a=int(a)*60-360
b=int(b)
#pocet min od 6:00
#vychod/zapad slnka od 6:00 do 18:00
c=a+b
x=c*1/4
print(x)

if x<0 or x>180:
    print('je tma ty vole, chod spat')
else:
    print (x)
#x/180=230/720, 180/720=1/4


