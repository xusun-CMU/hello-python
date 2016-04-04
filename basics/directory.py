#direcoty is like hashmap in java
def direcoty_101():
	#way1
	phonebook = {}
	phonebook["John"] = 938477566
	phonebook["Jack"] = 938377264
	phonebook["Jill"] = 947662781

	#way2
	phonebook = {
	    "John" : 938477566,
	    "Jack" : 938377264,
	    "Jill" : 947662781
	}

	#itering the directory
	for name, number in phonebook.iteritems():
    	print "Phone number of %s is %d" % (name, number)

    #remove value
	del phonebook["John"]
	#or
	phonebook.pop("John")

	


	