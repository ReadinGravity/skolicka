from PIL import Image

img=Image.new("RGB", (100, 100), "yellow")
pix=img.load()

for i in range (img.size[1]):
    for j in range (img.size[0]):
        if (i+j)%2==0:
            pix [i,j]=(0,0,0)
img.save("new.jpg")
