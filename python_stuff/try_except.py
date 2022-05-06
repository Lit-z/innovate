# try and except as one function, means if entered incorrectly all values have 
# to be rentered
def add_up():
    test1 = input('enter first ')
    test2 = input('enter second ')
    try:
        print(f'one function test has {test1} + {test2} = {int(test1) + int(test2)}')
    except ValueError:          # type of error to reject
        print('Enter a correct value')
        add_up()

add_up()

# done as two functions to reject as the user enters an incorrect value
# means they only have to fix the incorrect value rather than entering all again
# requires use of globals and more coding than the above method but a bit more
# user friendly in terms of ui/ rejection of incorrect values
def first():
    global num1
    try:
        num1 = int(input('one: '))
    except ValueError:
        print('Error: please enter integer')
        first()

def second():
    global num2
    try:    
        num2 = int(input('two: '))
    except ValueError:
        print('Error: please enter integer')
        second()

first()
second()
print(f'separate functions {num1} + {num2} is: {int(num1) + int(num2)}')