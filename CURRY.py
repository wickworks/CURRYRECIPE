#this one runs the game (hopefully)
"""board tiles are identified by their index in
the board array. The board array is a mixed array 
of empty spots (numbers) and pawns.
Tiles with value 2 are empty squares.

How the game plays:
-There's a turn counter. When it's 0, team 0 pieces
can move and team 1 pieces can't, and when it's 1
then the reverse is true.
-On a turn, check to see if one team has no pieces
left. Then ask the player which piece they want to
move. check to see if there's an appropriate piece
in that space. Then ask where to go. Get movable
and capturable locations, and see if it's one of
them. Then check that other pieces are and aren't
in appropriate locations. If everything is good,
change the board and then tell the pawn to change
its location. Then redraw the board. If it's a 
capture, ask if the player wants to make another
move.
"""
import prawncurry #pawn class

pieceList = []
board = []
isCurryReady = 'no'
turn = 1
moveTo = 0

def makeStartingPawns():
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

#sets the board to its empty "2" state
def emptyBoard():
	#clears out the entire board
	board = []
	#makes 64 "2"s
	for x in range(0,8):
		for y in range(0,8):
			board.append[2]	

#adds pieces to the (presumably empty) board
def addPieces():
	for pawn in pieceList:
		board[pawn.boardLocation()] = pawn

#checks to see if the curry is ready and we don't have to play checkers anymore
def checkCurry():
	team0 = 0
	team1 = 0
	for pawn in pieceList:
		if pawn.team == 0:
			team0 += 1
		else
			team1 += 1
	if team0 == 0
		print "Game over. Team 1 wins."
		return 'muffins'
	elif team1 == 0
		print "Game over. Team 1 brings shame to their people."
		return 'yes'
	else
		return 'no'

#draws the current board in all its ASCII glory
def drawBoard():
	print("")
	for y in range(0,8):
		for x in range(0,8):
			if board[(x,y)] != 2
				print("[" + str(board[x].team) + "]");		
			else:
				print("[ ]"),
		
		print("")

#returns whatever is on the board at a given x,y
def boardAt(x,y):
	return board[(x + 8*y)]

#initializes the board for the first time
emptyBoard()

#make all the pawns
makeStartingPawns()
currentPawn = pieceList[0];

#"""
while isCurryReady == 'no':
	turn = (turn + 1) % 2
	print("Player " + str(turn) + "'s turn.")
	while x = 0:
		print("Which piece do you want to move?")
		print("(Use x,y coordinates to select a square.)")
		userX = input("x: ")
		userY = input("y: ")
		if boardAt(userX, userY).team == turn:
			currentPawn = boardAt(userX, userY)
			break
		else:
			print("You don't have a pawn on that square.")
	moveLocations = currentPawn.possibleMoves();
	#captureLocations = currentPawn.possibleCaptures();
	while x = 0:
		print("Where do you want to move?")
		print("(Use x,y coordinates to select a square.)")
		userX = input("x: ")
		userY = input("y: ")
		#need to add for loop to check possibleMoves
			if boardAt(userX, userY) = possibleMoves(x): #make it do things
			moveTo = (userX, userY)
			break
		else:
			print("That's not a legal move.")
	#if it's a capture, get rid of the captured piece
	#then move the pawn:
	pawn.x = userX
	pawn.y = userY
	#redraw the board and see if anyone's won
	emptyBoard()
	addPieces()
	drawBoard()
	isCurryReady = checkCurry()
	#if it was a capture, same player should have option to move again

"""




























