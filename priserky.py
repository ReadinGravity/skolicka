# gentic code priserky 0 az 9 a je to 5 cisel napr. 2,5,8,9,1
# best priserka je 1,1,1,1,1
# mutacie

import random
monsters=[]

def monster_creation():
    temp=[]
    for i in range (5):
        temp.append(random.randint(0,10))
        return temp

def iq_test(monster:list)-> int:
    return monster.count (1)

def sexik (monster1, monster2):
    #mutacie su 7%
    if random.randint(0,101) <=7:
        # mutacia here
    else:
        # mutacia not here

def genocida:
    #povrazdime 50% populacie
