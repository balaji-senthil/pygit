import random as rd

magicNumber = rd.randint(1, 51)
guess = int(input('Guess a number from 1 to 50\n '))
while 1:
    if guess != magicNumber:
        if guess < magicNumber:
            guess = int(input('Guess a higher number '))
        if guess > magicNumber:
            guess = int(input('Guess a lower number '))
    else:
        print('Hurray! Gotcha')
        break
