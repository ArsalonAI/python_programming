import threading
from time import sleep 

# Threading Example

def print_values(values, delay):
    for item in values:
        print(item)
        sleep(delay)
        

thread_one = threading.Thread(target=print_values, args=([1, 3, 5], 0.2))
thread_two = threading.Thread(target=print_values, args=([2,4], 0.3))

thread_one.start()
thread_two.start()
