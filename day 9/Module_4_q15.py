class Person:
    def __init__(self, name="John"):
        self.name = name

p1 = Person()
p2 = Person("Mike")
print(p1.name+p2.name)
