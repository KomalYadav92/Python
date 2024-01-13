lucky_nos=[3,5,8,89,16]
friends=["Rakhi","Ekta","Prerana","megha","Rahul"]
print(friends)
'''
#to extend the list
friends.extend(lucky_nos)
print(friends)
'''


#to append
friends.append("Priyanka")
print(friends)

#to insert(index , value)  the value is inserted in that possition & all other get pushed to next positions
friends.insert(1,"komal")
print(friends)

#to remove value form list
friends.remove("Rakhi")
print(friends)
'''
# to empty list
friends.clear();
print(friends)
'''
# to see the index of value
print(friends.index("komal"))

# to couut how many times the value is repeated
friends=["Rakhi","Ekta","Ekta","Prerana","megha","Rahul"]
print(friends.count("Ekta"))
friends.sort()
#to sort the list
print(friends)
lucky_nos.sort()
print(lucky_nos)
#to reverse the list
lucky_nos.reverse()
print(lucky_nos)

#to copy the list
friends2=friends.copy()
print(friends2)

SS