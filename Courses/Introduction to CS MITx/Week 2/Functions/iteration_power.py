def iterPower(base, exp):
    '''

    :param base: int or float
    :param exp: int >= 0
    :return: int or float, base^epx
    '''
    result = 1
    for i in range(exp):
        result *= base
        exp -= 1
    return result

print(iterPower(13, 1))