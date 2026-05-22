import multiprocessing
import time

def task():
    print("I am in worker task")
    time.sleep(3)
    print("worker task finished")

if(__name__=="__main__"):
    process=multiprocessing.Process(target=task)  #Main creates Worker
    process.start()       #Worker begins running task
    process.join()         #Main WAITS for Worker
    print("Main program waited to finish the task")





