# #fr=open("cesta k suboru"), fr reading, fw writing
# #   absolutna=cela, od hardisku C:/downloads/asus/downloads, npc ak sa subor premiestni
# #   relativna= data/data.txt, lepsie
#
fr=open("../data/data.txt", "r", encoding="utf-8")
# #sposoby prechodu suboru:
#
# #1. sposob
# for riadok in fr:
#     print(riadok.strip()) #odstrani neviditelne znaky
#
#2.sposob - vytvorim mega str
#ms=fr.read()

#
# #3. sposob - ked riadky potrebujem spracovat inak
# prvyriadok=fr.readline() #citacia hlava precita 1. riadok a caka na zaciatku 2.
# print(prvyriadok)
#
# druhyriadok=fr.readline()
# print(druhyriadok)
#
# for riadok in fr:
#     print(riadok)
#
# #4. sposob - riadky v zozname
# zoz_riadok=fr.readlines()
# print(zoz_riadok)

#kolko je tam lowecase pismenok

from string import ascii_lowercase
ms=fr.read()
poc={}
enter=0
for znak in ms:
    if znak in znak.isupper() or znak.islower():
        poc[znak]=poc.get(znak,0)+1
    if znak=='\n'
        enter+=1


print(poc)
rpint(enter)

#priemerny pocet pismen v riadku, kolko je tam medzier, zapisat subor odzadu
#fw.write(zapis do suboru)
