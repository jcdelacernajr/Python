class Company:
    def __init__(self, name, proj):
        self.name = name
        self._proj = proj
        self.ccode = ""
   
    def show(self):
        print("The code of the company is = "+ self.ccode)

class Emp(Company):
    def __init__(self, e_name, sal, c_name, proj):
        super().__init__(c_name, proj)
        self.name = e_name
        self.__sal = sal

    def get_sal(self):
        return self.__sal

c = Company("Stark Industries", "Mark 4")
e = Emp("Steve", 9999999, c.name, c._proj)

print(f"Welcome to {c.name}. Here {e.name} is working on {e._proj}. He earns {e.get_sal()}")
