#Python uses C-style string formatting to create new, formatted strings. 
#The "%" operator is used to format a set of variables enclosed in a "tuple" 
#(a fixed size list), together with a format string, 
#which contains normal text together with "argument specifiers", 
#special symbols like "%s" and "%d".

def string_formatter_101():
	#String use %s
	#integers use %d
	name = "John"
	age = 23
	print "%s is %d years old." % (name, age)	#(name, age) is the tuple

	#lists use %s as well
	mylist = [1,2,3]
	print "A list: %s" % mylist



# %s - String (or any object with a string representation, like numbers, lists)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)


if __name__ == '__main__':
	string_formatter_101()