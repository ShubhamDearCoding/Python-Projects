youtuber = "shubham" 
print(f"subscribe to {youtuber}")


adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"computer programming is so {adj}! it always makes me excited because \
i love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)

import random 

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('sorry,guess again. too low. ')
        elif guess > random_number:
            print('sorry,guess again. too high. ')

    print(f'Yay, congrats. you have guessed the number {random_number} correctly!! ')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high bc low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! the computer guessed your number, {guess}, correctly!')

computer_guess(10)


