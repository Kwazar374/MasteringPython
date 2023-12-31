from functools import singledispatchmethod

class DemoClass:
    @singledispatchmethod
    def generic_method(self, arg):
        print(f"Do something with argument of type: {type(arg).__name__}")

    @generic_method.register
    def _(self, arg: int):
        print("Implementention for an int argument...")

    @generic_method.register(str)
    def _(self, arg):
        print("Implementation for a str argument...")