import threading
import time

balance = 0
my_lock = threading.Lock() # option 1: using a lock
my_semaphore = threading.Semaphore(1) # option 2: using a semaphore
my_rlock = threading.RLock() # option 3: using reentrant lock

# Lock is basic synchronization mechanism
# when a thread acquires a lock, no other thread can acquire it until the first thread release it.
# Prevents multiple threads from accessing the critical region at the same time

# # Option 1: Using lock
# def add_amount():
#     global balance
#     my_lock.acquire() # acquire the lock
#     for i in range(100):
#         # time.sleep(0.1)
#         balance += 1
#     my_lock.release() # release the lock
     
    
# Semaphore is a more general synchronization primitive.
# A binary semaphore (semaphore(1)) behaves like a lock (one thread at a time)
# A semaphore allows a count-based control , e.g, semaphore(3) allows 3 threads to enter in critical region at once
# Option 2: Using Semaphore
# def add_amount():
#     global balance
#     my_semaphore.acquire() # acquire the semaphore
#     for i in range(100):
#         # time.sleep(0.1)
#         balance += 1
#     my_semaphore.release() # release the semaphore
   

#A reentrant lock (RLock) allows a thread to acquire the same lock multiple times.
# used when a function needs to call another function that also acquires the lock. 
# # Option 3: Using reentrant lock
# def add_amount():
#     global balance
#     my_rlock.acquire() # acquire the reentrant lock
#     for i in range(100):
#         # time.sleep(0.1)
#         balance += 1
#     my_rlock.release() # release the reentrant lock
   
def synchronized(func):
    lock = threading.Lock()
    def synched_function(*args, **kws):
        with lock:
            return func(*args, **kws)
    return synched_function

@synchronized
def add_amount():
    global balance
    for i in range(100):
        balance += 1

@synchronized
def withdraw_amount():
    global balance
    for i in range(100):
        balance -= 1
        
if __name__ == '__main__':
    customer1 = threading.Thread(target=add_amount)
    customer2 = threading.Thread(target=add_amount)
    
    customer3 = threading.Thread(target=withdraw_amount)
    customer4 = threading.Thread(target=withdraw_amount)
    
    customer1.start()
    customer2.start()
    customer3.start()
    customer4.start()
    customer1.join()
    customer2.join()
    customer3.join()
    customer4.join()
    
    print(f'Current Balance: {balance}')