word = input("Enter Word: ")

# Reverse the input word
def reverse(word):
    _word = ""
    for i in range(len(word)-1,-1,-1):
        _word += word[i]
    return _word

# Ouput the reverse word and all character turn into capitalize letters
# An count how many letters
print(f"{ reverse(word).upper() } ({ len(reverse(word)) } characters)")
        
    
