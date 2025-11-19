# Python Class

class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello {}!".format(self.name))

SJBSR = Person("SJBSR")
SJBSR.say_hello()
