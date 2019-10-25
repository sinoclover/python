import os
import random

secret = random.randint(1, 100)
guess = 0
tries = 0

print("AHOY! I'm the Dread Priate Roberts, and I have a secret!")
print("It's a number from 1 to 99, I'll give you 6 tries")

while guess != secret and tries < 6:
    guess = int(input("What's your guess? "))
    # 如果不加int()类型转换会出现错误，'<' not supported between instances of 'str' and 'int'
    if guess < secret:
        print("Too low!, ye scurvy dog!")
    elif guess > secret:
        print("Too high, landlubber!")
    tries += 1

if guess == secret:
    print("Avast! Ye got it! Found my secret, ye did!")
else:
    print("No more guesses! Better luck next time, matey!")
    print('The secret number was', secret)

os.system('pause')