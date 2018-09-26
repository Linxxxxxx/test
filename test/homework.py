# 司机和售票员的故事
#     创建父子进程分别代表司机和售票员
#     当售票员收到SIGINT信号,给司机发送SIGUSR1信号,此时司机打印'老司机开车了'
#     当售票员收到SIGQUIT信号,给司机发送SIGUSR2信号,此时司机打印'车速有点快,系好安全带'
#     当司机捕捉到SIGTSTP信号,给售票员发送SIGUSR1,售票员打印'到站了,请下车'
#     到站后 售票员先下车, 司机下车
#     说明
#         SIGINT SIGQUIT SIGTSTP 从键盘发出


import signal
import os
import sys
import time
from multiprocessing import Process


def dirhandler(sig, frame):
    if sig == signal.SIGTSTP:
        os.kill(shou.pid, signal.SIGUSR1)
    if sig == signal.SIGUSR1:
        print('老司机开车了')
    if sig == signal.SIGUSR2:
        print('车速有点快,系好安全带')


def selhandler(sig, frame):
    if sig == signal.SIGINT:
        os.kill(shou._parent_pid, signal.SIGUSR1)
    if sig == signal.SIGQUIT:
        os.kill(shou._parent_pid, signal.SIGUSR2)
    if sig == signal.SIGUSR1:
        print('到站了,请下车')
        sys.exit()


def sell():
    signal.signal(signal.SIGINT, selhandler)
    signal.signal(signal.SIGQUIT, selhandler)
    signal.signal(signal.SIGUSR1, selhandler)
    signal.signal(signal.SIGTSTP, signal.SIG_IGN)
    while True:
        time.sleep(2)


shou = Process(target=sell)
shou.start()

signal.signal(signal.SIGTSTP, dirhandler)
signal.signal(signal.SIGUSR1, dirhandler)
signal.signal(signal.SIGUSR2, dirhandler)
signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGQUIT, signal.SIG_IGN)
shou.join()
