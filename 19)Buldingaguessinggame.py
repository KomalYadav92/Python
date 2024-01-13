secrete_world="shivansh"
guess=""
a=1


while a<=3:
    guess = input("Enter your guess: ")
    if guess != secrete_world and a<=3:
        print("You loss"+ str(a) + " chance to guess the secret" )
        a = a + 1
    elif guess == secrete_world and a<=3:
        print("Congratulations! You win!!!")
    else:
        print("You loss your chance to guess the secret")




