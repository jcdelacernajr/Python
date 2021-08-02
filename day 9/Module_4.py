
# Question 12
output = ""
try:
    a = "orange"
    if a == "apple":
        raise ValueError
    else:
        raise TypeError
except ValueError:
    output += "Apple Error"
except TypeError:
    output += "Orange Error"
else:
    print("No error")
finally:
    output += "Fruit Error"
    print(output)
