import random

fruits = ['banana','apple','pear','mango','grapes','orange','watermelon','peach','apricot','strawberry']
choice = random.choice(fruits)
# print(choice)

print("The hungry monkey wants to eat some fruits. Guess which fruit did the monkey choose:")
print('You have 5 tries to guess the fruit')

count = 0
while (count != 5):

    guess = input("Enter name of a fruit: ")
    if guess.lower()== choice:
        print("Well done. Your guess is correct!")
        break
    else:
        print("Try Again.")
    count += 1
    print('Tries left: ',(5 - count))
    if count == 3:
        print('Hint! The name of the fruit starts with', choice[0])

print('The monkey chose ', choice)