# Python Functions Exercise

# 1 - Create a function in Python
# Write a program to create a function that takes two arguments,
# name and age, and print their value

#def funcao(name, age):
#    print(name, age)

#funcao("Carlos", 26)

# 2 - Create a function with variable length of arguments
# Write a program to create function func1() to accept a variable
# length of arguments and print their value

#def func1(*var):
#    for i in var:
#        print(i)

#func1(20, 40, 60)
#func1(80,100)

# 3 - Return multiple values from a function
# Write a program to create function calculation() such that it
# can accept two variables and calculate addition and subtraction.
# Also, it must return both addition and subtraction in a single
# return call

#def calculation(a,b):
#    c=a+b
#    d=a-b
#    return c, d
#res = calculation(40, 10)
#print(res)

# 4 - Create a function with default argument
# Write a program to create a function show_employee() using
# the following conditions.
# It should accept the employee's name and salary and display both
# If the salary is missing in the function call then assign default value 9k to salary

#def show_employee(name, sal=9000):
#    print('Name:', name,'; Salary:', sal)

#show_employee('Ben', 12000)
#show_employee('Jessa')

# 5 - Create an inner function to calculate the addition in
# the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will
# calculate the addition of a and b
# At least, an outer function will add 5 into addition and return it

#def fun1(a,b):
#    c = a
#    d = b
#    def fun2(c, d):
#        return c+d

#    add = fun2(c, d)
#    return add + 5

#result = fun1(5,10)
#print(result)

# 6 - Create a recursive function
# Write a program to create a recursive function to calculate
# the sum of numbers from 0 to 10
# A recursive function is a function that calls itself again and again

#def recursive(num):
#    if num:
#        return num+recursive(num-1)
#    else:
#        return 0
#res = recursive(10)
#print(res)

# 7 - Assign a different name to function and call it through
# the new name

#def display_student(name, age):
#    print(name, age)

#Alternative (need to change previous function)
#def show_student(name, age):
#        display_student(name, age)
#        print(name, age)

#Right way
#show_student = display_student

#display_student("Marlon", 28)
#show_student("Emma", 26)

# 8 - Generate a Python list of all the even numbers between
# 4 to 30

#def lista():
#    for i in list(range(4,31,2)):
#        print(i)
#lista()

# 9 - Find the largest item from a given list

#x = [4, 6, 8, 24, 12, 2]
#print(max(x))