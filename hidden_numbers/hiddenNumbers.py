import sys

inputList = open (sys.argv[1], 'r')
outputList = open (sys.argv[2], 'w')
for i, line in enumerate(inputList):
	myStr = ''
	if i is 0:
		cases = line.rstrip()
	elif i is 1:
		length = len(set(line.rstrip()))
		bigN = 0
		smallN = 0
		for j in range(0,length):
			bigN +=  j*length**(j)
			if j is (length-1):
				smallN += length**(length-1)
			elif j is (length-2):
				continue
			else:
				smallN += (length-j-1)*length**(j)
		print(bigN)
		print(smallN)
		outputList.write('Case #%d: %d\n' % (i, bigN-smallN))
		
		
inputList.close()
outputList.close()