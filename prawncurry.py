#This is a pawn
class Pawn:
	team = 0
	x = 0
	y = 1

	def initialize(self, team, x):
		self.team = team
		self.x = x
		if team == 1:
			self.y = 6
		else:
			self.y = 1
			
	
	# returns a list of all possible MOVES and CAPTURES
	# e.g. [ [ [2,0],[ 0,2] ] , [ [4,0],[ 0,4] ] ]
	#     move coords ^                 ^ capture coords
	def possibleMoves(self):
		moveList = []
		captureList = []
		
		# four possible movement directions
		movex = 0
		movey = 0
		for move in range(0,4):
			if move == 0:	#UP LEFT
				movex = -1
				movey = -1
			elif move == 1:	#UP RIGHT
				movex = 1
				movey = -1
			elif move == 2:	#DOWN LEFT
				movex = -1
				movey = 1
			elif move == 3:	#DOWN RIGHT
				movex = 1
				movey = 1
			
			#capture moves are the same only bigger
			capturex = movex * 2
			capturey = movey * 2
			
			#set the movement/capture to absolute board coordinates			
			movex = x + movex
			movey = y + movey
			
			capturex = x + capturex
			capturey = y + capturey
				
			#check to see if this move is on the board and add it to the move list if so
			if movex >= 0 and movex < 8:
				if movey >= 0 and movey < 8:
					moveList.append([movex,movey])
		
			#check to see if this capture is on the board and et cetera
			if capturex >= 0 and capturex < 8:
				if capturey >= 0 and capturey < 8:
					captureList.append([capturex,capturey])
		

		# returns both the MOVE and CAPTURE coordinate possibilities
		return [movelist, captureList]

		
			
	def boardLocation(self):
		return (self.x + 8*self.y)