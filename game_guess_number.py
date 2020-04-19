#Guess the Number
import random

guessTaken = 0
print("Hello! What is your name?")
myName = str(input())

number = random.randint(1, 20)
print('Well', myName, ', I am thinking of a number btw 1 and 20.')

while guessTaken < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessTaken = guessTaken + 1
    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break

if guess == number:
    guessTaken = str(guessTaken)
    print('Good job,' + myName + '! you guessed my number in ' + guessTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)

