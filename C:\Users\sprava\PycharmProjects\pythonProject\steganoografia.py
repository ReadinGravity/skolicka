from PIL import Image
from random import randint

img = Image.open("rei.png")
pixels = img.load()
#
for i in range(img.size[0]):
    for j in range(img.size[1]):
        sf=int(sum(pixels[i,j])/3)
        pixels[i,j] = (sf,sf,sf)

# img.show()
img.save("mojprvy.png")

#https://www.youtube.com/watch?v=0L2n8Tg2FwI

#steganografia skrytie samotnej spravy

#doplnim si 0 aby bolo vzdycky 8 znakov na zaciatok
#RBG kodujem do B
# 1 pis = 8 pix
# podla cis z bin z ord pismena zmenime posldne cis z B zlozky premeneho na bin
