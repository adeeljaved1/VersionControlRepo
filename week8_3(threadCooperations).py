import threading
import random
import time

balance = 0
attempt = 0

def withdraw_task(cond):
    global balance
    global attempt
    
    while(attempt < 10):
        with cond:
            time.sleep(0.5)
            print('Withdraw task started by ',threading.currentThread().getName())
            amount = random.randint(1, 10) # a random amount between 1 and 10 to be withdrawn
            while(balance < amount):
                print('Attempt to withdraw', amount, ' --Not sufficient fund. Wait for a deposit----------------')
                cond.wait() # wait and send signal to producer (1.e, deposit_task) threads
                
            balance -= amount
            print('\t\t\t Withdraw: ', amount, '\t\t\t Balance', balance)
        attempt += 1
        
def deposit_task(cond):
    global balance
    global attempt
    
    while (attempt < 10):
    #while(True):  keep depositing
        with cond:
            time.sleep(0.5)
            print('Deposit task started by ', threading.currentThread().getName())
            amount = random.randint(1, 10) # a random amount between 1 and 10 to be deposited
                
            balance += amount
            print('\t\t\t Deposit: ', amount, '\t\t\t Balance', balance)
            cond.notify_all() # send a signal to all waiting consumer (i.e., withdraw_task) threads
        attempt += 1
        
if __name__ == '__main__':
    condition = threading.Condition()
    
    w1 = threading.Thread(name='customer1-withdraw', target=withdraw_task, args=(condition,))
    d1 = threading.Thread(name='customer2-deposit', target=deposit_task, args=(condition,))
    
    w1.start()
    d1.start()
    
    w1.join()
    d1.join()
    
    print('Thank you. Both withdraw and deposit tasks are Done!!!')