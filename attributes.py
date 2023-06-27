class Person:
    number_of_people = 0
    
    def __init__(self, name):
        self.name = name
        Person.add_person()
    
    @classmethod    
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
        
p1 = Person('Tim')
p2 = Person('Jill')

# Person.number_of_people = 8
print(p1.number_of_people)
p3 = Person('Bill')
# Person.number_of_people = 2
print(Person.number_of_people)

print(Person.number_of_people_())