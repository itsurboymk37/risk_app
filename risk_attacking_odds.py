from random import randint

def odds():
    a = 0
    d = 0
    for i in range(1000000):
        attack = (randint(1, 6), randint(1, 6), randint(1, 6))
        defend = (randint(1, 6), randint(1, 6))
        attack = sorted(attack)
        defend = sorted(defend)
        if attack[2]>defend[1]:
            a += 1
        else:
            d += 1
        if attack[1]>defend[0]:
            a += 1
        else:
            d += 1
    print (a)
    print (d)
    print ("the attacker wins", (a / (d + a)) * 100, "% of the time")

odds()




