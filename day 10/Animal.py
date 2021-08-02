class Animal:
    def __init__(self):
        self.multicellular = True
        self.eukaryotic = True
        
    def breath(self):
        return "I breathe oxygen."

    def feed(self):
        return "I eat food."

class Herbivore(Animal):
    def __init__(self):
        super().__init__()
        self.food = "plants"

    def feed(self):
        return "I eat only "+ self.food +". I am vegetarian."

h = Herbivore()
print(h.feed()+" "+h.breath())
