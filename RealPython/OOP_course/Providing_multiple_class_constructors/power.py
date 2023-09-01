class CumulativePowerFactory:
    def __init__(self, exponent=2, *, start=0):
        self.exponent = exponent
        self.total = start
    
    def __call__(self, base):
        power = base ** self.exponent
        self.total += power
        return power