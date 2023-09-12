class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '{self.__class__.__name__}({self.color}, {self.mileage})'.format(self=self)
    
my_car = Car('red', 37719)
print(repr(my_car))
print(my_car)