#!/usr/local/bin/python3
import sys
import numpy as np
from routingSlow import Router
from tqdm import tqdm

inputList = open (sys.argv[1], 'r')
newLevel = False
levelN = 0
levelsArr={}
sizes={}
routers={}
for i, line in enumerate(inputList):
	if i is 0:
		levels = line.rstrip()
		newLevel = True
		continue
	if newLevel:
		currHeight = 0
		levelN += 1
		levelsArr['level%d' % levelN] = []
		size = line.rstrip().split(' ',2)
		sizes['level%d' % levelN] = size
		width = size[1]
		height = size[0]
		newLevel = False
	else:
		if currHeight == int(height):
			newLevel = True
		else:
			notesArray = list(line.rstrip())
			
			levelsArr['level%d' % levelN].append(notesArray)
			currHeight += 1
			if currHeight == int(height):
				newLevel = True
inputList.close()

npLevels={}
knight = {}
princess = {}
destination = {}

print('MAPPING LEVELS...')
for level in tqdm(range(1,levelN+1)):
	npLevels['level%d' % level] = np.array(levelsArr['level%d' % level])
	routers['level%d' % level] =  [[Router([h,w], npLevels['level%d' % level][h][w], sizes['level%d' % level], npLevels['level%d' % level]) for w in range(int(sizes['level%d' % level][1]))] for h in range(int(sizes['level%d' % level][0]))]
	
	for h in range(int(sizes['level%d' % level][0])):
		for w in range(int(sizes['level%d' % level][1])): 
			if 'S' in routers['level%d' % level][h][w].getNature():
				knight['level%d' % level] = [h,w]
			if 'P' in routers['level%d' % level][h][w].getNature():
				princess['level%d' % level] = [h,w]
			if 'D' in routers['level%d' % level][h][w].getNature():
				destination['level%d' % level] = [h, w]
			routers['level%d' % level][h][w].tellDestinantions(routers['level%d' % level])

def findPath(origin, destination, level):
	whoCanGoTo = {}
	found = False
	phase = 1
	explored = []
	destinations = [destination]
	while found is False:
		whoCanGoTo['phase%d' % phase] = []
		noMoreToExplore=True
		for destination in destinations:
			hH = destination[0]
			wW = destination[1]
			if [destination] in explored:
				continue
			else: 
				noMoreToExplore = False
				explored.append([destination])
				whoCanGoTo['phase%d' % phase].extend(routers['level%d' % level][hH][wW].getOrigins())
		if origin in whoCanGoTo['phase%d' % phase]:
			return phase;
		elif noMoreToExplore:
			return -1;
			break
		else:
			destinations = whoCanGoTo['phase%d' % phase]
		
		phase+=1

print('FINDING SHORTEST PATHS...')		
outputList = open (sys.argv[2], 'w')
for level in tqdm(range(1,levelN+1)):
	path1 = findPath(knight['level%d' % level], princess['level%d' % level], level)
	path2 = findPath(princess['level%d' % level], destination['level%d' % level], level)
	if (path1 == -1) or (path2 == -1):
		outputList.write('Case #%d: IMPOSSIBLE\n' % level)
	else:
		outputList.write('Case #%d: %d\n' % (level, path1+path2))
outputList.close()

