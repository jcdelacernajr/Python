class Father:
    def __init__(self):
        self.eyes = 'blue'

class Mother:
    def __init__(self):
        self.hair = 'brown'

class Child(Father, Mother):
    def __init__(self):
        Mother.__init__(self)
        Father.__init__(self)
        self.height = '175cm'

a = Child()
print(f"{a.eyes} {a.hair} {a.height}")
