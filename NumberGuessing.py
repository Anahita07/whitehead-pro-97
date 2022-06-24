from mimetypes import guess_type
import random
print ("number guessing game")
number = random.randint(1,9)
chances = 5
print("guess a number between 1 and 9 ")

while chances < 5:
    guess = int(input("enter you guess: "))
     
    if guess == number :
        print("CONGRATULATIONS!!! you won!!")
        break

    elif guess < number :
        print("your guess was too low :( guess a number higher than"  + guess)

    else: 
        print("your number was too high :( guess a number lower than" +  guess)

chances  = chances - 1

if not chances < 5:
    print("YOU LOSE!!! the number is: " + number)


