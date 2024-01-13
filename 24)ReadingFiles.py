#Open external file
#modes:
'''
r=reading
a=append (read the file & write new line at the end of file)
w=writing
r+ = reading & writing


It is important that whenever you open file you must need to close that file
to read the file use the function readable()



employee_file=open("employee.txt","r")
print(employee_file.readable())
employee_file.close()


output:= True
because i make the file in r mode
if i change the file to w mode then it will give the output as False.

To print all the infromation from employee_file call function read.

employee_file=open("employee.txt","r")
print(employee_file.read())
employee_file.close()

output:=
Mamta-Master Trainer
Komal-Domain Trainer
Megha-Asst Trainer
Kashmira-Student
Moumi-Student

To read individual line we use the function readline()

employee_file=open("employee.txt","r")
print(employee_file.readline())
employee_file.close()

output:=
Mamta-Master Trainer



employee_file=open("employee.txt","r")
print(employee_file.readline())
print(employee_file.readline())
employee_file.close()

output:=

Mamta-Master Trainer

Komal-Domain Trainer


readlines()
It will read all the lines from employee_file & display them in array format.


employee_file=open("employee.txt","r")
print(employee_file.readlines())
employee_file.close()

output:=
['Mamta-Master Trainer\n', 'Komal-Domain Trainer\n', 'Megha-Asst Trainer\n', 'Kashmira-Student\n', 'Moumi-Student\n']


employee_file=open("employee.txt","r")
print(employee_file.readlines()[1])
employee_file.close()


output:=
Komal-Domain Trainer
'''

employee_file=open("employee.txt","r")
for employess in employee_file.readlines():
    print(employess)