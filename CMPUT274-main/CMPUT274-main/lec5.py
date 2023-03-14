theCount = 0
done = False
while not done:
	try:
		word = input("Word: ")
	except EOFError:
		done = True
		continue
		if word in [ 'exit', 'Exit' ]:
			done = True
		if word in [ 'the', 'The' ]:
			theCount = theCount + 1
print( "Total count %s" % (theCount) )