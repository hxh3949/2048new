
import random

map2048=[
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]
]

def fill_to_num(n):
    l=[]
    for i in range(4):
        for j in range(4):
            if map2048[i][j]==0:
                l.append((i,j))
    if not l:
        return 
    i=random.choice(l)
    r,c=i
    map2048[r][c]=n

def reset():
    fill_to_num(2)
    fill_to_num(2)
    fill_to_num(4)
    print(map2048)

def move_zero(l):
    try:
        while True:
            i=l.index(0)
            l.pop(i)
    except Exception as e:
        pass

def _left_shift(l):
    old=l.copy()
    move_zero(l)
    for i in range(len(l)-1):
        if l[i]==l[i+1]:
            l[i]*=2
            l[i+1]=0
    move_zero(l)
    while len(l)<4:
        l.append(0)
    return old != l

def left():
    ret=False
    for i in map2048:
        if _left_shift(i):
            ret=True
    return ret

def right():
    ret = False
    for i in map2048:
        i.reverse()
    ret = left()
    for i in map2048:
        i.reverse()
    return ret

def up():
    ret=False
    for i in range(4):
        l=[]
        for r in map2048:
            l.append(r[i])
        if _left_shift(l):
            ret=True
        for j in range(4):
            map2048[j][i]=l[j]
    return ret

def down():
    map2048.reverse()
    ret=up()
    map2048.reverse()
    return ret

def is_gameover():
    for r in map2048:
        if r.count(0):
            return False

    for r in map2048:
        for j in range(3):
            if r[j]==r[j+1]:
                return False

    for col in range(4):
        for i in range(3):
            if map2048[i][col]==map2048[i+1][col]:
                return False
    return True







reset()
