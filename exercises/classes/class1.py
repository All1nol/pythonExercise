## Create a class named Vehicle with attributes color and speed.
## Add a method accelerate that takes a parameter increase
## and increases the speed by that amount.

class Vehicle:
    def __init__(self,color,speed):
        self.color = color
        self.speed =speed
    def accelerate(self, increase):
        self.speed += increase
        print(f"The {self.color} vehicle accelerated by {increase} units. Current speed: {self.speed}")

car = Vehicle("red",60)
car.accelerate(20)