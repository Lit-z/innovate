import string

# imports the alphabet as a string in lower case
letters = string.ascii_lowercase

# creates a list on the string separating each character into it's own term
alpha_list = list(letters)

# prints out the elements of the list 1 by 1 (so the alphabet)
i = 0
for letter in alpha_list:
    print(alpha_list[i])
    i += 1

# picking a letter with a user defined input
def user_letter():
    pick = input('Enter a whole number between 1 and 26 for corresponding letter: ')
    while pick.isdigit() == False:      # rejects non integer inputs
        pick = input('Enter an whole number (between 1 and 26): ')

# calculates the letter value from the user defined input (pick - 1)
    if 1 <= int(pick) <=26:             # will reject numbers out of the range
        pick = int(pick) - 1
        print(f'Your chosen letter is {alpha_list[pick]}')
    else:
        print('Invalid number, please enter correctly')    
        user_letter()                   # loops back if number is rejected

user_letter()