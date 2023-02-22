from PIL import Image

img=Image.open("rei.png")
pixel_out=img.load()
img2=Image.new("RGB", img.size, "white") #(img.size[0]*2, img.size[1]*2)
pixel_in=img2.load()

#mirroring cez obe osi
for x in range (img.size[0]):
     for y in range (img.size[1]):
         pixel_in[x,y]=pixel_out[-1-x,-1-y]
img2.show()

#zmensenie
# for x in range (0,img.size[0],2):
#     for y in range (0,img.size[1],2):
#         pixel_in[x//2,y//2]=pixel_out[-1-x,-1-y] #del //2 get comic effect
# img2.show()

#zvacsenie
for x in range (img.size[0]):
    for y in range (img.size[1]):
        pixel_in[2*x  , 2*y]   =pixel_out[x,y]
        pixel_in[2*x+1, 2*y]   =pixel_out[x,y]
        pixel_in[2*x  , 2*y+1] =pixel_out[x,y]
        pixel_in[2*x+1, 2*y+1] =pixel_out[x,y]
img2.show()

