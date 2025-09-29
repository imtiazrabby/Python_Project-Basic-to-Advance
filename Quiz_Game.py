print("Welcome to my Computer  Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()


print("Okay! Let's Play :) ")
score = 0

answer = input ("What does CPU Stand for? ")

if answer.lower() == "central processing unit" :
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input ("What does GPU Stand for? ")

if answer.lower() == "graphics processing unit" :
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")




answer = input ("What does RAM Stand for? ")

if answer.lower() == "random access memory" :
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")




answer = input ("What does ROM Stand for? ")

if answer.lower() == "read only memory" :
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")



answer = input ("What does PSU Stand for? ")

if answer.lower() == "power supply" :
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")




answer = input ("What does CSE Stand for? ")

if answer.lower() == "computer science and engineering" :
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")



answer = input ("What does ICT Stand for? ")

if answer.lower() == "information and communication technology" :
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " question correct. ")  
print("You got " + str((score/7)*100) + " %.")  