# User input
sentence = input("Create a sentence: ")

# Variable
number_count,letters_count, index = 0, 0, 0

while index < len(sentence):
    if (sentence[index].isdigit()):
        # Count how many numbers
        number_count += 1
    else:
        # Count how many letters
        letters_count += 1
    index += 1
        
# Output
print(f"The sentence contained {letters_count} letters and {number_count} numbers")

