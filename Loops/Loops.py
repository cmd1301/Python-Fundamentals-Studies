# Loops Exercises
# 1 - Print first 10 natural numbers using while loop

#i = 1
#while i <= 10:
#    print(i)
#    i +=1

# 2 - Print the following pattern
# Write a program to print the following number patern |\
# using loop

#rows = 5
#for i in range(1, rows+1):
#    for j in range(1, i+1):
#        print(j, end='')
#    print ('')

# 3 - Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate
# the sum of all numbers from 1 to a given number

#number = int(input('give the number:'))
#suma = 0
#for i in range(1, number+1, 1):
#    suma +=i
#print(suma, end='')

# 4 - Write a program to print multiplication table of a given number

#num = int(input('giv numbr: '))
#rows = 10
#for i in range(1, rows+1, 1):
#    m = num*i
#    print(m, end='\n')

# 5 - Display numbers from a list using loop
# Write a program to display only those numbers from a list
# that satisfy the following conditions:
# The number must be divisible by 5
# If the number is greater than 150, skip it and move to the next number
# If the number is greater than 500, then stop the loop

#numbers = [12, 75, 150, 180, 145, 525, 50]
#for i in numbers:
#    if i>500:
#        break
#    elif i>150:
#        continue
#    elif i%5==0:
#        print(i)

# 6 - Count the total number of digits in a number
# Write a program to count the total number of digits in a
# number using a while loop

#number = 75869
#count = 0
#while number!=0:
#    number = number//10
#    count +=1
#print(count)

# Ele viu quantas vezes consegui dividir por 10 até chegar a
# um número 0,n e como só está sendo visto num int, assume-se
# que number = 0 e assim finaliza dada a condição !=0.

# 7 - Print the following pattern
# Write a program to use for loop to print the following reverse
# number pattern

#rows = 5
#for i in range(0, rows+1):
#    for j in range(rows-i,0,-1):
#        print(j, end='')
#    print ('')

# 8 - Print list in reverse order using a loop

#list1 = [10, 20, 30, 40, 50]
#size = len(list1) -1
#for i in range(size, -1, -1):
#    print(list1[i])

# 9 - Display numbers from -10 to -1 using for loop

#for i in range(10, 0, -1):
#    print(-i)

# 10 - Use else block to display a message "Done" after
# successful execution of for loop

#for i in range(5):
#    print(i)
#else:
#    print('Done!')

# 11 - Write a program to display all prime numbers within a
# range

#start = 25
#end = 50

#for i in range(25, 51):
#    if i%2==0 or i%3==0 or i%5==0 or i%7==0:
#        continue
#    else:
#        print(i)

#for i in range(25, 51):
#    for j in range(2,i):
#        if (i%j)==0:
#            break
#    else:
#        print(i)

# 12 - Display Fibonacci series up to 10 terms
# The Fibonacci Sequence is a series of numbers. The next
# number is found by adding up the two numbers before it.
# The first two numbers are 0 and 1

#p = 0
#a = 1
#for i in range(10):
#    print(p, end=' ')
#    res = p + a
#    p=a
#    a=res

# 13 - Find the factorial of a given number
# Write a program to use the loop to find the factorial of
# a given number

#num = int(input('Number:'))
#fac = 1
#for i in range(1, num+1):
#    fac = fac*i
#print(fac)

# 14 - Reverse a given integer number

#number = int(input('Num:'))
#rev_number = 0

#while (number>0):
#    remainder = number%10
#    rev_number = (rev_number*10) + remainder
#    number = number//10
#print(rev_number)

# 15 - Use a loop to display elements from a given list present
# at odd index positions

#my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#for i in my_list[1::2]: #2 a 2 step
#    print(i, end=' ')

# 16 - Calculate the cube of all numbers from 1 to a given
# number

#for i in range(1, int(input('Number:'))+1):
#    cube = i**3
#    print('Current Number is:', i, 'and the cube is:', cube)

# 17 - Find the sum of the series upto n terms
# Write a program to calculate the sum of series up to n term.
# For example, if n=5 the series will become 2 + 22 + 222 +
# + 2222 + 22222 = 24690

#n = 5
#s = 2
#sum = 0

#for i in range (0, n):
#    print(s, end="+")
#    sum += s
#    s = s*10+2
#print('\n', sum)

# 18 - Print the flag pattern |>

#for i in range(0, 5):
#    for j in range(0, i+1):
#        print('*', end=' ')
#    print('\r')
#for k in range(5,0,-1):
#    for l in range(0, k-1):
#        print('*', end=' ')
#    print('\r')