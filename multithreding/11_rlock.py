#threading.RLock() is a Reentrant Lock - same as Lock() but the same thread can
#acquire it multiple times without deadlocking
#Ex:1
import threading
# rlock = threading.RLock()

# def recursive_function(n):
#     with rlock:
#         if n > 0:
#             print(f"Recursion level: {n}")
#             recursive_function(n - 1)   
#         else:
#             print("Base case reached")
# recursive_function(3)

# #Ex:2 with acquire and release
# print("---------------------------------------")
# rlock = threading.RLock()

# def recursive_function1(n):
#     rlock.acquire()
#     print(f"Level {n}: acquired lock")
#     if n > 0:
#         recursive_function1(n - 1)
#     rlock.release()
# recursive_function1(3)

#Ex:3
class Counter:
    def __init__(self):
        self.value = 0
        self.mylock = threading.RLock()

    def increment(self):
        with self.mylock:
            self.value += 1
            print(f"Counter value: {self.value}")
counter = Counter()
threads = [threading.Thread(target=counter.increment) for _ in range(5)]

for t in threads:
    t.start()
for t in threads:
    t.join()    
print(f"Final counter value: {counter.value}")