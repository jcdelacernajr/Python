class a:
    def __init__(self, name):
        self.name = name
    def get(self):
        return self.name

class p(a):
    def __init__(self, name, occu):
        super().__init__(name)
        self.job = occu
    def get(self):
        return self.job

class c(p):
    def __init__(self, name, emp, add):
        super().__init__(name, emp)
        self.add = add
    def get(self):
        return self.add

c = c("Juan", "Developer", "Catalunan")
print(c.get())

