import random
import string
import time
from getpass import getpass

i = 0
passwd = getpass()
count = 1

def ranpass():
  # comment below line from "+ string.ascii_uppercase + ..." to quickly test programm only with digits
	chars = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
  # adjust the second argument to define passwd length 
  # a length of 4 combined with digits its the most quickly way to test the program
	size = random.randint(4, 12)
	return ''.join(random.choice(chars) for x in range(size))

start = time.time()
while i < 1:
	rp = ranpass()

	if passwd == rp:
		print("The password is:", rp, "and it took",count, "iterations in {0:.2f}".format(time.time() - start), "seconds.")
		i = 1
	else:
		print(rp)
		i = 0
	count += 1
	
