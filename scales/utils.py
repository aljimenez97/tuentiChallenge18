MAYOR = [1,0,1,0,1,1,0,1,0,1,0,1]
MINOR = [1,0,1,1,0,1,0,1,1,0,1,0]

def getInputDict():
	inputDict = {}
	inputDict.update(dict.fromkeys(['C','B#'], 0))
	inputDict.update(dict.fromkeys(['C#','Db'], 1))
	inputDict.update(dict.fromkeys(['D'], 2))
	inputDict.update(dict.fromkeys(['D#', 'Eb'], 3))
	inputDict.update(dict.fromkeys(['E', 'Fb'], 4))
	inputDict.update(dict.fromkeys(['F', 'E#'], 5))
	inputDict.update(dict.fromkeys(['F#', 'Gb'], 6))
	inputDict.update(dict.fromkeys(['G'], 7))
	inputDict.update(dict.fromkeys(['G#', 'Ab'], 8))
	inputDict.update(dict.fromkeys(['A'], 9))
	inputDict.update(dict.fromkeys(['A#', 'Bb'], 10))
	inputDict.update(dict.fromkeys(['B', 'Cb'], 11))

	return inputDict

outDict = {0:'A', 1:'A#', 2: 'B', 3: 'C', 4: 'C#', 5: 'D', 6: 'D#', 7: 'E', 8: 'F', 9: 'F#', 10: 'G', 11: 'G#'}

def bitwiseCompare(arr1, arr2, uniques):
	matches = 0
	for i,note in enumerate(arr1):
		if note is 1 and note is arr2[i]:
			matches += 1
	if matches == uniques:
		return True
	else:
		return False

def getInputArray(line):
	pitchDict = getInputDict()

def mapToArray(uniqueNotes):
	notes = uniqueNotes
	myArray = []
	myDict = getInputDict()
	for note in uniqueNotes:
		myArray.append(myDict[note])
	outArray = [0]*12
	for i in myArray:
		outArray[i] = 1
	return(outArray)

def rotateArray(arr, rot):
	return (arr[-rot:]+arr[:-rot])

