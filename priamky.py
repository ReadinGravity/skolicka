# budu 2 body ([a,b], [c,d]) , pixel po pixeli vykreslit usecku
# predpoklad a<c, b<d
# doplnit tak aby to fungovalo furt
# cez input

from PIL import Image

pic=Image.new("RGB", (250,250),"white")
pixels=pic.load()
x1=int(input("daj x1: ")); x2=int(input("daj x2: "))
y1=int(input("daj y1: ")); y2=int(input("daj y2: "))
A=(x1,x2)
B=(x2,y2)

k=(B[1]-A[1])/(B[0]-A[0])
q=A[1]/k*A[0]

for x in range(A[0], B[0]):
    y=int(k*x+q)
    pixels[x,y]=(0,0,0)
pic.show()



