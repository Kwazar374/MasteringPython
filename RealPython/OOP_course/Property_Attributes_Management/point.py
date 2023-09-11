class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x
    
    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y
    
    def set_y(self, value):
        self._y = value

# using getter and setter methods in Python is usually considered
# as a bad practice and it's better to avoid it

class BetterPoint:
    def __init__(self, x, y):
        self.x
        self.y