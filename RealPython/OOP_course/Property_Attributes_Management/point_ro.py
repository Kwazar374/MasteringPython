class WriteCoordinateError(Exception):
    pass

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @x.setter
    def x(self, value):
        raise WriteCoordinateError("x coordinate is read-only")
    
    @y.setter
    def y(self, value):
        raise WriteCoordinateError("y coordinate is read-only")