# Implementaiton of Euclid Algorithm
# We should find the greatest common divisor of two positive integers
# Som it means, find largest integer that divides each of them
# without remainder e.x. gcdIter( 3, 5) should be 1

def gcdIter(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
gcdIter(3, 5)

# Let's dig more deeply Look throug 6 - 13 line of code
# Firstly i define a function - Line 6
# Then i look where function is invoking - Line 13
# Then execute function, and we have Global frame, gcdIter, - Line 6
# where a equals 3, b equals 5
# Next, we go throug while loop, do until a will equal or not equal b (a != b) - Line 7
# Then subloop, if a > b: we substract b from a  - Line 8
# (a = a - b <=> a -= b) Line 9.
# If not( if a is greater then b), we go to else statement - Line 10
# And substract a from b  - Line 11
# (b = b - a <=> b -= a) Line 11.
# And do it, until a and b will equal the same
#
# I do this only for myself, if it helped you, you can star / write to me. Thanks

# a is smaller then b, so we do else statement: b - a <=> 5 - 3 = 2 | b = 2
# Then again we go through loop. Check a > b( 3 > 2), yes. Then 3 - 2 = 1 | a = 1
# Again go through loop a > b ? (1 > 2) - Not. Do else: b > a. Yes
# So, b = b - a <=> b = 2 - 1 | b = 1
# Check while condition a != b, no no no. A is equal to b, a = 1, and b = 1
# We go to return statement (line 12). And return value of a, It will return to us - 1 :)


def gcdIterative(x, y):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    while y != 0:
        (x, y) = (y, x % y)
    return x