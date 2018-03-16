# Bisection search
# We know that hte square root of x lies between 1 and x
# Rather than exahaustively trying things starting at, 1
# suppose instead we pick a number in the middle of this range
# 1 ----------------------- g ----------------------- X
# If we are lucky, this answer is close enough

# Then
# If not close enough, is quess too big or too small?
# if g**2 > x, then know g is too big but now search
# 1 ----------- new g ------------ g (-----------------------) X
# On each ctep we throw away what we don't need

# Ex. of square root

x = 25
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high + low) / 2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + 'low = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))