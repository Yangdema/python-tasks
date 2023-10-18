import random
secret_number = random.randint(1,100)
guess = 0
while guess != secret_number:
    guess = int(input("take a guess:"))
if guess < secret_number:
    print("Too low!")
elif guess > secret_number:
    print("Too high!")