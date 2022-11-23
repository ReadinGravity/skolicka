# #dictionary = zoznam na steroidoch
# #sam si vytvorim indexy (nesmu byt 2 rovnake) "index":hodnota
# pd={}
# fz={"a":0, "b":5, "auto":148, 5:487, "c":[4,8,7]}
# print(fz["b"])
# print(fz["c"][-1])
#
# for key in fz:
#     print(key)
#     print(fz[key])
# print(fz)
# print(*fz)

#kolko je tam pismen minn abecedy
from string import ascii_lowercase
vstup=input("zadaj mi retazec: ")
poc={} #poc=dict()
for i in vstup:
    if i in ascii_lowercase:
        poc[i]=poc.get(i,0) +1

print(poc)

#3 polozky s najvacsimi hodnotami
slov={"item1":45.50,"item2":35,"item3":41.30, "item4":55, "item5":24}
#zotredit a vypisat prve 3 ==du
#sorted(slov, )

#hladam max prvok v dict
for i in range (3):
    moj_max=slov[index_max]
    index_max=slov.keys()[0]
    for prvok in slov:
        if slov[prvok]>moj_max:
             moj_max=slov[prvok]
             index_max=prvok
print(moj_max, index_max)
temp=slov.pop(index_max)
