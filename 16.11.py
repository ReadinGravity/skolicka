# zoz=[]
# for i in range(10):
#     zoz.append(input("zadaj mi prvok zoznamu"))
#
# #1. sposob
# print(*zoz) #bez zatvoriek s medzerami
#
# #2. sposob
# for i in range (10):
#     priny (zoz[i]) #i je vzdy int
#
# for prvok in zoz:
#     print (prvok, type(prvok)) #typ prvku rovn ako v zoz
#
# #3. sposob
# for index, hodnota in enumerate(zoz): #(index, value) vrati poradie a hodnotu v zoz
#     print(index)
# #     print(hodnota)
# -------------------------------
# import random
# zoz=[]
# for i in range(10):
#     zoz.append(random.randrange(0,100))
# print(zoz)
#
# #vyber nahodneho prvku
# index=random.randrange(0,10)
# print(zoz[index])
#
# print(random.choice(zoz))
#
# print (zoz)
# nov_zoz=sorted(zoz)
# print (nov_zoz) #*novy potriedeny zoz
#
# zoz.sort()
# print(zoz) #urobi si poriadok sam so sebou
---------------------------
#algoritmus ako sorted ale w/o it
zoz=[22,10,15,1,8]

def find_max(index:int)->int:
    max_value=zoz[index]
    max_index=index
    for i in range (index,len(zoz)):
        if zoz [i] >max_value:
            max_value=zoz[i]
            max_index=i
    return max_index
print(*zoz)
print(find_max(0))

for i in range(index,len(zoz)):
    zoz[i]=find_max(i)
    zoz[i], zoz[max_index]=zoz[max_index], zoz[i]
print(zoz)

#bubble sort
