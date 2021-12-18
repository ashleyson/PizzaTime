#CustomPizza.py***
from Pizza import Pizza
class CustomPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.topping = []
        if self.size == "S":
            self.price = 8.00
        if self.size == "M":
            self.price = 10.00
        if self.size == "L":
            self.price = 12.00

    def addTopping(self, topping):
        self.topping.append(str(topping))
        if self.size == "S":
            self.price += 0.50
            
        elif self.size == "M":
            self.price += 0.75

        elif self.size == "L":
            self.price += 1.00

    def getPizzaDetails(self):
        string = ""
        for toppings in self.topping:
            if toppings == self.topping[-1]:
                string+=toppings
            else:
                string+=toppings+"\n\t+ "

        if len(self.topping) == 0:
            return "CUSTOM PIZZA\n\
Size: {}\n\
Toppings:\n\
Price: ${:.2f}\n".format(self.size,self.price)
        else:
            return "CUSTOM PIZZA\n\
Size: {}\n\
Toppings:\n\
\t+ {}\n\
Price: ${:.2f}\n".format(self.size,string,self.price)
    
    
