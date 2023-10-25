import random

random_number = random.randint(1, 100)
guess = int(input("Guess the number: "))
count = 0
while guess != random_number:

    if guess > random_number:
        print("Too high: ")
        count += 1
    elif guess < random_number:
        print("too low: ")
        count += 1
    guess = int(input("Guess the number: "))
print("You found the number in ", count, "times")

list_numbers = list(range(1, 100))




