import multiprocessing
#Example 1


def add():
    print("Process started!")
if __name__ == "__main__": # ← ADD THIS!
    process = multiprocessing.Process(target=add,name="process:1")
    print(process)
    process.start() # Starts running the task in a separate process
    print(process.is_alive())
    
    process.kill() #"Force kill NOW" - Instantly murders process
    process.join()
    print(f"after kill the process -{process.is_alive()}")


#Example 2
#code to make process connect to other new thread
#code for hello world in new process
def hello_world():
    print("Hello, World!")
if __name__ == "__main__":
    process2 = multiprocessing.Process(target=hello_world,name ="Process-2")
    process2.start()
    process2.join()





