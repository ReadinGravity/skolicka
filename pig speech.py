# def pigspeech(slovo:str)->str:
#     newword:''
#     if len(slovo)>3:
#         newword=slovo[1::]+slovo[:2:]+'ay'
#     else:
#         newword=slovo
#
#     return newword
#
#
# print(pigspeech('hello'))

def accum(slovo:str)->str:
    novoslovo=''
    for i in range(len(slovo)):
        temp=slovo[i]*(i+1)
        temp=temp.capitalize()
        temp+= '-'
        novoslovo+=temp
    return novoslovo[:-1:]

print(accum ('dudo'))
