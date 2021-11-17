# A Quiz for children 

print("Welcome to my Game")

playing = input("Do you want to play a game? ")

if playing.lower() != "yes" :
    quit()

print("Okay Lets Play")
score = 0

answer = input("Which is the largest animal? ")
if answer.lower() == "blue whale":
    print("Correct")
    score += 1
else :
    print("Incorrect")

answer = input("In which direction does the sun rise? ")
if answer.lower() == "east":
    print("Correct")
    score += 1
else :
    print("Incorrect")

answer = input("Which is the smallest continent? ")
if answer.lower() == "australia":
    print("Correct")
    score += 1
else :
    print("Incorrect")

answer = input("Which is the coldest location in the earth? ")
if answer.lower() == "east antartica":
    print("Correct")
    score += 1
else :
    print("Incorrect")      

print("Your score is",str(score))    
print("Your percentage is " + str(score/4 * 100) + "%")
