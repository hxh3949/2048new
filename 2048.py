import random
import copy



def fill_to_num(n):
    l = []
    for i in range(4):
        for j in range(4):
            if map[i][j] == 0:
                l.append((i, j))
    if l:
        r, c = random.choice(l)
        map[r][c] = n


def left_shift(l):
    del_zero(l)
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            count += l[i]
            l[i] = l[i] * 2
            global count
            l[i+1] = 0
    del_zero(l)
    while len(l) < 4:
        l.append(0)

def left(map):
    for i in map:
        left_shift(i)


def right(map):
    for i in map:
        i.reverse()
        left_shift(i)
        i.reverse()

def up(map):
    map2 = copy.deepcopy(map)
    for i in range(4):
        for j in range(4):
            map[i][j] = map2[j][i]
    left(map)
    map2 = copy.deepcopy(map)
    for i in range(4):
        for j in range(4):
            map[i][j] = map2[j][i]

def down(map):
    map2 = copy.deepcopy(map)
    for i in range(4):
        for j in range(4):
            map[i][j] = map2[j][i]
    right(map)
    map2 = copy.deepcopy(map)
    for i in range(4):
        for j in range(4):
            map[i][j] = map2[j][i]

def del_zero(l):
    try:
        while True:
            i = l.index(0)
            l.pop(i)
    except Exception as e:
        pass

def not_end():
    map2 = copy.deepcopy(map)
    map3 = copy.deepcopy(map)
    map4 = copy.deepcopy(map)
    map5 = copy.deepcopy(map)
    
    for l in map:
        if l.count(0):
            return True
    else:
        global count
        t = count
        left(map2)
        right(map3)
        up(map4)
        down(map5)
        count = t
        if map2 == map and map3 == map\
        and map4 == map and map5 == map:
            print("游戏结束,总得分为%d" % count)
            return False
        else:
            return True




clr = {
    0: '\033[0;30;47m',
    2: '\033[0;30;43m',
    4: '\033[0;30;42m',
    8: '\033[0;30;46m',
    16: '\033[0;30;45m',
    32: '\033[0;30;41m',
    64: '\033[0;30;44m',
    128: '\033[1;37;43m',
    256: '\033[1;37;42m',
    512: '\033[1;37;46m',
    1024: '\033[1;37;45m',
    2048: '\033[1;37;47m',
}


def print_map():
    for r in map:
        for c in r:
            print(clr[c]+'      ',end=' ')
        print('\033[0m')

        for c in r:
            text=str(c) if c else ''
            print(clr[c]+text.center(6),end=' ')
        print('\033[0m')

        for c in r:
            print(clr[c]+'      ',end=' ')
        print('\033[0m')



map = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]

count = 0

while not_end():
    fill_to_num(2)
    print_map()
    print("得分为：", count)
    op = input("请输入操作")
    if op == "a":
        left(map)
    if op == "d":
        right(map)
    if op == 'w':
        up(map)
    if op == 's':
        down(map)

