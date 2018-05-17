try:
	a = int(raw_input())
	b = int(raw_input())
	c = int(raw_input())


	if a > b and a > c:
		print("a is Greater")
	elif b > a and b > c:
		print("b is Greater")
	elif c > a and c > b:
		print("c is Greater")
except:
	print("Input is not a digit")
