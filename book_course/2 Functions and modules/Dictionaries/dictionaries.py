#Some tasks
# Lets define dictionary

cars_dict = {'ar324df' : 'Sam Smith', 'ai132dg' : 'Catherine Mcgrey', 'a2fd4ed' : 'Dict element'}
print(cars_dict['ar324df'])
# print(cars_dict['Dict element']) Return - Error
print('ar324df' in cars_dict)# - True
print('Sam Smith' in cars_dict) # False - why?
print('Sam' not in cars_dict) # True

# Let's add new key : value
cars_dict[101] = 'New value'
print(cars_dict[101]) # New value
print(cars_dict.get('ar324df')) # Returns value - Sam Smith/ If not exists
print(cars_dict.get('notexist')) # It will return None - not

# Let's iterate our dictionary in loop
dict = {'Kiryha' : 21, 'Sasha' : 19, 'Mikyta' : 22, 'Rob' : '25'}
for key in dict:
    print(key, end=' ')

print("\n")
# Russian: переберем, только явно будем исп. функцию keys - у словаря.
for key in dict.keys():
    print(key, end=' ')

print("\n") # Next line
for value in dict.values():
    print(value, end=' ')

print("\n") # Next line
# Now we are printing out <key> <value> Using dictionry function .items()
for keys, values in dict.items():
    print(keys,values, end="; ")


