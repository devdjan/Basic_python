print('Please think of a number between 0 and 100')

# At the start the highest number should be = 100, lowest = 0
high = 100
low = 0
quessed = False

# While loop until it quesses correctly
while not quessed:
    # Bisection seacrch: quess the midpoint between our
    # current high and low values
    quess = (high + low) // 2
    print('Is your secret number ' + str(quess)+ '?')
    user_inp = input("Enter 'h' to indicate the quess is too high. Enter 'l' to indicate that quess is too low. Enter 'c' to indicate that I quessed correctly. ")

    if user_inp == 'c':
        quessed = True
    elif user_inp == 'h':
        high = quess
    elif user_inp == 'l':
        low = quess
    else:
        print('Surprise mothef*ca, you have entered a wrong input!')

print('Game over. Your secret number was: ' + str(quess))
