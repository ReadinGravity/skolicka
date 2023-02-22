from PIL import Image, ImageOps

img=Image.open("rei.png")
g_img=ImageOps.grayscale(img)
pixels=g_img.load()

fw=open("vysledok.txt","w", encoding="UTF-8")
fw.write (str(img.size[0])+ " " +str(img.size[1])+"\n")

for y in range(g_img.size[1]):
    for x in range(g_img.size[0]):
        a=hex(pixels[x,y])[2::] # hex prevod o 16 sustavy
        if len (a)==1:
            a="0"+a
        fw.write(a)
    fw.write("\n")

    #todo: zapis do suboru, ak je dlzka=1 pridaj 0
    # todo: namiesto ciernej bude 0, biela 1




fw.close()

