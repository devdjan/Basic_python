import stdio
# Start doing task from books/ Added stdio library, to
# use some code from book;
n = 4
a = [] #initializing empty array
for i in range(n):
    a += [0.0] # addingone elem in the end of array

# Some fundamental operations
# a = [1,2,3,4,5]
# total = 0.0
# for i in range(len(a)):
#     total += a
# average = total / len(a)
# print(average)

# Перебор элементов массива не обращаясь к индексам явно.
# Поместим имя массива после ключевого слова in в операторе for
total = 0.0
for v in a:
    total += v
average = total / len(a)
stdio.writeln(average)

#----------------------------------------------------------
#Write a Python program to create an array of 5 integers
# and display the array items.
# Access individual element through indexes
# a = [1,4,5,6,7]
# for i in range(a):
#     print(i)
#     print(i[-1])
array = [1,4,5,6,7]
for i in array:
    print(i)
    print(array[1]) # five times 4 4 4 4 4

#----------------------------------------------------------
#Write a Python program to append a new item to the end of the array.
array = [1,2,3,4,5,0]
array.append(6)
print(array)

#----------------------------------------------------------
#Write a Python program to reverse the order of the items in the array.
#Maybe using .reverse

array = [1,2,3,6,7,8,0,-1]
array.reverse()
print(array)

#Tomorrov i will try to write some function of "reverse"