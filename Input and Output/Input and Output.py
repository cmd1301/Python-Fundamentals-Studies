# Input and Output Exercises

# 1 -Accept numbers from a user: write a program to accept two numbers
# from the user and calculate multiplication

#input
print('Insert two numbers: ')
num1 = input('First number: ')
num2 = input('Second number: ')

#multiplication
num1_int = int(num1)
num2_int = int(num2)
def multip(arg1, arg2):
    return (arg1*arg2)
print(multip(num1_int,num2_int))

# 2 - Display three string "Name", "Is, "James" as "Name**Is**James"
# Use the print() function to format the given words in the mentioned
# format. Display the ** separator between each string.

str1 = 'Name'
str2 = 'Is'
str3 = 'James'

x = (str1+"**"+str2+"**"+str3)
#other form
#print(str1, str2, str3, sep='**')
print(x)

# 3 - Convert decimal number to octal using print() outpur formatting
#def dectoOct(decimal):
   # if (decimal > 0):
    #    dectoOct((int)(decimal / 8))
     #   print(decimal % 8, end='')


#decimal = int(input("Enter a decimal number \n"))
#print("Octal: ", end='')
#dectoOct(decimal);

#num=8
#print('%o' % num) %o é para octal


# 4 - Display float number with 2 decimal places using print()

num4 = 458.541215
print('%.2f' % num4)

# 5 - Accept a list of 5 float numbers as an input from the user
#numbers = []
#while len(numbers) < 5:
 #   i = float(input('number: '))
  #  numbers.append(i)
#print(numbers)

# 6 - Write all content of a given file into a new file by skipping
# line number 5
counter = 0

with open('test.txt', 'r') as arq1, open('new_file.txt', 'w') as arq2:
    for line in arq1:
        if counter == 4:
            counter += 1
            continue
        else:
            arq2.write(line)
        counter+=1

print(counter)
arq2.close()
arq2 = open('new_file.txt', 'r')
print(arq2.read())

# 7 - Accept any three string from one input() call
# Write a program to take three names as input from a user in the
# single input() function call.

#name, middle_name, sur_name = input('Enter your name, middle name and sur name separated by space ').split()
#print('Full name: ', name, middle_name, sur_name)

# 8 - Format variables using a string.format() method
# Write a program to use string.formar() method to format the following
# three variables as per the expected output.

#totalMoney = 1000
#quantity = 3
#price = 450

#print('I have {0} dollars so I can buy {1} football for {2} dollars.'.format(totalMoney, quantity, price))

# 9 - Check file is empty or not
# Write a program to check if the given file is empty or not

import os

size = os.stat('empty_file.txt').st_size
if size == 0:
    print('file is empty')
else:
    print('file loaded')

# 10 - Read line number 4 from the following the file test.txt

arquivo = open('test.txt', 'r')
line = arquivo.readlines()[4]
print(line)
