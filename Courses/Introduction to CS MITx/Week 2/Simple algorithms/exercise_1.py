# Task 1
iteration = 0
count = 0
while iteration < 5:
    for letter in 'hello, world':
        count += 1
    print('Iteration ' + str(iteration) + '; count is: ' + str(count))
    iteration += 1
print('------------------------------------')

# What is the value of the variable count that
# is printed out (at the print statement) on iteration 0, 1, 2 ..?
# Try to quess without running this part of code

# ----------------------

# Task 2
iteration = 0
while iteration < 5:
    count = 0
    for letter in 'hello, world':
        count += 1
    print('Iteration ' + str(iteration) + '; count is: ' + str(count))
    iteration += 1
print('------------------------------------')
# What is the value of the variable count that
# is printed out (at the print statement) on iteration 0, 1, 2 ..?

# ----------------------

# Task 3
iteration = 0
while iteration < 5:
    count = 0
    for letter in 'hello, world':
        count += 1
        if iteration % 2 == 0:
            break
    print('Iteration ' + str(iteration) + '; count is: ' + str(count))
    iteration += 1
print('------------------------------------')

# ----------------------
