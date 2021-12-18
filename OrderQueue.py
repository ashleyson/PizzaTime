from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from Pizza import Pizza
from PizzaOrder import PizzaOrder

class OrderQueue:
    def __init__(self):
        self.order = [0]
        self.sizeNow = 0
        
    def percUp(self,i):
        while i//2 > 0:
            if self.order[i].getTime() < self.order[i//2].getTime():
                tmp = self.order[i//2]
                self.order[i//2] = self.order[i]
                self.order[i] = tmp
            i = i//2
    def addOrder(self,pizzaOrder):
        self.order.append(pizzaOrder)
        self.sizeNow += 1
        self.percUp(self.sizeNow)


    def percDown(self,i):
        while (i*2) <= self.sizeNow:
            mc = self.minChild(i)
            if self.order[i].getTime() > self.order[mc].getTime():
                tmp = self.order[i]
                self.order[i] = self.order[mc]
                self.order[mc] = tmp
            i = mc

    def minChild(self,i):
        if i *2 +1 > self.sizeNow:
            return i * 2
        else:
            if self.order[i*2].getTime() < self.order[i*2+1].getTime():
                return i * 2
            else:
                return i * 2 + 1

    def processNextOrder(self):
        if self.order == [0]:
            raise QueueEmptyException
        
        root = self.order[1].getOrderDescription()
        self.order[1] = self.order[self.sizeNow]
        self.sizeNow -= 1
        self.order.pop()
        self.percDown(1)
        return root
class QueueEmptyException(Exception):
    pass


        
        
