# User input
name = input("Employee name:")
hours = input("Enter number of hours:")
sss = input("SSS Contribution:")
philhealth = input("Philhealth:")
housing = input("Housing loan:")

# Free define variable
rate = 500
tax = 0.1

# Display the user information
print("\n")
print("============PAYSLIP============")
print("=====EMPLOYEE INFORMATION======")
print("Employee name: {}".format(name))
print("Rendered hours: {}".format(int(hours)))
print("Rate per hour: {}".format(rate))
total_gross_salary = float(rate) * float(hours)
print("Gross Salary: {}\n".format(total_gross_salary))

# Display the user deductions
print("==========DEDUCTIONS===========")
print("SSS: {}".format(float(sss)))
print("Philhealth: {}".format(float(philhealth)))
print("Housing: {}".format(float(housing)))

total_tax = total_gross_salary * tax
total_deductions = float(sss) + float(philhealth) + float(housing) + float(total_tax)

print("Tax: {}".format(total_tax))
print("Total deductions: {}\n".format(total_deductions))

# Display the Employee Net salary
net_salary = total_gross_salary - total_deductions
print("Net Salary: {}".format(net_salary))

