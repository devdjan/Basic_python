# Let's split problem
# firstly it should return us base * recursion(base, epx-1)
# while exp will equal to 1
# Then we write if statement
# If exp == 1, obviously we will return base (e.x. (2,0) ==> 2
# if exp == 0 return 1
# else return base * recursion(base, epx-1)
#

def recurPower(base, exp):
    '''

    :param base: int or float
    :param exp: int >=0
    :return: int of dloat, base^exp
    '''
    if exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        return base*(recurPower(base, exp-1))

print(recurPower(3,4))