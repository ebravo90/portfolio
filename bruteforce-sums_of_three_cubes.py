# based on https://en.wikipedia.org/wiki/Sums_of_three_cubes
import random
import string

i = 0
count = 1

class variable:
	def __new__(cls):
# size lenght for variable, for a full ecuation the lenght should be 1-17
		size = random.randint(1, 1)
		num = ''.join(random.choice(string.digits) for x in range(size))

		def negative():
			neg = int(num) * -1
			return neg
		def positive():
			pos = int(num)
			return pos

		neg = negative()
		pos = positive()
		op = [neg, pos]
		ran = random.choice(op)
		return ran

print("Enter result for generates ecuation: ")
inp = input()
res = int(inp)

while i < 1:
# uncomment(under your own risk) for use each variable
	x = variable()
	#y = variable()
	#z = variable()
# uncomment(under your own risk) the number of sum desired
	operator = (x ** 3) #+ (y ** 3) + (z ** 3)

	if operator == res:
# each print are equal to a mid to full size ecuation 
		#print("Correct ecuation is: (" + str(x) + ")^3 + (" + str(y) + ")^3 + (" + str(z) + ")^3 = " + str(operator))
		#print("Correct ecuation is: (" + str(x) + ")^3 + (" + str(y) + ")^3 = " + str(operator))
		print("Correct ecuation is: (" + str(x) + ")^3 = " + str(operator))
		i = 1
	else:
# each print are equal to a mid to full size ecuation 
		#print("Trying: (" + str(x) + ")^3 + (" + str(y) + ")^3 + (" + str(z) + ")^3 = " + str(operator))
		#print("Trying: (" + str(x) + ")^3 + (" + str(y) + ")^3 = " + str(operator))
		print("Trying: (" + str(x) + ")^3 = " + str(operator))
		i = 0
	count += 1

