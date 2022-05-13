a_list = [{'key1':'value1','key2':'value2','key3':'value3'}
,{'new1':'item1','new2':'item2','new3':'item3','new4':'item4'}]

space = []

for i in a_list:
    space.append(list(i.values())[0])

def add_to_list(new_item):
    space.append(new_item)

def del_from_list(old_item):
    space.remove(old_item)