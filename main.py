# Простая игра крестики-нолики в терминале

class Board:
	def __init__(self):
		"""
		Инициализация доски.
		"""
		self.board = [
			['-', '-', '-'],
			['-', '-', '-'],
			['-', '-', '-'],
		]

	def show_board(self) -> None:
		"""
		Показ доски.
		"""
		print (' ', 0, 1, 2)
		n = 0
		for row in self.board:
			print(f'{n} {" ".join(row)}')
			n += 1

	def make_move(self, row: int, column: int, player: str) -> None:
		"""
		Выполнить ход на доске.
		:param row: Номер строки.
		:param column: Номер столбца.
		:param player: Символ игрока
		"""
		self.board[row][column] = player

	def is_empty(self, row: int, column: int) -> bool:
		"""
		Проверка на пустую ячейку.
		:param row: Номер строки.
		:param column: Номер столбца.
		:return: True, если пусто, иначе False.
		"""
		if self.board[row][column] == '-':
			return True
		return False
		
	def is_win(self, player: str) -> bool:
		"""
		Проверка поля на победную комбинацию.
		:param player: Символ игрока.
		:return: True, если имеется победная комбинация, иначе False.
		"""
		for i in range(3):
			if all(cell == player for cell in self.board[i]): # Проверка всех горизонтальных линий.
				return True
			if all(self.board[j][i] == player for j in range(3)): # Проверка всех вертикальных линий.
				return True
		# Проверка двух диагоналей.
		if all(self.board[i][i] == player for i in range(3)):
			return True
		if all(self.board[i][2 - i] == player for i in range(3)):
			return True
		return False

	def is_draw(self) -> bool:
		"""
		Проверка доски на ничью.
		:return: True, если нет пустых ячеек, иначе False.		
		"""
		if all(cell != '-' for row in self.board for cell in row):
			return True
		return False


class Player:
	def __init__(self):
		"""
		Инициализация игроков.
		"""
		self.players = ['X','O']
		self.current_player = 0

	def switch_player(self) -> None:
		"""
		Смена хода игрока.
		"""
		self.current_player = 1 - self.current_player
	
	def get_current_player(self) -> str:
		"""
		Получить нынешнего игрока.
		:return: Символ игрока.
		"""
		return self.players[self.current_player]

	def make_move(self, row: int, column: int, board: Board) -> None:
		"""
		Выполнить ход.
		:param row: Номер строки.
		:param column: Номер столбца.
		:param board: Класс Доски.
		"""
		player = self.get_current_player()
		if row >= 3 or column >= 3:
			raise IndexError('Выход за ограничения поля. Ввводите корректные номера столбоц и строк.')
		if board.is_empty:
			board.make_move(row=row, column=column, player=player)
		else:
			raise ValueError(f'Клетка {row}:{column} уже занята.')

def main() -> None:
	"""
	Основной цикл игры.
	"""
	pos_anser = ('y', 'yes')
	while True:
		board = Board()
		players = Player()

		while True:
			print('')
			board.show_board()
			current_player = players.get_current_player()
			print('')
			print (f'Ход игрока - {current_player}.')

			try:
				row = int(input('Введите номер строки: '))
				column = int(input('Введите номер столбца: '))
				players.make_move(row=row, column=column, board=board)
			except (ValueError, IndexError) as e:
				print('')
				print(f'Ошибка ввода: {e}')
				continue
			else:
				if board.is_win(player=current_player):
					print('')
					board.show_board()
					print('')
					print (f'Игрок - {current_player} - победил')
					break
				if board.is_draw():
					print('')
					board.show_board()
					print('')
					print ('НИЧЬЯ!!!')
					break

				players.switch_player()

		answer = input('Хотите ещё игру? (y/n): ')
		if answer.lower() in pos_anser:
			continue
		break

if __name__ == '__main__':
	main()
