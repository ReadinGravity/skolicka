from PIL import Image

#na zaklade parnosti viem urcit poseldnu cifru v bin

sprava="Ahoj svet#"
img=Image.open("rei.png")
pix=img.load()

def priprav(sprava:str)->list:
    res=[]
    for pismenko in sprava:
        cislo=bin(ord(pismenko))[2::]
        while len(cislo)!=8:
            cislo="0"+cislo
        for j in cislo:
            res.append(int(j))
    return res
print (priprav(sprava))

def drticka(sprava):
    sp=priprav(sprava)
    for i in range (len(sp)):
        #sp[i] co tam idzem pchat
        sirka=img.size[0]
        vyska=img.size[0]
        x=i%sirka            #double check that shit
        y=i//sirka           #same
        pixblue=pix[x,y][2]
        newblue=int(bin(pixblue)[2:-1:] + str(sp[i]),2)
        newcolor=(pix[x,y][0], pix[x,y][1],newblue)
        print(pix[x,y], newcolor)
        pix[x,y] = newcolor
    img.save("obrsospr.png")

drticka(sprava)








