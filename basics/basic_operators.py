#Arithmetic Operators:
	#Same as other languages:
	# 	plus: +
	#	minus: -
	#	multiple: *
	#	divide: /
	#	mod: %
	#	pow: **

#Using Operators with Strings
#	Python supports concatenating strings using the addition operator:
def string_op_101():
	helloworld = "hello" + " " + "world"
	print helloworld

	lotsofhellos = "hello" * 3
	print lotsofhellos

#Using Operators with Lists
#Lists can be joined with the addition operators:
def lists_op_101():
	even_numbers = [2,4,6,8]
	odd_numbers = [1,3,5,7]
	all_numbers = odd_numbers + even_numbers
	print all_numbers	#print 13572468 in sequence

	print [1,2,3] * 3

if __name__ == '__main__':
	string_op_101()
	lists_op_101()