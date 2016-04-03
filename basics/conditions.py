#There are couple of conditional operators in python:
# 1, boolean operator.
#	1.1 equal/notequal : ==/!=
#	1.2 and/or : and/or
# 2, in operator
# 	The "in" operator could be used to check if a specified object exists within an iterable object container,
#	such as a list:
# 3, The 'is' operator
#	Unlike the double equals operator "==", the "is" operator does not match the values of the variables, 
#	but the instances themselves.
# 4, python also has a not operator

#python logic block:
#if <statement is true>:
#    <do something>
#    ....
#    ....
#elif <another statement is true>: # else if
#    <do something else>
#    ....
#    ....
#else:
#    <do another thing>
#    ....
#    ....
# python also treat numnber '0' as false, other numbers as true. (like C)


def boolean_101():
	name = "John"
	age = 24
	if name == "John" and age != 23:
	    print "Your name is John, and you are not 23 years old."

	if name == "John" or name == "Rick":
	    print "Your name is either John or Rick."

def in_101():
	name = "John"
	age = 24
	if name in ["John", "Rick"]:
    	print "Your name is either John or Rick."

def is_101():
	x = [1,2,3]
	y = [1,2,3]
	print x == y # Prints out True
	print x is y # Prints out False


if __name__ == '__main__':
	boolean_101()
	in_101()