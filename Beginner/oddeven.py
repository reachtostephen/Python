try:
	N = int(raw_input())

	if N>=0:
		if(N%2==0):
			print("Even")
		else:
			print("Odd")
except:
	print("Exception")
