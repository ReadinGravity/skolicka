#syntax sugar - list comprehensions
#vytvaranie zoz kt su dopredu naplnene hodnotami
from string import ascii_lowercase

zoz=[]
for i in range(0,51,2):
    zoz.append(i)

print(zoz)

zoz1=[i for i in (0,51,2)]
print (zoz1)

zoz2=[i for i in range (0,51,2) if i%4==0]

#leap years
zoz3=[year for year in range(1900,2001) if year%4==0 and year%100!=0 or year%400==0]
print(zoz3)


zoz4=[(i,j) for i in ascii_lowercase for j in range(9)]
print (zoz4)
