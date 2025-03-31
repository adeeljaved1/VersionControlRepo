import threading
import time

# Task to print a char
class PrintChar(threading.Thread):
    def __init__(self, char_to_print, times):
        super().__init__()
        self.char_to_print = char_to_print
        self.times = times
        
    def run(self): # override the run() method to define the task to be performed
        for i in range(0, self.times):
            print(self.char_to_print)
            time.sleep(0.35)
        
# Task to print a number
class PrintNumber(threading.Thread):
    def __init__(self, number_to_print, times):
        super().__init__()
        self.number_to_print = number_to_print
        self.times = times
        
    def run(self): # override the run() method to define the task to be performed
        for i in range(0, self.times):
            print(self.number_to_print)
            time.sleep(0.35)        

if __name__ == '__main__':
    t1 = PrintChar('A', 1000)
    t2 = PrintNumber(2, 1000)
    t3 = PrintChar('B', 1000)
    t4 = PrintNumber(5, 1000)
    
    t1.start() # the run() method of PrintChar class will automatically be called
    t2.start() # the run() method of PrintChar class will automatically be called
    t3.start() # the run() method of PrintChar class will automatically be called
    t4.start() # the run() method of PrintChar class will automatically be called
    
    t1.join() # causes main thread to wait for t1 thread to finish
    t2.join() # causes main thread to wait for t2 thread to finish

    print('Main thread DONE!!!') # will be printed after t1 and t2 are done, but may be beofre t3 and t4 complete their tasks