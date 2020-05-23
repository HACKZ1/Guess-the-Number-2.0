import random
import time

start = input("Want to guess a number?")

if start in [" yes", " Yes"]:
    print("I am thinking of a number 1-100 you have 3 chances to guess it")
else:
    print("Ok play with me later!")
    exit()

number = random.randint(1,100)
number2 = str(number)

guess1 = input("What is your first guess?")
guess11 = int(guess1)

if guess11 == number:
    print("No way you got it first try!")
    exit()

if guess11 > number:
    print("My number is lower that that.")

if guess11 < number:
    print("My number is higher than that.")

guess2 = input("Ok, what is your second guess?")
guess21 = int(guess2)

if guess21 == number:
    print("Nice you got it in two tries")
    exit()

if guess21 > number:
    print("My number is lower that that.")

if guess21 < number:
    print("My number is higher than that.")

print("This is your last guess I will let you think a little")

time.sleep(5)

guess3 = input("What is your final guess?")
guess31 = int(guess3)

if guess31 == number:
    print("Phew you got it on the last try!")
    exit()

if guess31 > number:
    print("My number was lower than that.")

if guess31 < number:
    print("My number was higher than that.")

print("Oh no you lost my number was " + number2)
exit()

