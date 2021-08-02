# User input
name = input("Enter Name: ")
math_grade = input("Enter Math Grade: ")
science_grade = input("Enter Science Grade: ")
english_grade = input("Enter English Grade: ")

# Ouput
print("\n")
print("Name: {}".format(name.title()))
print("Math: {}".format(float(math_grade)))
print("Science: {}".format(float(science_grade)))
print("English: {}".format(float(english_grade)))

# Computation
passing_grade = 75.0
average = float(math_grade) + float(science_grade) + float(english_grade)
_average = average / 3

# Output
print("Average: {}".format(float(_average)))

print("\n")
if(_average >= passing_grade):
    print("Congratulations for passing the semester!")
else:
    print("Sorry but you failed the semester!")
