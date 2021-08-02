# RESTAURANT RESRVATION SYSTEM
# Created by Juanito C. Dela Cerna Jr. March 12, 2021

# class System
class System:
    # Free define constant variables
    # For Adults 500
    # For Children 300
    pay_for_adults = 500
    pay_for_children = 300   
    def __init__(self,row):
        # table row
        self.row = row

    def run(self):    
        print("=============RESTAURANT RESRVATION SYSTEM=============")
        print("   System Menu")
        print("                 (a) For view all reservation")
        print("                 (b) For make reservation")
        print("                 (c) For delete reservation")
        print("                 (d) For generate report")
        print("                 (e) For exit \n")

        # Check the record file
        # if there is existing records
        try:
            records = ""
            # read the file
            with open('record.txt', 'r') as record:
                for txt in record.readlines():
                    records = txt
                    
            # convert string to dictionary
            if len(records):
                r = eval(records)
                # get the last row id
                self.row = r['id']
        except IOError: # throw error if file not found
            # set the row to 0 if there is no records
            self.row = 0 
        
        # flag
        flag = True
        while flag:
            choose = input("Choose: ").lower()
            if(choose == "a"):
                # view all reservation
                vew_all_reservation()
            elif(choose == "b"):
                # increment the table row
                self.row += int(1)
                make_reservation(self.row)    
            elif(choose == "c"):
                # delete reservation
                delete_reservation()
            elif(choose == "d"):
                # generate a report
                generate_report(System.pay_for_adults, System.pay_for_children)
            elif(choose == "e"):
                flag = exit()


# Person class
class Person:
    # initialize the dictionary
    information = {'id':'','name':'','date':'','time':'','adults':0,'children':0}    
    def __init__(self, row, name, date, time, adults, children):
        self.row = row
        self.name = name.title()
        self.date = date
        self.time = time
        self.adults = int(adults)
        self.children = int(children)
        Person.information['id'] = self.row
        Person.information['name'] = self.name
        Person.information['date'] = self.date
        Person.information['time'] = self.time
        Person.information['adults'] = self.adults
        Person.information['children'] = self.children
    def get_person(self):
        return self.information
               

# view all reservation
def vew_all_reservation():
    try:
        # table header
        print("# | Date       | Time    | Name      | Adults | Children ")
        # read the file
        with open('record.txt', 'r') as record:
            for row in record.readlines():
                data = eval(row.strip())
                print(f"{data['id']} | {data['date']} | {data['time']} | {data['name']}   | {data['adults']}      | {data['children']}        ")
               
    except IOError: # throw error if file not found
        print("Error: File not found")


# make reservation
def make_reservation(row):
    try:
        # name must be a string
        name = input("Enter name(String): ")
        # date must be a string 
        date = str(input("Enter date(String): ")) 
        # time must be a string 
        time = str(input("Enter time(String): "))
        # adults and children must be an integer
        adults = int(input("Enter adults(Integer): "))
        children = int(input("Enter children(Integer): "))
        # reservation
        r = Person(row,name,date,time,adults,children)
        # next line delimiter
        next_line = "\n"
        # create and write the data input
        with open('record.txt', 'a') as record:
           record.write(format(r.get_person()) +" "+next_line)
    except ValueError:
        print("Oops! enter an integer!")

# delete reservation 
def delete_reservation():
    try:
        row_id = input("Enter the reservation nunber to remove: ")
        # for new dictionary 
        string = ""
        # this is the old dictionary 
        records = ""
        # read the file
        with open('record.txt', 'r') as record:
            for row in record.readlines():
                records = eval(row.strip())
                if int(row_id) != int(records['id']):
                    string += row.strip() +"\n"

        # clear the .txt file
        with open('record.txt', 'w') as new_record:
           new_record.write("")            

        # write the new dictionary to the .txt file
        with open('record.txt', 'a') as new_record:
           new_record.write(string)                   
    except IOError: # throw error if file not found
        print("Error: File not found")
    except ValueError:
        print("Please enter an integer")


def generate_report(_500, _300):
    try:
        total_no_of_adults = 0
        total_no_of_kis = 0
        # table header
        print("\n")
        print("# | Date       | Time    | Name           | Adults | Children | subtotal")
        # read the file
        with open('record.txt', 'r') as record:
            for row in record.readlines():
                data = eval(row.strip())
                # reservation pay for adults
                _adults =  _500 * int(data['adults'])
                _kids = _300 * int(data['children'])
                subtotal = _adults + _kids
                print(f"{data['id']} | {data['date']} | {data['time']} | {data['name']}    | {data['adults']}      | {data['children']}        | {subtotal} ")
                # grand total
                total_no_of_adults += int(data['adults'])
                total_no_of_kis += int(data['children'])

        grand_total = float((total_no_of_adults * _500) + (total_no_of_kis * _300))
        print("\n")
        print(f"Total number of adults: {total_no_of_adults}")
        print(f"Total number of kids: {total_no_of_kis}")
        print("Grand total: PHP {:.2f}".format(grand_total))
        print("\n")
        print("------------------------------ nothings follows ------------------------------")
               
    except IOError: # throw error if file not found
        print("Error: File not found")

def exit():
    print("Thank you!")
    return False

# System initialization
s = System(0) # 0 is the initial value for the table row
s.run()
    




