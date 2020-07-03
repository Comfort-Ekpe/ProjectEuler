
'''
NUMBER TWO
by considering the terms in the fibonacci sequence whose values do not exceed 4 million, find the sum of the even valued 
terms

the terms looks like
	0, 1, 1, 2, 3, 5, 8, 13
'''
# let terms be the list of terms
terms  = []
a = 0
b = 1
# using the list comprehension method
# terms = [a  if i == 0 else b if i == 1 else  for i in range(100) ]
for i in range(100):
	if i == 0:
		terms.append(i)
	elif i == 1:
		terms.append(1)
	else:
		a = terms[i - 2]
		b = terms[i - 1]
		nth_term = a + b
		if nth_term >= 4000000:
			break
		terms.append(nth_term)

even_terms = [i for i in terms if i % 2 == 0]
# print(even_terms)
# print(sum(even_terms))
# print(terms)
# print(sum(terms))

# using list comprehension to solve the question
import math
alpha = float((1 + math.sqrt(5))/ 2)
beta = float((1 - math.sqrt(5))/ 2)
def find_nth_terms(n):
	return int(1 / math.sqrt(5) * (math.pow(alpha,n) - (math.pow(beta,n))))

terms = [i if i <= 1 else find_nth_terms(i) for i in range(100) if find_nth_terms(i) < 4000000]
even_terms = [i for i in terms if i % 2 == 0]

# using map
def add_ten(n):
	return n + 10
terms = list(map(add_ten,terms))
print(terms)
# print(even_terms)
# print(sum(even_terms))


table1 = []
table2 = []
table3 = []
table4 = []
table5 = []
table6 = []
i = 0
for i in range(1,13):
	table1.append(i * 1)
	table2.append(i * 2)
	table3.append(i * 3)
	table4.append(i * 4)
	table5.append(i * 5)
	table6.append(i * 6)
i = i + 1
# print("multiples of 1 are: ", table1)
# print("multiples of 2 are: ", table2)
# print("multiples of 3 are: ", table3)
# print("multiples of 4 are: ", table4)
# print("multiples of 5 are: ", table5)
# print("multiples of 6 are: ", table6)

# # # or
a,b = 1,21
table = {}
def makeTable(n):
	return [n * i for i in range(1,13)]
for i in range(a,b):
	table[str(i) + '_terms'] = makeTable(i)
# for key,value in table.items():
	# print(key,value)


# MAP
# map takes a function and an iterable