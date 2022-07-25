student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# creating a dictionary with the following {'A': 'Alfa', 'B': 'Bravo'}
alphabet_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(alphabet_dict)
# {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'}

user_words = input("Enter a word, please!:").upper()
# for example: if the word is hello
'''
we would need to traverse the string 'hello' and letter by letter
h -> alphabet_dict[h] = Hotel
e -> alphabet_dict[e] = Echo
l -> alphabet_dict[l] = Lima
l -> alphabet_dict[l] = Lima
o -> alphabet_dict[o] = Oscar
'''
match_letter_dict = [alphabet_dict[letter] for letter in user_words]
print(match_letter_dict)
