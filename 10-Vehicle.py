#!/usr/bin/python

class Vehicle:
    # Class Attribute
    type = "car"

    # Initializer / Instance Attributes
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # instance's methods
    def description(self):
        print("\nThe car {} has a price of {} eur".format(self.name, self.price))

    def color(self, status):
        print("\nThe price of {} is refered for a car {}".format(self.name, status))

    def changecost(self,price):
        self.price=price


# Instantiate the Vehicle object
megane = Vehicle("Megane", 25000)
nissan = Vehicle("Nissan", 9000)

# access the class variable
print("\nThe Megane is a {}".format(megane.__class__.type))
print("The Nissan is a {}".format(nissan.__class__.type))

# access attributes instance

print("\nThe car {} has a price of {} eur".format(megane.name, megane.price))
print("The car {} has a price instead of {} eur".format(nissan.name, nissan.price))

# Instanziate a new Vehicle
m3 = Vehicle("BMW M3", 40000)
# Call
m3.description()
m3.color("used")

m3.changecost(42000)
m3.description()
#child class

class Camper(Vehicle):

     def __init__(self,nome,prezzo,mq):
         super().__init__(nome,prezzo)
         self.mq=mq

         # instance's methods

     def description(self):
         super().description()
         print("A camper is also a Vehicle")
         print("It has a dimension of",format(self.mq)+" mq")


marcopolo=Camper("Mercede MarcoPolo",80000,15)

marcopolo.description()