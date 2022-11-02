#parsovat = prechod suboru for finding / editing = regular expressions
tr="asd<dfgdfgrd><bmnhgk>bnkgfj<nm>dngldki"
def parsovacka(zdroj:str)->str:
    nr=""
    status=True
    for i in zdroj:
        if i == "<":
            status=False
        if status:
            nr+=i
        if i==">":
            status=True
    print(nr)

parsovacka("asd<dfgdfgrd><bmnhgk>bnkgfj<nm>dngldki")


