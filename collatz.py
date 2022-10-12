# #napis funkciu kt pre zadane cislo vypise jeho cleny colatzovej postupnosti
# def collatz(cislo):
#     while cislo!=1:
#         if cislo %2==0:
#             cislo//=2
#         elif cislo %2==1:
#             cislo=cislo*3+1
#         print(int(cislo), end=" ")
#
#
# collatz(13)


#napis funckiu kde ked napisem 5, bude z toho pravouhly trojuholnik
def psc(riadok:int):
    for cr in range (riadok+1):
        for k in range(cr+1):
            print("*"*(cr+1), end=" ")
        print(" ")
psc(5)

#pekny trojuholni, 1 for na medzery, druhy na *
#input.sk funkcie 1,2,3
