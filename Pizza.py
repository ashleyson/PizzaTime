#Pizza.py
class Pizza():
    def __init__(self,size):
        self.price = 0.0
        self.size = size

    def setSize(self,size):
        self.size = size

    def getSize(self):
        return str(self.size)

    def setPrice(self,price):
        self.price = price

    def getPrice(self):
        return self.price
            
