# Solution to Queue problem with Threading

from queue import Queue
from time import sleep
from numpy import random
import threading


def main():

    tasks_que = Queue(5)
    item = tasks_que.get

    i = 0
    while True:
        if not tasks_que.full():
            tasks_que.put(threading.Thread(target=_new_function).start())
        else:
            break  # Since the first while loop is set to True, it will continue to loop unless told otherwise. 
        i += 1     # By adding a break point, the first loop is told that if the task queue is not done(False),
                   # it will jump to the second while loop and print "Remaining tasks in queue"...
    while True:
        if not tasks_que.empty():
            tasks_que.get()
            tasks_que.task_done()
            print("Remaining tasks in queue: ", tasks_que.qsize())

    return


def _new_function():
    print("First task in queue starting: {}".format(threading.currentThread().getName())) #The def new_function is called to the threading.Thread(target)to start the queues. 
    sleep(random.randint(30))
    print("Second task in queue starting:", threading.currentThread().getName())


if __name__ == '__main__':
        main()


