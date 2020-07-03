# list comprehension
ls = []
for i in range(21):
	for j in range (3):
		ls.append(i + j)

# generate the  list above in one line
# List comprehension using nested lists
ls =[i + j + k for i in range(21) for j in range(10) for k in range(1,10)]
# print the list
# print(ls)

# classwork
square = []
for i in range(1,101):
	square.append(i**2)
# print(square)

# using list comprehension
square = [i**2 for i in range(1,101)]
# print(square)


# usin already defined variables and funtions in list comprehension

def squared(x):
	return x ** 2

# using list comprehension
square = [squared(i) for i in range(10)]
# print(square)


# adding conditionals
for i in range(1,10):
	if i % 2 == 0 and i % 3 == 0:
		square.append(i ** 2)
# print(square)

# list comprhension method
square = [squared(j) for j in range(1,10) if j % 2 == 0 and j % 3 == 0 ]
# print(square)


# CLASSWORK TWO
# find the sine and cos of numbers from 1 to 100, if its even find the sine, if its odd, find the cos
import math
square = []
for i in range(10):
	if i % 2 == 0:
		square.append(math.sin(i))
	else:
		square.append(math.cos(i))
# print(square)

# list comprehension
square = [math.sin(i) if i % 2 == 0 else math.cos(i) for i in range(10) ]
# print(square)