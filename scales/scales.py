import sys
from utils import MAYOR, MINOR, bitwiseCompare, getInputDict, mapToArray, rotateArray, outDict
import numpy as np

inputList = open (sys.argv[1], 'r')
outputList = open (sys.argv[2], 'w')
newSong = False
songN = 0
for i, line in enumerate(inputList):
	if i is 0:
		songs = line.rstrip()
		newSong = True
		continue
	if newSong:
		songN += 1
		outputList.write('Case #%d:' % songN)
		newSong = False
		notes = line.rstrip()
		if int(notes) is 0:
			for i in outDict:
				outputList.write(' M%s' %outDict[i])
			for i in outDict:
				outputList.write(' m%s' %outDict[i])
			outputList.write('\n')
			newSong = True
	else:
		notesArray = line.rstrip().split(' ', int(notes))
		mappedSong = rotateArray(mapToArray(set(notesArray)), 3)
		npArr = np.array(mappedSong)
		uniques = np.sum(npArr == 1)
		MmatchesIndex = []
		mmatchesIndex = []
		for i in range (0,12):
			attemptMayor = rotateArray(MAYOR,i)
			attemptMinor = rotateArray(MINOR,i)
			if bitwiseCompare(attemptMayor, mappedSong, uniques):
				MmatchesIndex.append(i)
			if bitwiseCompare(attemptMinor, mappedSong, uniques):
				mmatchesIndex.append(i)
		for i in MmatchesIndex:
			outputList.write(' M%s' % outDict[i])
		for i in mmatchesIndex:
			outputList.write(' m%s' % outDict[i])
		if len(MmatchesIndex) is 0 and len(mmatchesIndex) is 0:
			outputList.write(' None')
		outputList.write('\n')
		newSong = True
			
inputList.close()
outputList.close()