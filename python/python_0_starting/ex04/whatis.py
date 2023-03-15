import sys as check

if len(check.argv) == 1:
	check.exit()
if len(check.argv) > 2:
	print("AssertionError: more than one argument are provided")
	check.exit()
try:
	if int(check.argv[1]) % 2:
		print("I'm Odd.")
		check.exit()
	print("I'm Even.")
except ValueError:
	print("AssertionError: argument is not an integer")

