#paradigma= sposob programovania

    #OOP-object oriented programming
    #proceduralne - rozdeli kod na funkcie/procedury
    #funkcionalne - skladanie funkcii

def fak (cislo) #v zatvorke vstupne parametre
    vys=1
    #lokalna premenna, * ked zavolam fak, akonahle sa vrati result (fak skonci) premenna  zanik
    for i in range(2,cislo+1):
        vys*=i
    return vys
    #definicia funkcia, jej deklaracie
vypocet=fakt(5)
print(vypocet)

# globalne vs lokalne premenne
    #globalne = existuju pocas celeho programu
    #lokalne = existuje len v casti programu napr. vo funkcii

