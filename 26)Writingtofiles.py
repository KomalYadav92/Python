'''
a=append (read the file & write new line at the end of file)


employee_file=open("employee.txt","a")
employee_file.write("Sajid-student")
employee_file.close()

The output in console is blank but if yu go & see in employee.txt the new line is writed into that file
use \n for new line otherwise whenever you run the program the line will added at the end of last line only.


w= It will overwrite existing file & add new data from starting of file
you can also use w to create new file.
employee_file=open("employee.txt","w")
employee_file.write("\nBob-customer service")
employee_file.close()
'''
'''
employee_file=open("employee1.txt","w")
employee_file.write("\nBob-customer service")
employee_file.close()
'''

employee_file=open("index.html","w")
employee_file.write("<p>Hello Python!!!</p>")
employee_file.close()