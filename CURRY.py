
import prawncurry



pieceList = []


for team in range(0,2):
	for pawns in range(0,8):
		pawn = prawncurry.Pawn()
		pawn.initialize(team, pawns)
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




























