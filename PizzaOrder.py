from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from Pizza import Pizza

class PizzaOrder:
    def __init__(self, time):
        self.pizzas = []
        self.time = time
  
    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time
  
    def addPizza(self, pizza):
        self.pizzas.append(pizza)
  
    def getOrderDescription(self):
        string = ""
        for pizzas in self.pizzas:
            if pizzas == self.pizzas[-1]:
                string += pizzas.getPizzaDetails() + "\n"
                string += "----"
            else:
                string += pizzas.getPizzaDetails() + "\n"
                string += "----\n"

            totalPrice = 0.0
        for pizzas in self.pizzas:
            totalPrice = sum(pizzas.getPrice() for pizzas in self.pizzas)
            return "******\n\
Order Time: {}\n\
{}\n\
TOTAL ORDER PRICE: ${:.2f}\n\
******\n".format(self.time, string, totalPrice)

    def getPizzas(self):
        return self.pizzas


  
