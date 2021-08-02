
# Function
def user_input():
    n1,n2 = input("Enter first number and Enter second number: ").split()
    _sum = int(n1) + int(n2)
    print(f"The sum of number 1 and number 2 is: {_sum}")

# Initialize
user_input()      

# Asking
ask = input("Want to try again? ").lower()
if str(ask) == "y":
    user_input()
else:
    print("Thank you!")


