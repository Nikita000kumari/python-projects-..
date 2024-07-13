print("welcome to my computer quiz!")

playing = input("Do you want to play?")


if playing.lower() != "yes":
    quit()

print("okay! let 's play:)")
score = 0

answer = input("what does  cpu stand for ?  ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("what does GPU syand for  ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score =  score +1
    
else:
    print("Incorrect!")

answer = input("what does  RAM stand for ? ")
if answer.lower() == "random access memory ":
    print("correct!")
    score = score +1
else:
    print("Incorrect!")

answer = input("what does  PSU  stand for ?  ")
if answer.lower() == "power supply  unit":
    print("correct!")
    score = score +1
else:
    print("Incorrect!")

answer = input("who is the power house of the cell ")
if answer.lower() == " mitochondria":
    print("correct!")
    score = score +1
else:
    print("Incorrect!")

answer = input("what is the colour of the sky?  ")
if answer.lower() == "blue":
    print("correct!")
    score = score +1
else:
    print("Incorrect!")    

print("You got" + str(score) + "questions coreect!")


