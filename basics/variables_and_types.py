#You do not need to declare variables before using them, or declare their type. 
#Every variable in Python is an object.


#Numbers
	#Python supports two types of numbers - integers and floating point numbers. 
	#(It also supports complex numbers, which will not be explained in this tutorial).
def number_101():
	myint = 7
	myfloat1 = 1.0
	myfloat2 = float(1.5)

	print(myint, myfloat1, myfloat2)

#Strings are defined either with a single quote or a double quotes.
def string_101():
	mystring1 = 'hello'
	mystring2 = "hello"
	#use case for using single quote
	mystring = "Don't worry about apostrophes"

def operation_101():
	one = 1
	two = 2
	three = one + two

	print three

	hello = "hello"
	world = "world"
	helloworld = hello + " " + world

	print helloworld


	# This will not work!
	# Mixing operators between numbers and strings is not supported:
	# print one + two + hello

def check_instance_and_print_101():
	mystring = "hello"
	myfloat = 10.0
	myint = 20

	# isinstance(variable, type): check the type of a variable
	# the c-stylc print can be used is python using % to sprate actrual content and variable
	if mystring == "hello":
	    print "String: %s" % mystring
	if isinstance(myfloat, float) and myfloat == 10.0:
	    print "Float: %d" % myfloat
	if isinstance(myint, int) and myint == 20:
	    print "Integer: %d" % myint


def main():
	number_101

