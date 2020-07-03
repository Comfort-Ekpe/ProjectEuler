'''
NUMBER ONE
if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. the sum of these multiples
is 23. find the sum of all the multiples of 3 or 5 below 100, the answer is 233168
'''
def MultiplesOf3or5():
	x = []
	for i in range(0,1000):
		if i % 3 == 0 or i % 5 == 0:
			x.append(i)
	print(sum(x))
MultiplesOf3or5()

'''
NUMBER TWO
by considering the terms in the fibonacci sequence whose values do not exceed 4 million, find the sum of the even valued 
terms
'''

n1 = 0
n2 = 1
# fibonacci = []
# get the length of the fibonacci sequence you want to find from the user
length = int(input("Enter the length of the fibonacci sequence you want to find: "))
# for i in fibonacci:
# 	if i % 2 == 0:
# 		fibonacci.append(i)
# 		summer = sum(fibonacci)
		# print(summer)
# set your count
count = 0
if length <= 0:
	x  = int(input("Please input a number greater than 0: "))
	# fibonacci.append(nth_term)
	print("This fibonacci sequence has {} elements".format(length), )
			
elif length == 1:
	print(f'This fibonacci sequence has element', n1, (length))
	
	# fibonacci.append(nth_term)
else:
	# length > 1
	print("This fibonacci sequence has {} elements".format(length), )
	while count < length:

		print (n1, end= ',')
		nth_term = n1 + n2
		n1 = n2
		n2 = nth_term
		# fibonacci.append(n1)
		count += 1
		
