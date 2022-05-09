# classes intro
class Person():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    
    def talk(self):
        print(f'Their name is {self.name}, they\'re {self.age} years old and {self.height}m tall')

someone = Person('Litz',1.86,30)

# how to call values from within the class
print(someone.name)
print(someone.age)
print(someone.height)
someone.talk()

# dictionaries breakdown
dict_1 = {
    6 : 30,
    'test':'why'}

dict_2 = {
    'yes': 'me',
    'no':'you'}

list_1 = [dict_1, dict_2]               # list of dictonaries

list_1[0][6] = 30000                    # can reference 6 cos it's a key in dict_1
list_1[1]['yes'] = 'them'

print(list_1)
print(list_1[0][6])

list_2 = [{'y': '1', 'n':'2'},          # list of dictionaries made in a diff way
    {'fancy':'list','while':'doing','this':'stuff'}] 

list_2[0]['n'] = 'infinity'
list_2[1]['this'] = 'madness'

print(list_2)
print(list_2[0]['n'])

dict_3 = dict_1 | dict_2                # adding dictionaries together
print(f'3rd dict: {dict_3}')

figure = dict_3.pop('no')        # removes the value with the key 'no' and stores the value
print(figure)

# a diff dictonary, setdefault() adds a value to stuff
countries = {
    'UK':'Manchester',
    'France':'Paris',
    'Spain':'Madrid',
    'Italy':'Rome'
}

countries.setdefault('Canada','Ottawa')
countries.setdefault('Denmark','Copenhagen')

# some diff ways of extracting values
print(countries.keys())
print(countries.values())

for i, value in countries.items():
    print(i,':',value)

