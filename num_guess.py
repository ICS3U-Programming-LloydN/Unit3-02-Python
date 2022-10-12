#!/usr/bin/env python3
 
# Created by: Lloyd Najac
# Created on: Oct 2022
# This program picks a random number and you have to guess
import random
number = random.randint(1, 10)
 
number_of_guesses = 0
print('okay! I am Guessing a number between 1 and 10:')
 
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is incorrect')
    if guess > number:
        print('Your guess is incorrect')
    if guess == number:
        break
if guess == number:
    print('You guessed the number')
else:
    print('You did not guess the number, The number was ' + str(number))
 
