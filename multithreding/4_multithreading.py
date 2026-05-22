#Example of multithreading
#Multiple threads in 1 process,share memory,Good for I/O (network, files),threading.Thread()
import threading
import time
# Define a function to run in a thread
def print_numbers():
    for i in range(8):
        print(f"[{threading.current_thread().name}] Number: {i}")
        time.sleep(1)
def func():
    for temp in range(10):
        print(f"[{threading.current_thread().name}] Thread is running!")
        time.sleep(1)

# Create multiple threads
thread1 = threading.Thread(target=print_numbers, name="Thread:1")
thread2 = threading.Thread(target=func, name="Thread:2")

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Main thread: All threads finished.")

   