# person class
class Person:
    information = ""
    # initialize the class constructor
    def __init__(self, new_name, new_id, new_birth_date):
        self.name = new_name
        self.id = new_id
        self.birth_date = new_birth_date
        Person.information = "ID: "+ self.id + ", Name: "+ self.name +", Birth data: "+ self.birth_date

    # function
    def get_details(self):
        return self.information # return the person information

# student class
class Student(Person):
    information = ""
    def __init__(self, new_name, new_id, new_birth_date, new_grade):
        Person.__init__(self, new_name, new_id, new_birth_date)
        self.grade = new_grade
        Student.information = "ID: "+ self.id + ", Name: "+ self.name +", Birth date: "+ self.birth_date +", Grade: "+ str(float(self.grade))

    # get student details
    def get_details(self):
        return Student.information # return the student information

# employee class
class Employee(Person):
    information = ""
    def __init__(self, new_name, new_id, new_birth_date, new_salary):
        Person.__init__(self, new_name, new_id, new_birth_date)
        self.salary = new_salary
        Employee.information = "ID: "+ self.id + ", Name: "+ self.name +", Birth date: "+ self.birth_date +", Salary: "+ str(float(self.salary))

    # get employee details
    def get_details(self):
        return Employee.information # return the employee information

# instance for student
student1 = Student("Juanito C. Dela Cerna Jr.", "0101","Agust 27, 1988", 95)      
print("Student #1: " + student1.get_details())
# instance for student
student2 = Student("Merwy G. Mapait", "0223","July 3, 1998", 90)      
print("Student #2: " +  student2.get_details())
# instance for employee
employee = Employee("Anthony C. Taunan", "0420","December 25, 1990", 10000)      
print("Employee:  " + employee.get_details())
# instance for person
person = Person("Rodrigo Roa Duterte", "0128","March 28, 1945")      
print("Person: " + person.get_details())



