import threading 

def run(content):
    print(content)
    
thread1 = threading.Thread(target=run, args=("run",))
thread1.start()