class Board:

	def __init__(self):
		self.board = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]

	def show_board(self):
		print ('')
		print (' ', 0, 1, 2)
		n = 0
		for row in self.board:
			print(f'{n} {' '.join(row)}')
			n += 1

	def make_move(self, row, column, player):
		self.board[row][column] = player

	def check_cell(self, row, column):
		if self.board[row][column] != '-':
			return False
		return True
		
	def is_win(self, player):
		for i in range(3):
			if all(cell == player for cell in self.board[i]): # Checking all horizontal lines
				return True
			if all(self.board[j][i] == player for j in range(3)): # Checking all vertical lines
				return True
		# Checking Diagonals
		if all(self.board[i][i] == player for i in range(3)):
			return True
		if all(self.board[i][2 - i] == player for i in range(3)):
			return True
		return False

	def is_draw(self):
		if all(cell != '-' for row in self.board for cell in row):
			return True
		return False


class Player:

	def __init__(self):
		self.players = ['X','O']
		self.current_player = 0

	def switch_player(self):
		self.current_player = 1 - self.current_player
	
	def get_current_player(self):
		return self.players[self.current_player]

	def make_move(self, board):
		player = self.get_current_player()
		print('')
		print (f'Player - {player} moves')

		while True:
			try:
				row = int(input('Enter row number: '))
				column = int(input('Enter column number: '))

				if not board.check_cell(row, column):
					print('This cell is occupated')
					continue
				board.make_move(row, column, player)
				break
			except (IndexError, ValueError): #Processing incoming results according to the required format and range
				print ('Please enter only numbers from 0 to 2')


def game():

	board = Board()
	players = Player()

	while True:
		board.show_board()
		current_player = players.get_current_player()
		players.make_move(board)

		if board.is_win(current_player):
			board.show_board()
			print (f'{current_player} is win')
			break
		if board.is_draw():
			board.show_board()
			print (f'Its Draw')
			break

		players.switch_player()

game()


	





