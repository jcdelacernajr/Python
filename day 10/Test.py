class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_message(self):
        print("Name: "+ self.name)
        print("Age: "+ self.age)

try:
    t1 = Test()
except Exception:
    print("yes")
else:
    t1.print_message()
