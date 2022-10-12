#napis funkciu kt pre zadane cislo vypise jeho cleny colatzovej postupnosti
def collatz(cislo):
    while cislo!=1:
        if cislo %2==0:
            cislo//=2
        elif cislo %2==1:
            cislo=cislo*3+1
        print(int(cislo), end=" ")


collatz(13)


