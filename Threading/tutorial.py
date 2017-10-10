import threading



class VasuMessenger(threading.Thread):
    def run(self):
        for _ in range(100):     # _ means that we dont care about the variable
            print(threading.currentThread().getName())

x = VasuMessenger(name='Send out messages')
y = VasuMessenger(name='Receive messages')
x.start()
y.start()