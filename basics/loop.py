#1, for loop
#1.1	for x in xx
#			...
#2.2	For loops can iterate over a sequence of numbers using the "range" and "xrange" functions. 
#		The difference between range and xrange is that 
#		the range function returns a new list with numbers of that specified range, 
#		whereas xrange returns an iterator, which is more efficient. 
#		(Python 3 uses the range function, which acts like xrange). 
#		Note that the xrange function is zero based.
#2, while loop

#Python has the same continue / break as Java



#unlike languages like C,CPP.. we can use else for loops. 
#When the loop condition of "for" or "while" statement fails then code part in "else" is executed. 
# If break statement is executed inside for loop then the "else" part is skipped. 
# Note that "else" part is executed even if there is a continue statement.


def for_loop_101():

	print("--------- for loop example")

	# Prints out the numbers 0,1,2,3,4
	for x in xrange(5): # or range(5)		#Like the java old fashioned for loop using a pointer
	    print x

	# Prints out 3,4,5
	for x in xrange(3, 6): # or range(3, 6)
	    print x

	# Prints out 3,5,7
	for x in xrange(3, 8, 2): # or range(3, 8, 2)
	    print x

def while_loop_101():
	# Prints out 0,1,2,3,4
	print("--------- while loop example")
	count = 0
	while count < 5:
	    print count
	    count += 1  # This is the same as count = count + 1

def else_for_loop_101():
	# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

	print("--------- else in loop example")

	count=0
	while(count<5):
	    print count
	    count +=1
	else:
	    print "count value reached %d" %(count)

	# Prints out 1,2,3,4
	for i in xrange(1,10):
	    if(i%5==0):
	        break
	    print i
	else:
	    print "this is not printed because for loop is terminated because of break but not due to fail in condition"


if __name__ == '__main__':
	for_loop_101()
	while_loop_101()
	else_for_loop_101()