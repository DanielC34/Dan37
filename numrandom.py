import random

def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess a nummber between 1 and {x}: "))
        print(guess)
        if guess < random_num:
            print('Sorry too low, try again.')
        elif guess > random_num: 
            print('Sorry too high, try again.')
        
    print(f"Yay, congrats you guessed the right number {random_num} correctly!!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)??").lower()
        if feedback == "h":
            high = guess - 1 
        elif feedback == "l":
            low = guess + 1
            
    print(f"Yay, the computer guessed your number, {guess}, correctly!!")

# Execute both functions
guess(10)
computer_guess(10)
