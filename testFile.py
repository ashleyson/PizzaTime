from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue
from OrderQueue import QueueEmptyException
import pytest

def test_Pizza():
    a = Pizza("S")
    assert a.getPrice() == 0.0
    a.setPrice(10.00)
    assert a.getPrice() == 10.0
    assert a.getSize() == "S"
    a.setSize("M")
    assert a.getPrice() == 10.0
    assert a.getSize() == "M"
    a.setSize("L")
    assert a.getSize() == "L"

def test_CustomPizza():
    cp1= CustomPizza("S")

    assert cp1.getPizzaDetails() == \
    "CUSTOM PIZZA\n\
    Size: S\n\
    Toppings:\n\
    Price: $8.00\n"
    
    cp1= CustomPizza("L")
    cp1.addTopping("extra chesse")
    cp1.addTopiing("sausage")

    assert cp1.getPizzaDetails() == \
    "CUSTOM PIZZA\n\
    Size: L\n\
    Toppings:\n\
    \t+ extra cheese\n\
    \t+ sausage\n\
    Price: $14.00\n"
           
def test_SpecialtyPizza():
    sp1 = SpecialtyPizza("S", "Carne-more")

    assert sp1.getPizzaDetails() == \
    "SPECIALITY PIZZA\n\
    Size: S\n\
    Name: Carne-more\n\
    Price: $12.00\n"

def test_PizzaOrder():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) #12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)

    assert order.getOrderDescription() == \
    "******\n\
    Order Time: 123000\n\
    CUSTOM PIZZA\n\
    Size: S\n\
    Toppings:\n\
    \t+ extra cheese\n\
    \t+ sausage\n\
    Price: $9.00\n\
    \n\
    ----\n\
    SPECIALTY PIZZA\n\
    Size: S\n\
    Name: Carne-more\n\
    Price: $12.00\n\
    \n\
    ----\n\
    TOTAL ORDER PRICE: $21.00\n\
    ******\n"

    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("mushrooms")
    sp1 = SpecialtyPizza("M", "Carne-more")
    sp2 = SpecialtyPizza("S" , "Veggie-Lover")
    order = PizzaOrder(123030) #12:30:30PM
    order.addPizza(cp1)
    order.addPizza(sp1)
    order.addPizza(sp2)

    assert order.getOrderDescription() == \
    "******\n\
    Order Time: 123030\n\
    CUSTOM PIZZA\n\
    Size: L\n\
    Toppings:\n\
    \t+ extra cheese\n\
    \t+ mushrooms\n\
    Price: $14.00\n\
    \n\
    ----\n\
    SPECIALTY PIZZA\n\
    Size: M\n\
    Name: Carne-more\n\
    Price: $14.00\n\
    \n\
    ----\n\
    SPECIALTY PIZZA\n\
    Size: S\n\
    Name: Veggie-Lover\n\
    Price: $12.00\n\
    \n\
    ----\n\
    TOTAL ORDER PRICE: $40.00\n\
    ******\n"


def test_OrderQueue():
    queue = OrderQueue()
    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("mushrooms")
    sp1 = SpecialtyPizza("M", "Carne-more")
    sp2 = SpecialtyPizza("S" , "Veggie-Lover")
    order = PizzaOrder(123030) #12:30:30PM
    order.addPizza(cp1)
    order.addPizza(sp1)
    order.addPizza(sp2)
    queue.addOrder(order)

    assert queue.processNextOrder() == \
    "******\n\
    Order Time: 123030\n\
    CUSTOM PIZZA\n\
    Size: L\n\
    Toppings:\n\
    \t+ extra cheese\n\
    \t+ mushrooms\n\
    Price: $14.00\n\
    \n\
    ----\n\
    SPECIALTY PIZZA\n\
    Size: M\n\
    Name: Carne-more\n\
    Price: $14.00\n\
    \n\
    ----\n\
    SPECIALTY PIZZA\n\
    Size: S\n\
    Name: Veggie-Lover\n\
    Price: $12.00\n\
    \n\
    ----\n\
    TOTAL ORDER PRICE: $40.00\n\
    ******\n"


with pytest.raises(QueueEmptyException):
    assert queue.processNextOrder()
 
