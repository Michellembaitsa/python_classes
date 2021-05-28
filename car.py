class Car:
    def __init__(self,make,model,price,color):
        self.make=make
        self.model-=model
        self.price=price
    def accelerate(self):
       return f"{self.make } {self.model} has a maximum speed of 180 km/h, The {self.color} one goes for {self.price}"
    def hoot(self):
       return f"{self.make } {self.model} hoots at a rate of 10 hoots per minute"         