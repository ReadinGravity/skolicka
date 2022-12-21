zoz1=[i for i in (1,51) if i%3==0 or i%5==0]
print (zoz1)

zoz2=[(i.upper() + str(j) + k) for i in "abc" for j in (2,10,2) for k in "/+-"]
print(zoz2)


zoz3=[year for year in range(1000,2001) if year%4==0 and year%100!=0 or year%400==0]
print(zoz3)



vec=[-4, -2, 0, 2, 4]
zoz5=[i*2 for i in vec]
zoz6=[i for i in vec if i>0]
zoz7=[abs(i) for i in vec]
print(zoz5)
print(zoz6)
print(zoz7)

zoz8=[" banana", " loganberry", " passion fruit"]
fruit=[i.strip() for i in zoz8] #ak chcem ak strednu [i.replace(" ", "") for i in zoz8]
print(fruit)





