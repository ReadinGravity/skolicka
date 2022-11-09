#lists are mutable, da sa menit, napcham tam viacero nemohogennych hodnot
#uz neviem k comu sme to porovnavali, ci mrakodrap ci detsky domov/dudo
#v zozname moze byt dalsi zoznam
#pozicie-indexy
# zoz[], zoz=list()
#zoz.append(5) - adds to the list
#zoz.pop()- vybere zo zoznamu
#zoz.remove() - vymaye 1. vyskyt hodnoty

# mps= "jozo fero jano miso"
# zoz=msp.split(" ")
# print(zoz)
# print(zoz[2])

# import random
# zoz=[]
# for i in range (10):
#     zoz.append(random.randrange(0,21))
# print(*zoz) #* print bez zatvoriek
#
# maxik=zoz[0]
# for i in range(1,len(zoz)):
#     if maxik<zoz[i]:
#         maxik=zoz[i]
#         poz=i
# print("max prvok je:", maxik, "pozicia je:", poz)
#
# parne=0
# nepar=0
# for i in range (len(zoz)):
#     if zoz[i]%2==0:
#         parne+=1
#     else:
#         nepar+=1
#
# print("parnych je: ", parne, "neparnych je:", nepar)
#
# hello=0
# for i in range(len(zoz)):
#     if zoz[i]%2==0 and i%2==0:
#         hello+=1
# print("par cisel na par poz:", hello)

zoz1=[2,7,10,16,58]
zoz2=[15,16,18,20]
zoz3=zoz1+zoz2
poc=0
while poc<len(zoz3):
    print(zoz3[poc])
    poc+=1


