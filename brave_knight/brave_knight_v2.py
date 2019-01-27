#!/usr/local/bin/python3
import sys
from routing import Grid, findCost
from tqdm import tqdm
from multiprocessing.pool import Pool

# Allow pool to have uo to 2 workers
pool = Pool(processes=2)

inputList = open (sys.argv[1], 'r')
outputList = open (sys.argv[2], 'w')
newLevel = False
levelN = 0

for i, line in enumerate(inputList):
	if i == 0:
		print('SAVING THE PRINCESS...')
		pbar = tqdm(total = int(line.rstrip()))
		newLevel = True
		continue
	if newLevel:
		currHeight = 0
		levelN += 1
		matrix = []
		grid = Grid()
		height = line.rstrip().split(' ',1)[0]
		newLevel = False
	else:
		if currHeight == int(height):
			pbar.update(1)
			newLevel = True
		else:
			row = list(line.rstrip())
			if 'S' or 'P' or 'D' in row:
				grid.setAttribute(row, currHeight)
			matrix.append(row)
			currHeight += 1
			if currHeight == int(height):
				grid.setMatrix(matrix)
				# Launch tasks simultaneously (not much time gain though)
				cost1_async = pool.apply_async(findCost,(grid, grid.S, grid.P))
				cost2_async = pool.apply_async(findCost,(grid, grid.P, grid.D))
				# Wait for results 
				cost1 = cost1_async.get()
				cost2 = cost2_async.get()

				if cost1 != -1 and cost2 != -1:
					# Princess can be saved!
					outputList.write('Case #%d: %d\n' % (levelN, cost1+cost2))
				else:
					# Knight cannot save the princess =(
					outputList.write('Case #%d: IMPOSSIBLE\n' % levelN)
				pbar.update(1)
				newLevel = True
inputList.close()
pbar.close()