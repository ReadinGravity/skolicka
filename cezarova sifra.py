#cipher - symtericke (1 key), asymetricke (public + private key)
#zoberem znak, premenim na cislo, odpocitam 97, pripoc posun, zvysok po ped 26%, pripoc 97, prevod cisla na znak

def caesar_encode(zdroj:str, posun:int)->str:
    encode=""
    for i in zdroj:
        a=(ord(i)-97+posun)%26+97
        x=chr(a)
        encode+=x
    return encode
print(caesar_encode("zxcvb",10))
print(caesar_encode("sedrftgyhujikol",112))
