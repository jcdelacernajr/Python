# Free define variable
name, grade = "", 0
dictionaries = dict()

# ask the user
def ask():
    print("Press (a) to add data")
    print("Press (d) to delete data")
    print("Press (e) to close the application")

# add function
def add():
    name = input("Enter name: ")
    grade = input("Enter grade: ")
    dictionaries[name] = grade
    print("Output: {}\n".format(dictionaries))  

# delete function
def delete():
    name = input("Enter a name to delete: ")   
    if len(dictionaries) == 0:
        print("Output: Record Empty!")
    else:
        del dictionaries[name]       
        print("Output: {}\n".format(dictionaries))

# Run the script while true
flag = True
while flag: 
    ask()
    choose = input("Choose: ").lower()
    if(choose == "a"):
        add()       
    elif(choose == "d"):      
        delete()
    elif(choose == "e"):
        print("Thank you")
        flag = False
        
        
    

