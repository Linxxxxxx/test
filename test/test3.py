from test import *
import multiprocessing
import time


# def io():
#     write()
#     read()


count1 = []
t = time.time()
for x in range(10):
    th = multiprocessing.Process(target=count, args = (1, 1))
    count1.append(th)
    th.start()

for i in count1:
    i.join()

print('thread cpu:', time.time() - t)
