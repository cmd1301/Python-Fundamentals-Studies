# Enter Python code here and hit the Run button.

# 3

str = input("Digita ae: ")

print(str[0::2])

# 4

print(str[4::])

# 5

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def compararX (x):
    if x[0] == x[4]:
        return True
    else:
        return False
def compararY (y):
    if y[0] == y[4]:
        return True
    else:
        return False

print(compararX(numbers_x))
print(compararY(numbers_y))

# 6
lista = [10, 20, 33, 46, 55]
print('Given list is:', lista)

div5 = []

for i in lista:
    if i%5==0:
        div5.append(i)

print('Divisible by 5:', div5)

# 7

str_x = "Emma is good developer. Emma is a writer"
str_count = str_x.count('Emma')
print('Emma appeared', str_count, 'times')

# 8

for num in range(10):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")

# 9
#ask number
num = input('Manda pa nois:')
print(num)

#make reverse
num_rev = num[::-1]
print(num_rev)

#make int
num_int = int(num)
numrev_int = int(num_rev)

#if number = reverse == palindrome
if num_int == numrev_int:
    print('Palindromes')
else:
    print('not this time bro')

#########alternative version########
#através de função
#inserir número
numf = input('Manda pa nois:')
print(numf)

def reverse(x):
    return x[::-1]

numf_rev = reverse(numf)
print(numf_rev)

#make i(n)t
numf_int = int(numf)
numfrev_int = int(numf_rev)

def comparasion(arg1, arg2):
    if arg1 == arg2:
        return "PalindromeF"
    else:
        return "Not PalindromeF"

print(comparasion(numf_int, numfrev_int))

# 10

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

list3 = []

for i in list1:
    if i%2!=0:
        list3.append(i)

for i in list2:
    if i%2==0:
        list3.append(i)

print(list3)

# 11

#make the input
numero = input('fala bb:')
print(numero)

#reverse
numero_rev = numero[::-1]
print(numero_rev)

#numero_separate = int(numero_rev)//10
#print(numero_separate)
#nao consegui adicionar o espaçamento

# 12

#input
value_str = input('Insert income value:')
value = int(value_str)
print('Inserted value is: $',value)

ten = 10000
twenty = 20000
tax = 0
#tax calculus (function)
def taxes(value):
    if value <= ten:
        return print('No need to pay taxes')
    elif ten < value and value <= twenty:
        tax = ten*0.1
        return print('Taxes are:', tax)
    elif value > twenty:
        first = 0
        second = ten*0.1
        other = (value-twenty)*0.2
        tax = first + second + other
        print('Taxes are:', tax)

taxes(value)

# 13
#list creation

for i in range(1,11):
    for j in range(1,11):
        print(i*j, end=" ")
    print('')

# 14
rows = 5

for i in range(rows + 1,0,-1):
    for j in range(0, i-1):
        print('*', end=' ')
    print('')

# 15
def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)


exponent(5, 4)