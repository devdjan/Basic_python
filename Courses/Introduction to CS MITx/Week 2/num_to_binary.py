# Converting numbers to binary.
# Reason? I want to memorize it. How computer store numbers?
# Answer - in binary.
# Most difficult example,but you will understand(i joke):
# We have num 13. The correct way to conver it to binary, is to divide by two
# and catching the residuals of the results until the result is 0
# 13 / 2 = 6 and residual 1
# 6 / 2 = 3 and residual 0
# 3 / 2 = 1 and residual 1
# 1 / 2 = 0 and residual 1
# So read this from end we get - 1101
# How to convert to decimal?
# 1 * 2^3 + 1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 8 + 4 + 0 + 1 = 13
num = 13
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num // 2
if isNeg:
    result = '-' + result
print(result)