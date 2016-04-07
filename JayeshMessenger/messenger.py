'''
    Basically, what we will be doing her is creating a messenger using threading concepts
     first milestone : two threads communicating with each other (sending & receiving)
     second milestone : to be able to send files between two threads

'''


import threading

class JayeshMessenger(threading.Thread):
    sendMessage = ""
    receiveMessage =""

    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def get_name(self):
        print threading.current_thread().name

    def send(self):
        sndmsg = input("send some message\n")
        self.sendMessage = sndmsg

    def recv(self):
        self.receiveMessage = self.sendMessage
        print self.receiveMessage

    def run(self):
        self.get_name()
        while True:
            self.send()
            self.recv()


f1 = JayeshMessenger("thread1 ")
f2 = JayeshMessenger("thread2 ")

f1.start()
f2.start()




