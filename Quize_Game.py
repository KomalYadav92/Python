print("WELCOME TO THE QUIZ GAME!!!")

playing=input("Would you want to play???? ")
play=playing.lower()
score=0
if play=="yes":
    print("Okay!! Lets Play")
elif play=="no":
    print("Goodbye")
    quit()
else:
    print("Sorry, I didn't understand")
    quit()


answer=input("What is full form of CPU?? ")
if answer.lower()=="central processing unit":
    print("Correct!!")
    score=score+1;
else:
    print("Incorrect!!")

answer=input("What does GPU stands for??? ")
if answer.lower()=="graphics processing unit":
    print("Correct!!")
    score = score + 1;
else:
    print("Incorrect!!")

answer=input("What does RAM stands for??? ")
if answer.lower()=="random access memory":
    print("Correct!!")
    score = score + 1;
else:
    print("Incorrect!!")

answer=input("What does PSU stands for??? ")
if answer.lower()=="power supply unit":
    print("Correct!!")
    score = score + 1;
else:
    print("Incorrect!!")

print("Your got "+str(score)+" questions correct!!!!")
print("You got "+str((score/4)*100) +" %.")