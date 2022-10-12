def fak(cislo):
    vys=1
    for i in range (2,cislo+1):
        vys*=i
    return vys
print (fak(5))


def komb (n,k):
    return fak(n)//(fak(k)*fak(n-k))
print (komb(5,3))


def psc(riadok:int):
    for cr in range (riadok+1): #cr-cislo riadku
        for k in range(0,cr+1):
            print(komb(cr,k), end=" ")
        print(" ") #/n - enter koniec riadku
psc(5)

#v zadani ak je funkcia vrati = return
# ak funkcia vypise = print()
