from PIL import Image

fr=open("kompresia_obrazka_1.txt","r")
fl=fr.readline().split()
#print(fl)

img=Image.new ("RGB", (int(fl[0]), int(fl[1])), "white")
pix=img.load()

for i in range(img.height):
    a=fr.readline()
    for j in range (len(a)):
        if a[j]=="0":
            pix[j,i]=(0,0,0)


img.show()
