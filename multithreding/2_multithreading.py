#Example of join(), will ensure to finish worker thread first
import threading
import time

def worker():
    print("Worker starts")
    time.sleep(2)  # Slow worker
    print("Worker FINISHES")

print("Main starts")
t = threading.Thread(target=worker)
t.start()  # Worker runs independently

print("Main continues IMMEDIATELY")
t.join()  # worker will finish first and than main with join
print("Main finishes")  # ← Main ends FIRST!

print("------------------------------------------------------------")
#Class example
class MyThread(threading.Thread):
    def run(self):  # ← WORKER THREAD CODE (runs when obj.start() called)
        print("Thread started working...")  # Worker prints
        time.sleep(2)
        print("Thread finished!")           # Worker prints

obj = MyThread()  # Create worker thread object
obj.start()       # ← WORKER THREAD STARTS HERE

obj.join()        # ← MAIN THREAD WAITS HERE
print("Main program waited until thread finished.")  # MAIN THREAD CODE

