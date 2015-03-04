#This is a pawn
class Pawn:
	team = 0
	x = 0
	y = 1

	#kinged 
	kinged = 0

	def initialize(self, team, x, y):
		self.team = team
		self.x = x
		self.y = y
			
	
	# returns a list of all MOVES given the location, team, and whether it's kinged
	# e.g. [[2,0],[0,2]]
	def possibleMoves(self):
		moveList = []
		
		# four possible movement directions
		# 0 = UP LEFT
		# 1 = UP RIGHT
		# 2 = DOWN LEFT
		# 3 = DOWN RIGHT
		for direction in range(0,4):
			movex = 0
			movey = 0

			#the top team can only move down (unless kinged) and vice-versa
			valid_direction = True
			if not kinged:
				if team == 0:
					if direction == 0 or direction == 1:#TOP team can't move UPLEFT or UPRIGHT
						valid_direction = False
				elif team == 1:
					if direction == 2 or direction == 3:#BOTTOM team can't move DOWNLEFT or DOWNRIGHT
						valid_direction = False

			#if this is a valid direction for this pawn, add the movement coordinate to the list
			if valid_direction:
				if direction == 0:		#UP LEFT
					movex = -1
					movey = -1
				elif direction == 1:	#UP RIGHT
					movex = 1
					movey = -1
				elif direction == 2:	#DOWN LEFT
					movex = -1
					movey = 1
				elif direction == 3:	#DOWN RIGHT
					movex = 1
					movey = 1
				
				#convert to absolute board coordinates			
				movex = x + movex
				movey = y + movey
					
				#check to see if this move is on the board and add it to the move list if so
				if movex >= 0 and movex < 8:
					if movey >= 0 and movey < 8:
						moveList.append([movex,movey])
		
		# returns the list of possible move coordinates
		return movelist

	def possibleCaptures(self):
		
			
	def boardLocation(self):
		return (self.x + 8*self.y)