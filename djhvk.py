def uloha1(ret:str)->str:
    polka=len(ret)//2
    if len(ret)%2==1:
        polka+=1
#     #cez rezy
#     pp=ret[0:polka].upper()
#     hp=ret[polka::].lower()
#     return pp+hp
# print(uloha1('tomas'))

    # pp=""
    # for i in range(0,polka):
    #     pp+=ret[i].upper()
    # for i in range(polka, len(ret))|:
    #     hp+=ret[i]
    # return pp+hp

