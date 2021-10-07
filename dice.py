import random
import statistics
min = 1
max = 6
roll_again = "yes"

while roll_again == "yes" or roll_again == "y" or roll_again == "YES" or roll_again == "Y":
    print("Welcome to Klaud Dice...")
    print("The values of your dice: ")
    print (random.randint(min, max))
    print (random.randint(min, max))

    roll_again = input("Roll the dice again?")

#define the dice rolling function
