import random

# List of name
first_name = ['Juanito','Mark','Loyd','Rose','Victor','Merwyn','Anthony','Jay','Laurence','Lister']
middle_name = ['Chavez','Luayon','Candar','Mari','Tahon','Luzon','Mapait','Sixto','Bong','Nayunai']
last_name = ['Dela Cerna','Tantan','Taunan','Budiang','Pelpinosas','Suarez','Paster','Villiamore','Escanio','Bulacan']
list_of_person = []

# generate a random name
def generate():
    generated_name = first_name[random.randrange(0,10)] +" "+ middle_name[random.randrange(0,10)] +" "+ last_name[random.randrange(0,10)]
    list_of_person.insert(0,generated_name)
    return generated_name

# Run the script while true
flag = True
while flag:
    yes = input("Do you want to generate a name? ").lower()
    if(yes == "y"):
        # generate a name
        print(f"Output: Congratulations! Your new name is {generate()}")
    elif(yes == "n"):
        print("Output: Thank you!")
        if(len(list_of_person) == 0):
            print("")
        else:
            print("Output: {}".format(list_of_person))
        flag = False

