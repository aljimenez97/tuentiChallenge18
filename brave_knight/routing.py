import numpy as np
class Square:

	def __init__(self, position, nature, region, matrix):
		
		self.id = str(position[0]) + str(position[1])
		self.position = position
		self.nature = nature 
		self.reachableBy = []
		self.routes = self.neighbourIterator(position, self.axis[self.nature], region[0], region[1], matrix)
		self.region = region
		self.matrix = matrix
		#repr(self)

	axis = {'#': [0,0], 'S': [[1,2], [2,1]], 'P': [[1,2], [2,1]], 'D': [[1,2], [2,1]], '.': [[1,2], [2,1]], '*': [[2,4], [4,2]] }
	myBase = [[1,1],[1,-1],[-1,1],[-1,-1]]
	def neighbourIterator(self, myPosition, myAxis, height, width, matrix):
		pos = np.array(myPosition)
		neighbours = []
		for ax in myAxis:
			for i in self.myBase:
				attempt = pos + np.array(i)*np.array(ax)
				if self.checkNeighbourExists(attempt, height, width, matrix):
					neighbours.append([ str(attempt[0]) + str(attempt[1]), attempt, str(myPosition[0]) + str(myPosition[1]), myPosition, 1])
		return neighbours

	def checkNeighbourExists(self, neighbour, height, width, matrix):
		neigHeight = int(neighbour[0])
		neigWidth = int(neighbour[1])
		if neigHeight >= int(height) or neigWidth >= int(width) or neigHeight < 0 or neigWidth < 0:
			return False
		elif '#' in matrix[neigHeight][neigWidth]:
			return False
		else:
			return True

	def addOrigin(self, origin):
		self.reachableBy.append(origin)

	def getNature(self):
		return self.nature


	def getOrigins(self):
		return self.reachableBy

	def tellDestinantions(self, routerMatrix):
		for route in self.routes:
			routerMatrix[route[1][0]][route[1][1]].addOrigin(self.position)

	def printOrigins(self):
		print('-----------------------------------------------------------------------------------------------')
		print('ID ' + self.id)
		for origin in self.reachableBy:
			print("%s can come to me" % origin[0])
		if len(self.reachableBy) is 0:
			print("Nobody can come to me")

	def __repr__(self):
		print('-----------------------------------------------------------------------------------------------')
		print('ID ' + self.id)
		print('POSITION ' + str(self.position))
		print('NATURE: ' + self.nature)
		print('REGION: ' + str(self.region))
		print('ROUTES:')
		for route in self.routes:
			print('I can go to %s via %s, %d hop away' % (route[0], route[2], route[4]))
		if len(self.routes) is 0:
			print('I can go nowhere')
		return self.id





	



