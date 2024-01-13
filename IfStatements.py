'''is_male=True

if is_male:
    print("You are a male")

is_male = False

if is_male:
    print("You are a male")


#if   else

is_male = True

if is_male:
    print("You are a male")
else:
    print("You are not male")

#or operator

is_male = True
is_tall=True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall or both")

# and operator

is_male = True
is_tall=True

if is_male and is_tall:
    print("You are a male & tall")
else:
    print("You are neither male nor tall ")

'''

#4 conditions

is_male = False
is_tall=True

if is_male and is_tall:
    print("You are a male & tall")
elif is_male and not(is_tall):
    print("You are a male but not tall")
elif not(is_male) and is_tall:
    print("You are not a male")
else:
    print("You are neither male nor tall ")
