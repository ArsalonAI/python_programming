import threading 
from time import sleep 

def run(content, delay=1):
    sleep(delay)
    print(content)
    
thread1 = threading.Thread(target=run, args=("run 1",2 ))
thread2 = threading.Thread(target=run, args=("run 2", 1))

thread1.start()
thread2.start()