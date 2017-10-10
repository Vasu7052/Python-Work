import threading



class VasuMessenger(threading.Thread):
    def run(self):
        for _ in range(3):     # _ means that something but nothing
            print(threading.currentThread().getName())

x = VasuMessenger(name='Send out messages')
y = VasuMessenger(name='Receive messages')
x.start()
y.start()