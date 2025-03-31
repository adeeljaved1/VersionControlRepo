import threading
import time

class WriteNote(threading.Thread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        print('Starting writing note...')
        time.sleep(3) # thread sleeps for 3 secs
        print('Done Writing.')
        
if __name__ == '__main__':
    print('Main thread started.')
    my_note = WriteNote() # create a WriteNode() object
    print(f'Is the writing thread alive? {my_note.is_alive()}')
    
    print('WriteNote thread has been started by the main thread.')
    my_note.start()
    print(f'Is the writing thread alive? {my_note.is_alive()}')
    print('Main thread goes for sleeping.')
    time.sleep(0.5)
    print(f'Is the writing thread alive? {my_note.is_alive()}')
    print('main thread join the writeNote thread, i.e., waits for WriteNote to be finished first.')
    my_note.join()
    print(f'Is the writing thread alive? {my_note.is_alive()}')
    print('Both threads are done!')
    print(f'Is the writing thread alive? {my_note.is_alive()}')