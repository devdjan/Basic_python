strings = 'Data.Science.is.my passion '
result = []
for i in strings:
    if i.isalnum() or i.isspace():
        result.append(i)
    else:
        result.append(' ')

new_strings = "".join(result)
print(new_strings)
new_strings.split()
