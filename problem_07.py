# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))
# conversion factor
con_factor = 0.621371
# calculate miles
miles = kilometers * con_factor
# Print Result
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))