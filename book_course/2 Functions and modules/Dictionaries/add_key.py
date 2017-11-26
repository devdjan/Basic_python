# How i solve task with additional help
d = {1: 'Kiryha', 2:'Kirusha'}
def update_dictionary(d, key, value):
        # put your python code here
        if key in d:
            d[key].append(value)
        elif 2 * key in d:
            d[2 * key].append(value)
        else:
            d[2 * key] = []
            d[2 * key] = [value]


update_dictionary(d, 3, 'Sasha')
print(d)

# The another one, from forum using "setdefault"
d = {1: 'Kiryha', 2:'Kirusha'}
def update_dictionary(d, key, value):
    if key in d:
        d.setdefault(2 * key,[]).append(value)
    else:
        d[key]+=[value]

print(d)

# Best variant 2.45
def update_dictionary(d, key, value):
    key <<= key not in d
    d.setdeafult(key, []).append(value)

# P.S. еще нужно разобрать код, пару раз хотябы