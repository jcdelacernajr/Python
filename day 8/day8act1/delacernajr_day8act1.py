# employee class
class Employee:
    information = ""
    # initialize the class constructor
    def __init__(self, new_name, new_email, new_mobile_number):
        self.name = new_name
        self.email = new_email
        self.mobile_number = new_mobile_number
        Employee.information = "Name: "+ self.name +", Email: "+ self.email +", Mobile No.: "+ self.mobile_number

    # function
    def get_information(self):
        return self.information # return the employee information

# instantiate with new value
info1 = Employee("Juanito C. Dela Cerna Jr.", "jcdelacernajr@gmail.com","09201234561")
# print the employee information
print(info1.get_information())
# instantiate with new value
info2 = Employee("Mark T. Chavez", "mtchavez@gmail.com","09232513452")
# print the employee information
print(info2.get_information())
