#Example
import threading
def add():
  for temp in range(8):
        print("Thread is running! from other parallel thread")

# Create and start the thread
my_thread = threading.Thread(target=add)
  # Starts running in parallel
my_thread.start()

def task():
    for temp in range(3):
        print("Thread is running! from main thread")
task()