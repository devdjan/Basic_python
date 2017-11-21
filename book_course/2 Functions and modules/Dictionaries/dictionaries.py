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
print(cars_dict.get('notexist')) # It will return None - not Error!

#