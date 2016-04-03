#list is like array

def lists_101():
	#lists are initialized using bracket
	numbers = []
	#The way to assign initial values to lists:
	strings = ["hello", "world"]
	names = ["John", "Eric", "Jessica"]

	#Way to get value from list
	second_name = names[1]
	#way to define value in list
	numbers.append(1)
	numbers.append(2)
	numbers.append(3)



	# this code should write out the filled arrays and the second name in the names list (Eric).
	print(numbers)
	print(strings)
	print("The second name on the names list is %s" % second_name)

if __name__ == "__main__":
    lists_101()