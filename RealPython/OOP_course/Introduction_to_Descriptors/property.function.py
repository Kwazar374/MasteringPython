class Foo():
    def getter(self) -> object:
        print("accessing the attribute to get the value")
        return 42
    
    def setter(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")
    
    attribute1 = property(fget=getter, fset=setter)

my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)