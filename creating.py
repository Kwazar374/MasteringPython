class Dog:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def add_one(self, x):
        return x+1
    
    def bark(self):
        print('bark')
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age
        

d = Dog('Tim', 34)
# print(d.name)
print(d.get_name())
print(d.get_age())
d.set_age(15)
print(d.get_age())
d2 = Dog('Bill', 12)
# print(d2.name)

d.bark()
print(d.add_one(5))

print(type(d))