winning = {10,11,8,1,5,20}
players = {
"Jo":{1,8,10,27,12,15},
"JoJo":{1,8,27,3,4,9},
"Joe":{9,4,3,12,15,21},
}

count = 0
# Check the data using  for loop
for player, value in players.items():
    # Intersect the dictionary to count the data
    count = value.intersection(winning)
    # Multiply the count by 100 using len() method
    winning_price = 100 * len(count)
    # The players
    if(player == "JoJo"):
        print(f"JoJo won {winning_price} pesos!")
    if(player == "Jo"):
        print(f"Jo won {winning_price} pesos!")
    if(player == "Joe"):
        if(winning_price == 0):
            print(f"Jo won nothing")
        else:
            print(f"Jo won {winning_price} pesos!")
