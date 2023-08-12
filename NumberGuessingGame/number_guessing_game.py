''' Number Guessing Game'''

import random
import math

print("\tWelcome to the number guessing game!!!")
lb = int(input("\tEnter the lower bound: "))
ub = int(input("\tEnter the upper bound: "))

x = random.randint(lb, ub)

print("\n\tYou have only got", round(math.log(ub-lb+1,2)), "chances to find the integer!!!")

count = 0

while count < math.log(ub-lb+1,2):
    count += 1

    guess = int(input(f"Enter your {count} guess: "))

    if x==guess and count == 1:
        print("\tCongratulations you did it in", count, "try")
        break
    elif x==guess:
        print("\tCongratulations you did it in", count, "tries")
        break
    elif x > guess:
        print("\tThe number that you guessed is too low!!!")
    elif x < guess:
        print("\tThe number that you guessed is too high!!!")

if count > math.log(ub-lb+1,2):
    print(f"\n\tThe number is: {x}")
    print("\tBetter Luck Next Time :))")