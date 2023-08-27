class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return '{} is {} years old'.format(self.name, self.age)
    
    def speak(self, sound):
        return '{} says {}'.format(self.name, sound)
    
    def birthday(self):
        self.age += 1

""" philo = Dog('Philo', 5)
mikey = Dog('Mikey', 6)

mikey.age = 7
philo.species = 'mouse'

print('{} is {} and {} is {}'.format(philo.name, philo.age, mikey.name, mikey.age))

if philo.species == 'mammal':
    print('{} is a {}'.format(philo.name, philo.species)) """

mikey = Dog('Mikey', 6)

print(mikey.description())

print(mikey.speak('Gruff, gruff!'))

mikey.birthday()

print(mikey.description())