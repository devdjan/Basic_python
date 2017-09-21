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
# Cheto ne vishlo(
# Я бы взял [-1] массива в с помощью функции по аналогии с append, только
# наоборот, записал бы в другой список

#----------------------------------------------------------
#Write a Python program to get the length in bytes of one array item in the internal representation.
# array = [0,1,34,-1,3]
# array.itemsize
# print(array)

#----------------------------------------------------------
# in bytes
def byte_size(byte):
    return len(byte.encode('utf-8'))
print(byte_size)

#----------------------------------------------------------
# Stack overflow solution using sys library
import sys
array_test = [1,2,3,-1]
sys.getsizeof[1,23,4]
print(array_test)

#----------------------------------------------------------
# Write a Python program to append items from inerrable to the end of the array.
test = [1,2,3,4,5,6]
# Может воспользоваться методом extended
def append_items(test):
    return append_items().extend

#----------------------------------------------------------
# Convert an array to an array of machine values and return the bytes representation
