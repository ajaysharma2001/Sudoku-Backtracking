import math
import tkinter as tk
from time import sleep


def isfull (board):
	for lst in board:
		for val in lst:
			if val == 0:
				return False
	return True

def getColList (board, col):
	lst = []
	for row in xrange(0,9):
		if board[row][col] != 0:
			lst.append(board[row][col])
	return lst

def getRowList (board, row):
	lst = []
	for col in xrange(0,9):
		if board[row][col] != 0:
			lst.append(board[row][col])
	return lst

def notPossibleRowColVal(rowList, colList):
	lst = rowList
	for val in colList:
		if val not in lst:
			lst.append(val)
	return lst

def notPossibleSubGridVal (board, row, col):
	lst = []
	rowMax = int((math.ceil(float(row + 1)/3) * 3) - 1)
	rowMin = int(float(row)//3 * 3)
	colMax = int((math.ceil(float(col + 1)/3) * 3) - 1)
	colMin = int(float(col)//3 * 3)
	for row in xrange(rowMin,rowMax + 1):
		for col in xrange(colMin,colMax + 1):
			if board[row][col] != 0:
				lst.append(board[row][col])
	return lst


def possibleVal (board, row, col):
	subGridVal = notPossibleSubGridVal(board, row, col)
	rowColVal = notPossibleRowColVal(getRowList (board, row), getColList (board, col))
	lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	for val in subGridVal:
		lst.remove(val)
	for val in rowColVal:
		if val in lst:
			lst.remove(val)
	lst.sort()
	return lst

grid = [[0, 2, 0, 0, 0, 4, 3, 0, 0],
		[9, 0, 0, 0, 2, 0, 0, 0, 8],
		[0, 0, 0, 6, 0, 9, 0, 5, 2],
		[0, 0, 0, 0, 0, 0, 0, 0, 1],
		[0, 7, 2, 5, 0, 3, 6, 8, 0],
		[6, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 8, 0, 2, 0, 5, 0, 0, 0],
		[1, 0, 0, 0, 9, 0, 0, 0, 3],
		[0, 0, 9, 8, 0, 0, 0, 6, 0]]



print(possibleVal(grid, 4, 4))
#print(notPossibleSubGridVal(grid, 0, 0))
#print(notPossibleRowColVal(getRowList(grid, 0), getColList(grid, 0)))
#print(possibleVal(grid, 0, 8))
solvedGrid = [2]
def solveGrid (board):
	if isfull(board):
		solvedGrid = board
		print(board)
	else:
		row = -1
		col = -1
		for i in xrange(0,9):
			for j in xrange(0,9):
				if board[i][j] == 0:
					row = i
					col = j
					break
			if (row != -1 and col != -1):
				break
		possibleMoves = possibleVal(grid, row, col)

		for possibilies in possibleMoves:
			board[row][col] = possibilies
			solveGrid(board)
		board[row][col] = 0
	
gridLabels = []
solveGrid(grid)
#print(solvedGrid)



def create_grid(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    #c.delete('grid_line') # Will only remove the grid_line


    # Creates all vertical lines at intevals of 70
    for i in range(0, w, 70):
        c.create_line([(i, 0), (i, h)], tag='grid_line', width = 3 if i % 3 == 0 else 1)

    # Creates all horizontal lines at intevals of 70
    for i in range(0, h, 70):
        c.create_line([(0, i), (w, i)], tag='grid_line', width = 3 if i % 3 == 0 else 1)

    draw_num(grid)


	
def draw_num(board):
	for x in range(0, 9):     	
		for y in range (0, 9):     		
			gridLabels.append(c.create_text(x * 70 + 35,y * 70 +35,fill="darkblue",font="Times 20 italic bold",                         
				text= str(board[y][x]) if board[x][y] != 0 else "", tag = 'num'))
	

def del_num():
	for i in gridLabels:
		c.delete('num')



def update(sol):
	pass
	#print(sol)
	#draw_num(sol)



root = tk.Tk()

c = tk.Canvas(root, height=625, width=625, bg='white')
c.pack(fill=tk.BOTH, expand=True)

c.bind('<Configure>', create_grid)
root.after(1000, update, grid)

root.resizable(False, False)

root.mainloop()


 		 