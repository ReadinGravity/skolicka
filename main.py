meno=input("zadaj mi meno suboru: ")

def otvor_subor(meno="vstup3.txt"):
    return open("data/"+meno, "r", encoding="UTF-8")


def spracuj_subor(fr):
    riadky=fr.readlines()
    temp=riadky[1].strip()
    print("'" + temp + "'")
    slova=temp.split(" ")
    print(slova[0])
    print(temp.count(" "))
    poc=0
    for i in temp:
        if i==" ":
            poc+=1

fr=otvor_subor(meno)
spracuj_subor(fr)
# shift f6 replace all occurences


def sirka(fr):
    maxlen=0
    for riadok in fr:
        if len(riadok)>maxlen:
            maxlen=len(riadok)
    return maxlen
print(sirka(fr))
