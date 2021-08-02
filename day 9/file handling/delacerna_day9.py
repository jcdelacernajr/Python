# User options
print("=========================================")
print("Press (a) to add record")
print("Press (b) to view records")
print("Press (c) to clear all records")
print("Press (d) to exit")
print("=========================================")
# add record
def add_record():
    name = input("Enter name: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    # next line delimeter
    next_line = "\n"
    # create and write the data input
    with open('record.txt', 'a') as record:
        information = name.title()+", "+email+", "+address.title()
        record.write(information+" "+next_line)

# view records
def view_records():
    try:
        # read the file
        with open('record.txt', 'r') as record:
            for row in record.readlines():
                print(row.strip())
    except IOError: # throw error if file not found
        print("Error: File not found")
        
# clear all the records
def clear_all_records():
    open('record.txt', 'w')
    print("No records found.")
    
# exit
def exit():
    print("Thank you")
    return False

# flag
flag = True
while flag:
    choose = input("Choose: ").lower()
    if(choose == "a"):
        add_record()
    elif(choose == "b"):
        view_records()
    elif(choose == "c"):
        clear_all_records()
    elif(choose == "d"):
        flag = exit()
