#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


'''
file.read() -> get the entire file
file.readlines() -> get a list of line strings
file.readline() -> get a line
'''



# open the name file first
with open("./Input/Names/invited_names.txt", "r") as name_file:
    # store all the names in a list
    names = name_file.readlines()
    print(names)

# open the letter
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    # get the whole file of the letter
    letter_content = letter.read()
    # iterating over each name
    for name in names:
        # to remove the space at the end of the sentence
        stripped_name = name.strip()
        new_letter = letter_content.replace("[name]", stripped_name)
        # making a letter for each name
        with open(f"./Output/ReadyToSend/{stripped_name}.txt", "w") as write_letter:
            write_letter.write(new_letter)


