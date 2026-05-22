#Race conditions are non-deterministic - they depend on exact CPU timing. 
# Sometimes you get "lucky" and don't see corruption.
import threading
import time

shared_counter = 0
lock = threading.Lock()

def increment_with_lock():
    global shared_counter
    for _ in range(1000):
        with lock:
            shared_counter += 1

def increment_without_lock():
    global shared_counter
    for _ in range(1000):
        #temp=shared_counter  ## Thread switch can happen HERE
        time.sleep(0.001)  # 1 millisecond pause
        #shared_counter=temp+ 1
        shared_counter+=1
        
def demonstrate_lock_necessity():
    """Demonstrate why locks are necessary"""
    global shared_counter
    
    print("=== WITHOUT LOCK (Race Condition) ===")
    shared_counter = 0
    
    threads = [threading.Thread(target=increment_without_lock) for _ in range(5)]
    for t in threads:t.start()
    for t in threads:t.join()
    
    print(f"Expected value: {5 * 1000}")
    print(f"Actual value without lock: {shared_counter}")
    print(f"Data corruption occurred: {shared_counter != 5000}")

def demonstrate_lock_protection():
    """Demonstrate how locks prevent race conditions"""
    global shared_counter
    
    print("\n=== WITH LOCK (Thread Safe) ===")
    shared_counter = 0
    
    threads = [threading.Thread(target=increment_with_lock) for _ in range(5)]
            # ↑ Creates 5 threads, each doing 10,000 increments
    for t in threads: t.start()
    for t in threads: t.join()
    
    print(f"Expected value: {5 * 1000}")
    print(f"Actual value with lock: {shared_counter}")
    print(f"Data is safe: {shared_counter == 5000}")

if __name__ == "__main__":
    demonstrate_lock_necessity()
    demonstrate_lock_protection()


    