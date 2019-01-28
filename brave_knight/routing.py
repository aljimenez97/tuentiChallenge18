#!/usr/local/bin/python3

import numpy as np
from heapq import heappush, heappop

class Grid:
	def __init__(self):
		self.S = 0
		self.P = 0
		self.D = 0
		self.matrix = []

	def setMatrix(self, matrix):
		self.matrix = np.array(matrix)

	def setAttribute(self, row, height):
		if 'S' in row:
			self.S = (height, row.index('S'))
		if 'P' in row:
			self.P = (height, row.index('P'))
		if 'D' in row:
			self.D = (height, row.index('D'))

	# Generators improved performance over filtering or if/else return
	def isAllowed(self, neighbours):
		(height, width) = self.matrix.shape
		return (n for n in neighbours if 0 <= n[0] < height and 0 <= n[1] < width and self.matrix[n[0], n[1]] != '#')

	def getNeighbours(self, pos):
		axis1 = [(-1,-2), (-2,-1), (-1,2), (-2,1), (1,-2), (2, -1), (1,2), (2,1)]
		axis2 = [(-2,-4), (-4,-2), (-2,4), (-4,2), (2,-4), (4, -2), (2,4), (4,2)]
		(h,w) = pos
		# Accessing matrix via [X,Y] proved to be more efficient than [][] (numpy vs py)
			# Avoid calculation of coef* every iter in loop
			#coef = 2 if self.matrix[h,w] == '*' else 1
		axis = axis2 if self.matrix[h,w] == '*' else axis1
		neighbours = self.isAllowed([( h + ax[0], w + ax[1]) for ax in axis])
		return list(neighbours)

# Dijkstra cost-focused implementation
# Calculations extracted from for loop to reduce compute time (attemptCost is constant for all neighbours)
def findCost(grid, origin, destination):
	queue = []
	heappush(queue, (0, origin))
	cost = {origin: 0}
	while len(queue):
		currentNode = heappop(queue)[1]
		if currentNode == destination:
			return cost[destination]
		attemptCost = cost[currentNode] +1
		for neighbour in grid.getNeighbours(currentNode):
			if neighbour not in cost or attemptCost < cost[neighbour]:
				cost[neighbour] = attemptCost
				heappush(queue, (attemptCost, neighbour))
	return -1

