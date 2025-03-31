import threading
import time

balance = 0

def add_amount():
    global balance
    for i in range(100):
        # time.sleep(0.1)
        balance += 1
        
if __name__ == '__main__':
    customer1 = threading.Thread(target=add_amount)
    customer2 = threading.Thread(target=add_amount)
    
    customer1.start()
    customer2.start()
    customer1.join()
    customer2.join()
    
    print(f'Current Balance: {balance}')