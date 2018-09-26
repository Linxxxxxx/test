from test import *
import threading
import time


def io():
    write()
    read()


count1 = []
t = time.time()
for x in range(10):
    th = threading.Thread(target=io)
    count1.append(th)
    th.start()

for i in count1:
    i.join()

print('thread cpu:', time.time() - t)
