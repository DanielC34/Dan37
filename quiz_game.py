print("Welcome to my quiz!!")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play: ")
score = 0

answer = input("What does WHO stand for? ")
if answer.lower() == "world health organisation":
    print('That is correct!!')
    score += 1
else:
    print("Incorrect answer!!")
    
answer = input("What is the capital of Croatia? ")
if answer.lower() == "zagreb":
    print('That is correct!!')
    score += 1
else:
    print("Incorrect answer!!")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print('That is correct!!')
    score += 1
else:
    print("Incorrect answer!!")
    
    
answer = input("Which country is the city Stockholm found in? ")
if answer.lower() == "sweden":
    print('That is correct!!')
    score += 1
else:
    print("Incorrect answer!!")
    
    print("You got " + str(score) + " of the 4 questions correct!")
    print("You got " + str((score / 4) * 100) + "%.")