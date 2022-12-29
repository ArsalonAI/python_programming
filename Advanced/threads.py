import threading 
from time import sleep 

def run(content, delay=1):
    sleep(delay)
    print(content)
    
thread1 = threading.Thread(target=run, args=("run 1",2 ))
thread2 = threading.Thread(target=run, args=("run 2", 1))

thread1.start()
thread2.start()
print("main thread")
print('number of threads running', threading.active_count())
thread1.join() #gives control back to thread1

# Threading Example

def print_values(values, delay):
    for item in values:
        print(item)
        sleep(delay)
        

thread_one = threading.Thread(target=print_values, args=([1, 3, 5], 0.2))
thread_two = threading.Thread(target=print_values, args=([2,4], 0.3))

thread_one.start()
thread_two.start()

