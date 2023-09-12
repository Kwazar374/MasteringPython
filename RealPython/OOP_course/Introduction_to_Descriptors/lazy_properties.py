import time

class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]
    
class DeepThought:
    @LazyProperty
    def meaning_of_life(self):
        time.sleep(3)
        return 42
    
my_deep_thought_instance = DeepThought()
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)

""" First, you’ll get the result returned from the __get__ method of the data descriptor named after the attribute you’re looking for.

If that fails, then you’ll get the value of your object’s __dict__ for the key named after the attribute you’re looking for.

If that fails, then you’ll get the result returned from the __get__ method of the non-data descriptor named after the attribute you’re looking for.

If that fails, then you’ll get the value of your object type’s __dict__ for the key named after the attribute you’re looking for.

If that fails, then you’ll get the value of your object parent type’s __dict__ for the key named after the attribute you’re looking for.

If that fails, then the previous step is repeated for all the parent’s types in the method resolution order of your object.

If everything else has failed, then you’ll get an AttributeError exception. """