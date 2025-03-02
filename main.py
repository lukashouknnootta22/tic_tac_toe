#Tic Tac Toe on the command line

def show_board(board: list):
	''' 
	Shows the current state of the playing field

	:param board: playing field in the form of a list
	'''
	print ('')
	print (' ', 0, 1, 2)
	n = 0
	for row in board:
		print(f'{n} {' '.join(row)}')
		n += 1

def make_move(board: list, player: str):
	'''
	Taking the current player's turn

	:param board: playing field in the form of a list
	:param player: current player
	'''
	print (f'Player - {player} moves')
	print ('')
	while True:
		try:
			row = int(input('Enter row number: '))
			column = int(input('Enter column number: '))

			if board[row][column] != '-':
				print ('Selected cell is occupied')
			else:
				board[row][column] = player
				break
		except (IndexError, ValueError): #Processing incoming results according to the required format and range
			print ('Please enter only numbers from 0 to 2')

def check_winner(board, player):
	'''
	Checking the playing field for a winning combination

	:param board: playing field in the form of a list
	:param player: current player
	:return: True, if a winning combination is found, False otherwise 
	'''
	for i in range(3):
		if all(cell == player for cell in board[i]): # Checking all horizontal lines
			return True
		if all(board[j][i] == player for j in range(3)): # Checking all vertical lines
			return True
	# Checking Diagonals
	if all(board[i][i] == player for i in range(3)):
		return True
	if all(board[i][2 - i] == player for i in range(3)):
		return True
	return False

def is_draw(board):
	'''
	Checking the playing field for a draw (presence of empty cells)

	:param board: playing field in the form of a list
	:return: True, if all cells are occupied, False otherwise 
	'''
	if all(cell != '-' for row in board for cell in row):
		return True
	return False

def game():
	'''
	Main Function: Runs other functions and has initial values
	'''
	board = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]
	players = ['X','O']
	current_player = 0

	while True:
		show_board(board)
		player = players[current_player]
		make_move(board, player)

		if check_winner(board, player):
			show_board(board)
			print (f'Player - {player} wins')
			break

		if is_draw(board):
			show_board(board)
			print ('Draw')
			break
			
		current_player = 1 - current_player

game()