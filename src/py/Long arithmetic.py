import random

def long_arithmetic():

    random_num = random.randint(1, 10**99)
    random_100_digit = random_num + 100**99
    while (len(str(random_100_digit))) < 100:
        random_100_digit += 100**99
    return random_100_digit


Number = int(input("Enter any number: "))
print(long_arithmetic()/Number)