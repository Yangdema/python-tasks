import random
secret_number = random.randint(1,100)
for _ in range(3):
    guess = int(input("take a guess:"))
if guess < secret_number:
    print("Too low!")
elif guess > secret_number:
    print("Too high!")
else:
    print("congratulations! you guessed the secret number correctly!")
     
