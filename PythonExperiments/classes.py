'''
    here we will study about the classes and object oriented programming concepts using exanples
'''

import os
import sys

class Student():
    def __init__(self):
        print "I am student"

    def setName(self,name):
        self.myname = name

    def getName(self):
        return self.myname

    def hellos(self):
        print "hello bro !!!"

class Monitor(Student):
    def __init__(self):
        print "i am monitor of class"

    def __init__(self, name):
        self.myname = name

    def hellom(self):
        print "wassup dude !!!"

class President(Student,Monitor):
    def __init__(self):
        super.__init__(President, stri)
    pass


s1 = Student()
s1.setName("jayesh")
print "hi " + s1.getName()

s2 = Monitor()
s2.setName("rishi")
print "hi Monitor " + s2.getName()

s3 = President("arnub")
s3.setName("Pranab ")
print "hi  " + s3.getName()
s3.hellom()