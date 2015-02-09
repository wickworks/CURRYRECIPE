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