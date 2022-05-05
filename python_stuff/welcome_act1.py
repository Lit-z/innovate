# initial variables
welcome = 'Welcome to Code Nation!'
str_len = len(welcome)

# checking for even by checking for /2 with no remainders (%2 == 0)
def even_check():
    if str_len % 2 == 0:  
        print(f'the string "{welcome}" is an amazing {str_len} characters long it\'s looking pretty even')
    else:
        print(f'the string "{welcome}" is an amazing {str_len} characters long and We\'re odd around here')

# calling the function
even_check()