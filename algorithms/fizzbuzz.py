for num in range(1,100):
    if num % 3 == 0:
        print('Fizz')
    if num % 5 == 0:
        print('Buzz')
    if num % 15 == 0:
        print('FizzBuzz')
    else:
        print(num)