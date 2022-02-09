class test:
    def __init__(self):
        self.getString()
        self.printString()
    
    def getString(self):
        self.string = input("Write a string: ")
    
    def printString(self):
        print(self.string.upper())

test()
