# 作业
# 客户端功能：
# １．类似于ｑｑ聊天群，在聊天室允许多个用户加入聊天室
# ２．加入时需要有一个简单的用户名注册（不需要数据库，临时存储即可）
# ３．客户端发送消息时，其他客户端可以收到，但是本人收不到
# ４．如果有用户进入聊天室或者退出聊天室的时候会给其他客户端发送一个通知
# ５．支持管理员喊话（servse端是可以发消息的，server端发消息时所有客户端都能收到）

from threading import *
from socket import *
from time import *

ADDR = (('127.0.0.1', 8893))
BUTTERSIZA = 1024

s = socket()
s.bind(ADDR)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.listen(5)
d = {}
l = []
boardcast = []

def handler(c):
    def register(c):
        while True:
            try:
                name = c.recv(1024).decode()
                c.send("OK".encode())
                sleep(0.1)
                break
            except Exception as e:
                print(e)
        return name
    def recv(c):
        global d
        nonlocal name
        while True:
            message = c.recv(1024).decode()
            if message == 'exit':
                l.remove(name)
                break
            else:
                d[name].append(message)
    def send(c):
        global d, boardcast
        nonlocal name
        while True:
            sleep(0.1)
            c.send(('C#%s'%d).encode())
            sleep(0.2)
            c.send(('E#%s'%l).encode())
            sleep(0.2)
            c.send(('B#' + '%s' % boardcast).encode())
            if name not in l:
                break

    global d, l
    name = register(c)
    d[name] = []
    l.append(name)
    t1 = Thread(target=recv, args=(c,))
    t1.start()
    t2 = Thread(target=send, args=(c,))
    t2.start()
    t1.join()
    t2.join()
    c.close()

def board():
    s = input('请输入要广播的内容')
    boardcast.append(s)

if __name__ == '__main__':
    while True:
        try:
            c, addr = s.accept()
            print('c from', addr)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print(e)
        t = Thread(target=handler, args=(c,))
        t.start()
        t0 = Thread(target=board, args=())
        t0.start()
    s.close()

        

