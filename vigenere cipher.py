#nejdem sa ani tvarit ze som si na toto nevykradla vlastny github
#najblizsie pouzit medzery nech si hodinu nehladam chybu
def encoding(text: str, kluc: str) -> str:
    nr = ''
    for i in range(len(text)):
        posun = ord(kluc[i % len(kluc)]) - 96
        x = (ord(text[i]) - 97 + posun) % 26 + 97
        y = chr(x)
        nr += y
    return nr

def decoding(text: str, kluc: str) -> str:
    nr = ''
    for i in range(len(text)):
        posun = ord(kluc[i % len(kluc)]) - 96
        x = (ord(text[i]) - 97 - posun) % 26 + 97
        y = chr(x)
        nr += y
    return nr

print(encoding('zmrlinka', 'spagetyapomazankaktomu'))
print(decoding('scssnhjb', 'spagetyapomazankaktomu'))

