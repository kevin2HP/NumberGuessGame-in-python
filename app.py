import random
guessesTaken = 0
myName = input('What is your name?')
number = random.randint(1,20)
print('Hello '+myName+' I am thinking of a number between 1 and 20 you have 6 tries to guess the number')

while guessesTaken <6:
    try:
        guess = int(input('Take a guess'))
    except ValueError:
        print('Numbers Only!')
        continue
    guessesTaken = guessesTaken +1

    if guess < number:
        print('Too Low')       
    elif guess > number:
        print('Too High')
    if guess == number:
        print(str(number)+'!  Good Job '+myName+' you guessed the number in '+str(guessesTaken) + ' tries!')