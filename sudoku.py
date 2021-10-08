from z3 import *

# https://en.wikipedia.org/wiki/Sudoku
puzzle = [
	[5, 3, 0,  0, 7, 0,  0, 0, 0],
	[6, 0, 0,  1, 9, 5,  0, 0, 0],
	[0, 9, 8,  0, 0, 0,  0, 6, 0],

	[8, 0, 0,  0, 6, 0,  0, 0, 3],
	[4, 0, 0,  8, 0, 3,  0, 0, 1],
	[7, 0, 0,  0, 2, 0,  0, 0, 6],

	[0, 6, 0,  0, 0, 0,  2, 8, 0],
	[0, 0, 0,  4, 1, 9,  0, 0, 5],
	[0, 0, 0,  0, 8, 0,  0, 7, 9],
]

s = Solver()
N = 9
grid = [[Int("grid_" + str(r) + str(c)) for c in range(N)] for r in range(N)]

for r in range(N):
	for c in range(N):
		if puzzle[r][c] != 0:
			s.add(grid[r][c] == puzzle[r][c])

for i in range(N):
	for j in range(N):
		s.add(grid[i][j] > 0, grid[i][j] < N + 1)
	s.add(Distinct(grid[i]))
	s.add(Distinct([r[i] for r in grid]))

for i in range(int(N/3)):
	for j in range(int(N/3)):
		s.add(Distinct([grid[r][c]
			for r in range(i*3,(i+1)*3)
			for c in range(j*3,(j+1)*3)]))

s.check()
model = s.model()

for r in range(N):
	if r != 0:
		print('-' * (4 * N - 3))
	print(' | '.join([str(model[c]) for c in grid[r]]))
