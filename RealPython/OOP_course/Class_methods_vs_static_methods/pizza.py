import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return f'Pizza({self.ingredients})'
    
    def area(self):
        return self._circle_area(self.radius)
    
    @classmethod
    def margherita(cls):
        return cls(['cheese', 'tomatoes'])
    
    @classmethod
    def prosciutto(cls):
        return cls(['cheese', 'tomatoes', 'ham', 'mushrooms'])
    
    @staticmethod
    def _circle_area(r):
        return r ** 2 * math.pi
