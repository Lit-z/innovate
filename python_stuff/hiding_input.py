from getpass import getpass

actual_pw = '1234'

# function to check if a user input 'password' matches the variable actual_pw
# if it doesn't it loops back to the start of the function to guess again
# the getpass() hides the input as the user enters it in the terminal
def pw_hack():
    password = getpass('Password: ')
    if password == actual_pw:
        print('correct guess')
    else:
        print('incorrect guess')
        pw_hack()

pw_hack()