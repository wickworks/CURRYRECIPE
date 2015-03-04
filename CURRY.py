
import prawncurry



pieceList = []


for team in range(0,2):
	#team 0 starts on row 0, team 1 starts on row 6
	starting_row = team * 6

	for column in range(0,8):
		#alternate between the top and bottom row
		row = starting_row + (column % 2)

		#make the pawn
		pawn = prawncurry.Pawn()
		pawn.initialize(team, column, row)
		pieceList.append(pawn)
	
		

def drawBoard():
	print("")
	for y in range(0,8):
		for x in range(0,8):
			empty = 1
			
			for piece in pieceList:
				if piece.x == x and piece.y == y:
					print("[" + str(piece.team) + "]"),
					empty = 0
					
			if empty == 1:
				print("[ ]"),
		
		print("")




drawBoard()




























