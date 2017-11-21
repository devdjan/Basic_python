new_set = set()
new_set = {'Machine learning', 'Data scince', 'Business intelligense',}
print(new_set)
#{'Data scince', 'Machine learning', 'Business intelligense'}
new_set.add('Agriculture')
print(new_set)
#{'Data scince', 'Agriculture', 'Machine learning', 'Business intelligense'}
# Let's remove agriculture

new_set.remove('Agriculture') # If you write wrong the name of the removal element/ It will return Error
print(new_set)
# Without agriculture

new_set.discard('business') # Does not returns errors, even when i write wrong element's name
print(new_set) # Nothing

# So let print our set - to console. We will look how it is printing out
for x in new_set:
    print(x) # every time console shows us different ways of how it print's out.

new_set.clear()
print(new_set) # must be empty set()