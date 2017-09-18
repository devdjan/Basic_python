import stdio
# Start doing task from books/ Added stdio library, to
# use some code from book;
n = 4
a = [] #initializing empty array
for i in range(n):
    a += [0.0] # addingone elem in the end of array




# Some fundamental operations
a = [1,2,3,4,5]
total = 0.0
for i in range(len(a)):
    total += a[i]
average = total / len(a)
print(average)

# Перебор элементов массива не обращаясь к индексам явно.
# Поместим имя массива после ключевого слова in в операторе for
total = 0.0
for v in a:
    total += v
average = total / len(a)
stdio.writeln(average)

# Псевдонимы и копии массива.
# Alias