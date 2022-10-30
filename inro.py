import random


number = random.randint(1,20)

print("You have 5 tries to guess the number. Let's Play!")

count = 0
while (count != 5):

    guess = int(input("Input a number: "))
    if guess == number:
        print("Your guess is correct")
        break
    elif guess > number:
        print("Guess is big")
    else:
        print("Guess is smaller")
    count += 1
    print('Tries left: ',(5 - count))

print('The random number is', number)


