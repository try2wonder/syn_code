import random

def pl(t):
    for i in t:
        print(*i)


def sumrow(r1,r2):
    r3 = []
    for i in range(10):
        r3.append(r1[i] + r2[i])
    return r3



m1 = [[random.randint(-100, 100) for i in range(10) ] for i in range(10)]
m2 = [[random.randint(-100, 100) for i in range(10) ] for i in range(10)]
m3 = [sumrow(m1[i],m2[i]) for i in range(10)]



pl(m3)