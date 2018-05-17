try:
	a = int(raw_input())
	b = int(raw_input())
	c = int(raw_input())


	if a > b and a > c:
		print("a is Greater")
	elif b > a and b > c:
		print("b is Greater")
	else:
		print("c is Greater")
except:
	print("Enter a valid input")
