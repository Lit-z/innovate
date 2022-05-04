# initial variables
welcome = 'Welcome to Code Nation!'
str_len = len(welcome)

# checking for even by checking for /2 with no remainders (%2 == 0)
if str_len % 2 == 0:
    print(welcome)
    print('Things looking pretty even')
else:
    print(welcome)
    print("We're odd around here")
