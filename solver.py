class Sudoku:
	def __init__(self):
		self.game = [
			[5, 3, 0, 0, 7, 0, 0, 0, 0],
			[6, 0, 0, 1, 9, 5, 0, 0, 0],
			[0, 9, 8, 0, 0, 0, 0, 6, 0],
			[8, 0, 0, 0, 6, 0, 0, 0, 3],
			[4, 0, 0, 8, 0, 3, 0, 0, 1],
			[7, 0, 0, 0, 2, 0, 0, 0, 6],
			[0, 6, 0, 0, 0, 0, 2, 8, 0],
			[0, 0, 0, 4, 1, 9, 0, 0, 5],
			[0, 0, 0, 0, 8, 0, 0, 7, 9]
		]


	# Main function to traverse the grid
	def sudoku(self):

		for i, g in enumerate(self.game):
			for j, h in enumerate(g):

				# Check if number has already been assigned
				if h == 0:
					for k in range(1, 10):
						if self.check_all(g, i, j, k):
							self.game[i][j] = k

							# Recursively call the method to check the grid is valid
							if self.sudoku():
								return True

							# If number is not valid assign 0
							self.game[i][j] = 0

					return False

		return True


	# Wrapper function the calls other functions to check if the number is valid for the current position
	# Return true if number is valid, false otherwise
	def check_all(self, g, i, j, k):

		# Calls function to check for row
		row = self.row_check(g, k)

		# Calls function to check for column
		col = self.col_check(j, k)

		grid = False
		if i < 3:
			grid = self.grid_call(0, j, k)
		elif i >= 3 and i < 6:
			grid = self.grid_call(3, j, k)
		else:
			grid = self.grid_call(6, j, k)

		return row and col and grid


	# Function to check if the number is present in the row
	def row_check(self, g, k):

		if k not in g:
			return True

		return False


	# Function to check if the number is present in the column
	def col_check(self, j, k):

		for l in range(9):
			if self.game[l][j] == k:
				return False

		return True


	# Function to check if the number is present in the grid or not
	# This function is a wrapper function with parameters to calculate the grid of the current position
	def grid_call(self, p, j, k):

		if j < 3:
			return self.grid_check(p, 0, k)
		elif j >= 3 and j < 6:
			return self.grid_check(p, 3, k)
		else:
			return self.grid_check(p, 6, k)


	# Function to check if the number is present in the grid or not
	def grid_check(self, i, j, k):

		for l in range(i, i+3):
			for m in range(j, j+3):

				if self.game[l][m] == k:
					return False

		return True


	# Finds the solution to the problem
	def find_solution(self):

		print("Problem to solve: ")

		for _, t in enumerate(self.game):
			print(t)

		print()
		print("Solution: ")

		if self.sudoku():
			for _, t in enumerate(self.game):
				print(t)
		else:
			print("Invalid sudoku problem")


def main():
	sudoku_solution = Sudoku()
	sudoku_solution.find_solution()


if __name__ == "__main__":
	main()
