#astring="Hello world!"
# print astring.index("o"): get the first index
# print astring.count("l"): print appearance of a certain value
# print astring[3:7]: print the substring. exclusive of the second index
	# If you just have one number in the brackets, it will give you the single character at that index.
	# If you leave out the first number but keep the colon, it will give you a slice from the start to the number you left in. 
	# If you leave out the second number, it will give you a slice from the first number to the end.
	# You can even put negative numbers inside the brackets. 
	#  They are an easy way of starting at the end of the string instead of the beginning. 
	#  This way, -3 means "3rd character from the end".
# print astring[3:7:2]: This prints the characters of string from 3 to 7 skipping one character. 
	# This is extended slice syntax. The general form is [start:stop:step].


#Other obvious functions:
# afewwords = astring.split(" "): ["Hello", "world!"]
# print astring.startswith("Hello"): true
# print astring.endswith("asdfasdfasdf"): false