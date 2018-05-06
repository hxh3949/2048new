from game import *

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

def show_map():
    for r in map2048:
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



while not is_gameover():
    show_map()
    key=input('请输入操作')
    if key =='a':
        if left():
            fill_to_num(2)
    if key =='d':
        if right():
            fill_to_num(2)
    if key =='w':
        if up():
            fill_to_num(2)
    if key =='s':
        if down():
            fill_to_num(2)
    if key =='q':
        exit()