#Example without join()
import threading
import time

def worker():
    print("Worker starts")
    time.sleep(1)  # Slow worker
    print("Worker FINISHES")

print("Main starts")
t = threading.Thread(target=worker)
t.start()  # Worker runs independently

print("Main continues IMMEDIATELY")
time.sleep(2)
print("Main finishes")  # ← Main ends FIRST!

#Another Example 
# Define the task (function) for the thread
#test scenerio: test with time.sleep(), so it will raise error for main thread but still worker thread is running
print("------------------------------------------------------------")

def task():
    for temp in range(5):
        print(" WorkerThread is running!")
        time.sleep(1)
   
# Create the thread
my_thread = threading.Thread(target=task)

# Thread is created but not yet started
print("Thread created:", my_thread)
my_thread.start()

for temp in range(5):
        print("Main Thread is running!")
        #time.sleep()

