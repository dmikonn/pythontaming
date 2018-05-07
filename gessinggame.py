#This is the Guess-a-number game, inspired by the Automate Boring Stuff with Python course

import random

print("Hello. What is your name?")
name = input()

print("Well, "+name+", I'm thinking of the number between 1 and 20.")
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
        print("Take a guess.")

        while True:
            try:
                guess = int(input())
            except ValueError:
                print("Sorry, but this is not a nuber at all.")
                continue
                #Returns to the start of this loop
            else:
                #Nember was successfully parsed,
                #we're ready to exit the loop.
                break

        if guess < secretNumber:
                print("Your guess is too low.")
        elif guess > secretNumber and guess > 20:
                print("Your guess is too high. Way too high, it's over 20!")
        elif guess > secretNumber:
                print("Your guess is too high.")
        else:
                break

if guessesTaken == 1 and guess == secretNumber:
        print("Whoa, "+name+", that's awesome! You've guessed my number in the first guess!")
elif guess == secretNumber:
        print("Good job, "+name+"! You've guessed my number in "+str(guessesTaken)+" guesses!")
else:
        print("Nope. The number I was thinking was "+str(secretNumber)+".")

