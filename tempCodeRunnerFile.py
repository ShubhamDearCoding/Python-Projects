print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay let's play :)") 
score = 0

answer = input("What does WWW stand for? ")
if answer.lower() == "world wide web":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
# answer = "world wide Web"
# answer = input()
# print(answer.lower())
# print(answer.lower() == "world wide web")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memories":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")