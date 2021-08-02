# User input
def ask():
    print("Press (a) Addition")
    print("Press (b) Subtraction")
    print("Press (m) Multiplication")
    print("Press (d) Division")
    return input("Choose: ")

# addition
def addition():
    try:
        # statement
        n1 = input("Enter number 1: ")
        n2 = input("Enter number 2: ")
        print("Output: {}".format(float(n1) + float(n2)))     
    except ValueError as e:
        print(e)
    finally:
       try_again()

# Subtraction
def subtraction():
    try:
        # statement
        n1 = input("Enter number 1: ")
        n2 = input("Enter number 2: ")
        print("Output: {}".format(float(n1) - float(n2)))     
    except ValueError as e:
        print(e)
    finally:
       try_again()

# Multiplication
def multiplication():
    try:
        # statement
        n1 = input("Enter number 1: ")
        n2 = input("Enter number 2: ")
        print("Output: {}".format(float(n1) * float(n2)))     
    except ValueError as e:
        print(e)
    finally:
       try_again()

# division
def division():
    try:
        # statement
        n1 = input("Enter number 1: ")
        n2 = input("Enter number 2: ")
        print("Output: {}".format(float(n1) / float(n2)))     
    except ZeroDivisionError as e:
        print(e)
    finally:
       try_again()

# run function
def run():
    selected = ask()
    if(selected == "a"):
        addition()
    elif(selected == "b"):
        subtraction()
    elif(selected == "m"):
        multiplication()
    elif(selected == "d"):
        division()
  
def try_again():
    yes = input("Want to try again? (y/n) ").lower()
    if(yes == "y"):
       run()
    else:
        print("Thank you!")

# initialize the function
run()


