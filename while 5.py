slovo=input("povedz mi nejake slovo: ")
cd=0
while slovo[0]!="x":
    cd+=len(slovo)
    slovo=input("povedz mi nejake slovo: ")
print("pocet znakov: ",cd)
