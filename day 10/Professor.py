class Professor:
    def __init__(self, name, id_num, gender, bday, salary, rank):
        self.name = name
        self.id_num = id_num
        self.gender = gender
        self.bday = bday
        self.salary = salary
        self.rank = rank
    def get_salary(self):
        if self.rank in ["Assistant Professor","Associate Professor", "Full Professor"]:
            self.salary += 5000
        elif self.rank == "Lecturer":
            self.salary += 500
        else:
            self.salary = self.salary
        return self.salary

p1 = Professor('Charles Xavier', 'cx0001', 'male','01/01/1945',50000, 'Full Professor')
p2 = Professor('Jean Grey','jg0020','female','08/08/1988',25000,'Assistant Professor')
p3 = Professor('Hank McCoy','hm0003','male','07/07/1977',39000,'Associate Professor')
p4 = Professor('Logan Wolverine','lw0010','male','02/02/1855',18000,'Lecturer')
p5 = Professor('Adagulfo Sungal','as0100','male','12/12/1955',9000,'visiting professor')

faculty = [p1,p2,p3,p4,p5]
a= 0
for f in faculty:
    a += f.get_salary()
print(a)
        
