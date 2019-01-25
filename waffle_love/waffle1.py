import sys

inputList = open (sys.argv[1], 'r')
outputList = open (sys.argv[2], 'w')
for i, line in enumerate(inputList):
	if i is 0:
		cases = line.rstrip()
		print(cases)
	else:
		am = line.split(' ', 2)
		upp = am[0]
		cross = am[1].rstrip()
		wholes = (int(upp)-1)*(int(cross)-1)
		outputList.write('Case #%d: %d\n' % (i, wholes))
		
inputList.close()
outputList.close()