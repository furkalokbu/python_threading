import threading
import time

a = 5
b = 5

a_lock = threading.Lock()
b_lock = threading.Lock()

def thread1calc():
    global a,b

    print('Thread1 acquiring lock a')
    a_lock.acquire()
    time.sleep(5)

    print('Thread1 acquiring lock b')
    b_lock.acquire()
    time.sleep(5)

    a+=5
    b+=5


def thread2calc():
    global a,b

    print('Thread2 acquiring lock b')
    b_lock.acquire()
    time.sleep(5)

    print('Thread2 acquiring lock a')
    a_lock.acquire()
    time.sleep(5)

    a+=10
    b+=10


if __name__ == '__main__':
    t1 = threading.Thread(target=thread1calc)
    t1.start()

    t2 = threading.Thread(target=thread2calc)
    t2.start()
