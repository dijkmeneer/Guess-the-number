import random
import time
import os
import sys

input("Welcome to guess the number! press enter to start.")

print("How many tries do you want? (5 is standard.)")

tries = int(input())

number = random.randint(0, 10)


while tries > 0:
    print("choose a number. (0-10)")
    guess = int(input())
    if guess == number:
        print("correct")
        
        time.sleep(1)
        
        answer = None
        
        while answer not in ("yes", "no"):
            answer = input("Do you want to play again? (yes/no) ")
            if answer == "yes":
                print("Okay")
                time.sleep(1)
                os.execl(sys.executable, sys.executable, * sys.argv)
                time.sleep(1)
            elif answer == "no":
                print("Bye!")
                time.sleep(1)
                sys.exit()
            else:
                print("Please type yes or no.")
    else:
        tries -= 1
        if tries > 1:
            print("Wrong! you still have " +str(tries)+ " tries.")
        elif tries == 0:
            print("You lost!")
        else:
            print("Wrong! you still have " +str(tries)+ " try.")


answer = None

while answer not in ("yes", "no"):
    answer = input("Do you want to play again? (yes/no) ")
    if answer == "yes":
        print("Okay")
        time.sleep(1)
        os.execl(sys.executable, sys.executable, * sys.argv)
        time.sleep(1)
    elif answer == "no":
        print("Bye!")
        time.sleep(1)
        sys.exit()
    else:
        print("Please type yes or no.")