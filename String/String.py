# Exercícios Strings

# 1A - Create a string made of the first, middle and last character

#str1 = "James"
#str2 = str1[0:5:2]
#print(str2)

# 1B - Create a string made of the middle three characters
#import re
#str1 = "JhonDipPeta"
#str2 = "JaSonAy"

#def separar(x):
#    sep = re.split('(?=[A-Z])',x)
#    sep2 = sep[2]
#    return print(sep2)

#separar(str1)
#separar(str2)

# 2 - Append new string in the middle of a given string
# Given two strings s1 and s2, write a program to create a new string
# s3 by appending s2 in the middle of s1

#s1 = "Ault"
#s2 = "Kelly"

#def separar(x,y):
#    st1 = x[0:2]
#    st2 = x[2:4]
#    st3 = st1+y+st2
#    print(st3)
#separar(s1,s2)

# 3 - Create a new string made of the first, middle, and last characters
# of each input string

#s1 = "Carlos"
#s2 = "Dias"

#def fl(x,y):
#    fl1 = x[0]
#    fl2 = y[0]
#    print(fl1,fl2)
#    def ml(x,y):
#        ml1 = int(len(x)/2)
#        midl1 = x[ml1]
#        ml2 = int(len(y)/2)
#        midl2 = y[ml2]
#        print(midl1,midl2)
#        def ll(x,y):
#            ll1 = int(len(x))
#            lastl1 = x[(ll1)-1]
#            ll2 = int(len(y))
#            lastl2 = y[(ll2)-1]
#            print(lastl1,lastl2)
#            def alltogether(x,y):
#                all = fl1+fl2+midl1+midl2+lastl1+lastl2
#                print(all)
#            alltogether(x,y)
#        ll(x,y)
#    ml(x,y)

#fl(s1,s2)

# 4 - Arrange string characters such that lowercase letters should come
# first
#str1 = 'PyNaTive'
#lower = []
#upper = []

#for char in str1:
#    if char.islower():
#        lower.append(char)
#    else:
#        upper.append(char)

#res = ''.join(lower + upper)
#print(res)

# 5 - Count all letters, digits, and special symbols from a given string

#str1 = "P@#yn26at^&i5ve"

#chars = 0
#digits = 0
#symbol = 0

#for char in str1:
#    if char.isalpha():
#        chars += 1
#    elif char.isdigit():
#        digits += 1
#    else:
#        symbol += 1
#print(chars, digits, symbol)

# 6 - Create a mixed String using the following rules:
# Given two strins, s1 and s2, write a program to create a new string
# s3 made of the first char of s1, then the last char of s2. Next, the
# second char of s1 and second last char of s2, and so on. Any leftover
# chars go at the end of the result.

#s1 = "Abc"
#s2 = "Xyz"

#def fl(x,y):
#    fl1 = x[0]
#    fl2 = y[-1]
#    print(fl1,fl2)
#    def ml(x,y):
#        ml1 = x[1]
#        ml2 = y[-2]
#        print(ml1,ml2)
#        def ll(x,y):
#            ll1 = x[2]
#            ll2 = y[0]
#            print(ll1,ll2)
#            def alltogether(x,y):
#                all = fl1+fl2+ml1+ml2+ll1+ll2
#                print(all)
#            alltogether(x,y)
#        ll(x,y)
#    ml(x,y)

#fl(s1,s2)

# 7 - String characters balance Test
# Write a program to check if two strings are balanced. For example,
# strings s1 and s2 are balanced if all the characters in the s1 are
# present in s2. The character's position doesn't matter.

#Case 1
#s1 = "Yn"
#s2 = "PYnative"

#letters1 = []

#for char in s1:
#    letters1.append(char)
#print(letters1)
#for i in letters1:
#    if i in s2:
#        res = True
#    else:
#        res = False

#print(res)

# Case 2
#s3 = "Ynf"
#s4 = "PYnative"

#letters2 = []

#for char2 in s3:
#    letters2.append(char2)
#print(letters2)
#for j in letters2:
#    if j in s4:
#        res2 = True
#    else:
#        res2 = False

#print(res2)
#Desse jeito que fiz não importa a ordem das letras

# 8 - Find all occurrences of a substring in a given string by
# ignoring the case
# Write a program to find all occurrences of "USA" in a given string
# ignoring the case

#str1 = "Welcome to USA. usa isn't awesome"
#lowerstr = str1.lower()
#print(lowerstr)
#res = lowerstr.count("usa")
#print(res)

# 9 - Calculate the sum and average of the digits present in a string
# Given a str1, write a program to return the sum and average of the
# digits that appear in the string, ignoring all other characters.

#str1 = "PYnative29@#8496"
#num = []
#numint = []
#for i in str1:
#    if i.isdigit():
#        num.append(i)
#for j in range(0, len(num)):
#    num[j] = int(num[j])
#print(num)

#suma = sum(num)
#average = suma/len(num)

#print(suma, average)

# 10 - Write a program to count occurrences of all characters within
# a string

#str1 = 'apple'
#contadic = dict()
#for i in str1:
#    conta = str1.count(i)
#    contadic[i] = conta
#print('Result:', contadic)

# 11 - Reverse a given string

#str1 = "PYnative"
#rev = str1[::-1]
#print(rev)

#str2 = ''.join(reversed(str1))
#print(str2)

# 12 - Find the last position of a given substring
# Write a program to find the last position of a substring
# "Emma" in a given string

#str1 = "Emma is a data scientist who knows Python. Emma works at google."
#str2 = 'Emma'

#print(str1.index(str2, 1))
#rfind() last occurrence of the specified value

# 13 - Split a strin on hyphens
# Write a program to split a given string on hyphens and display each
# substring

#str1 = "Emma-isis-a-data-scientist"

#str1_split = str1.split('-')
#print(str1_split)

#for substring in str1_split:
#    print(substring)

# 14 - Remove empty strings from a list of strings

#str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

#new_str = [s for s in str_list if s != "" and s != None]
#print(new_str)

# 15 - Remove special symbols/punctuation from a string

#str1 = "/*Jon is @developer & musician"

#x = ""
#y = ""
#z = "/*@"

#clean_str1 = str1.maketrans(x, y, z)
#print(str1.translate(clean_str1))

# 16 - Remove all characters from a string except integers

#str1 = 'I am 25 years and 10 months old'

#res = ''.join([i for i in str1 if i.isnumeric()])
#print(res)

# 17 - Find words with both alphabets and numbers
# Write a program to find words with both alphabeats and numbers from
# an input string

#str1 = "Emma25 is Data scientist50 and AI Expert"

#sep = str1.split()
#print(sep)

#res = []

#for i in sep:
#    if any(char.isalpha() for char in i) and any(char.isdigit() for char in i):
#        res.append(i)
#for i in res:
#    print(i)

# 18 - Replace each special symbol with # in the following string
#import string

#str1 = '/*Jon is @developer & musician!!'
#replacer = "#"

#for char in string.punctuation:
#    str1 = str1.replace(char, replacer)
#print(str1)

pip install pandas