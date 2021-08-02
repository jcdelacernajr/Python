#free define variable
more_than_or_equal_10_years = ['10000','12000','15000']
below_10_years = ['5000','6000','7500']
_office = ['IT','ACCOUNTING','HR']

print("\n")
print("List of Office/Department:", end=" ")
print(_office)
print("\n")

# User input
years = input("Enter year in service: ")
office = input("Enter Office/Department: ")

# Computation for index 0
if(office == _office[0]): # _office[0] is IT
    salary = more_than_or_equal_10_years[0] # 10,000
    _salary = below_10_years[0] # 5,000
    if(int(years) >= int(10)):
        print("Employee's salary: {}".format(float(salary)))
    else:
        print("Employee's salary: {}".format(float(_salary)))

# Computation for index 1
if(office == _office[1]): # _office[1] is IT
    salary = more_than_or_equal_10_years[1] # 12,000
    _salary = below_10_years[1] # 6,000
    if(int(years) >= int(10)):
        print("Employee's salary: {}".format(float(salary)))
    else:
        print("Employee's salary: {}".format(float(_salary)))

# Computation for index 2
if(office == _office[2]): # _office[2] is IT
    salary = more_than_or_equal_10_years[2] # 15,000
    _salary = below_10_years[2] # 75,000
    if(int(years) >= int(10)):
        print("Employee's salary: {}".format(float(salary)))
    else:
        print("Employee's salary: {}".format(float(_salary)))
