class Person:
    count = 0
    def __init__(self, name="John"):
        self.name = name
        Person.count += 1

p1 = Person()
p2 = Person()
p3 = Person()
print(Person.count)
