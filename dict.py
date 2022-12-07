fr=open("data/animals.txt", "r", encoding="utf-8")
#print(*fr)
zoo={}
for row in fr:
    temp=row.strip().split(" ") #zretazenie funkcii, smrad vrati string a potom chop chop mf
    zoo[temp[0]]=int(temp[1]) #kt klucu kt hodnotu priradim
print(zoo)

zoo2=sorted(zoo) #debilny sposob ale it works
zoo3={}
for animal in zoo2:
    zoo3[animal]=zoo[animal]
print(zoo3)

poc=0
for hm in zoo:
    poc+=zoo[hm]
average=poc/len(zoo)
print(average)

#s neutriedenim
naj=list(zoo.keys())[0]
for kluc in zoo.keys():
    if zoo[kluc]>zoo[naj]:
        naj=kluc
print(naj,zoo[naj])

tazsie_ako(vstup_zviera:str)->dict:
new_zoo={}
for zviera in zoo:
    if zoo[zviera]>zoo[vstup_zviera]:
        new_zoo[zviera]=zoo[zviera]
    return new_zoo




