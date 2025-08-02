#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as user_name:
    user_names = user_name.readlines()

# with open("./Input/Letters/starting_letter.txt") as read_letter:
#     letter = read_letter.read()
#     i = 0
#     for name in user_names:
#
#         strip_name = name.strip()
#         new_letter = letter.replace(PLACEHOLDER, name)
#
#         with open(f"./Output/ReadyToSend/user_{strip_name}{i + 1}.txt", mode='w') as save:
#             save.write(new_letter)

import  os

for name in user_names:
    user = name.strip()
    os.remove(f"./Output/ReadyToSend/user_{user}1.txt")