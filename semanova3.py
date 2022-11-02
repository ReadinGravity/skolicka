# napiste funckiu kt bude mat 1 vstup parameter retaazec funckia ret prejde a vrati priemer vsetkych cislic kt tam najde

def average(ret:str):
    fullstring = "qwertzuioplkjhgfdsayxcvbnm"
    substring = "0123456789"
    nums="0123456789"
    sum=0
    pocet=0
    for i in ret:
        if i in fullstring:
            pocet+=1
            sum+=int(i)
    average=sum/pocet
    return(average)
    if substring in fullstring:
          print("Found!")

print(average("10245867"))
print(average("dfg175468"))
print(average("ajbfhe"))



fullstring = "StackAbuse"
substring = "tack"








