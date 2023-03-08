# prevod svetelnosti pix do ascii
# r+g+b / 3 do ascii 38 znakov

from PIL import Image
def mapovanie (a,b,c,d,x):
    return int(((d-c)*(x-a))/(b-a)+c)


density = 'Ñ@#W$9876543210?!abc;:+=-,._     '
fw=open("vystup.txt","w", encoding="utf-8")

img=Image.open("rei mini.jpg")
pix=img.load()

for y in range(img.height):
    for x in range(img.width):
        #print(pix[x,y])
        avg=sum(pix[x,y])/3
        pos=mapovanie(0,255,0,len(density)-1, avg)
        print(density[pos])
        fw.write(density[pos])
    fw.write("\n")
fw.close()




# print(mapovanie(0,255,0,38,12))
