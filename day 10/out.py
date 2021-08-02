out = ""
try:
    a = "orange"
    if a == "apple":
        raise ValueError
    else:
        raise TypeError
except ValueError:
    out += "Apple Error"
except TypeError:
    out += "Orange Error"
else:
    print("No Error")
finally:
    out += "Fruit Error"
    print(out)

print("I love \
Python")
