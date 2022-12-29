from threading import Lock, Thread 
from time import sleep 

def t1(lock):
    lock.acquire()
    sleep(1)
    print("t1")
    lock.release()
    
def t2(lock):
    lock.acquire() # lock is already aquired, must wait 
    sleep(1)
    print("t2")
    lock.release()
    
lock = Lock()
thread_1 = Thread(target=t1, args=(lock,))
thread_2 = Thread(target=t2, args=(lock,))

thread_1.start()
thread_2.start()

# Locks vs. delays
def print_values(values, start_lock, end_lock, name):
    for item in values:
        print(f"{name} waiting for lock")
        start_lock.acquire()
        print(item)
        end_lock.release()
        
lock1 = Lock()
lock2 = Lock()
lock2.acquire()

thread_one = Thread(target=print_values, args=([1, 3, 5], lock1, lock2, "t1"))
thread_two = Thread(target=print_values, args=([2,4], lock2, lock1, "t2"))

thread_one.start()
thread_two.start()