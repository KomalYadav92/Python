import random
#randrange not include stop number
#randint will include stop number
# randrange(11)  0 to 10
# randint(11) 1 to 11

top_of_range=input("Enter the top of range: ");
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range <= 0 :
        print("Plz enter a valid number next time!!!")
        quit()
else:
    print("Invalid Input")
    quit()

r= random.randrange(0,top_of_range)
print(r)
a=1
while a<=5:
    answer=input("Plz enter your guess")
    if r==int(answer):
        print("Congratulations you guessed my number!")
        quit()
    else:
        print("Sorry you are worng, plz try again")
        a+=1

print("sry ..you reached maximum limits of guess")
quit()
