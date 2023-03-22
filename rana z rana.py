from PIL import Image, ImageOps

img=Image.open("rei.png")
pixel_out=img.load()
img2=Image.new("RGB", img.size, "white")
pixel_in=img2.load()

# mirror flip
for x in range (img.size[0]):
     for y in range (img.size[1]):
         pixel_in[x,y]=pixel_out[-1-x,y]
img2.show()

# #doplnok kazdeho pixelu - negativ
invert=ImageOps.invert(img2)
invert.save('rei_neg.jpg')


