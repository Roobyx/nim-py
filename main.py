from operator import xor
import sys
import os
import re

currentPlayer = 1
playerVictory = False
gameRunning = True
board = [1,3,5,7]
aiMovesHistory = []
playerMovesHistory = []

def changePlayer():
	global currentPlayer

	if currentPlayer == 1:
		currentPlayer = 2
	else:
		currentPlayer = 1

def logLastMove(target):
	if(target == 'ai'):
		if(len(aiMovesHistory) > 0):
			print('\033[1;32;40m' + aiMovesHistory[-1])
			print('\033[1;37;40m')
	else:
		if(len(playerMovesHistory) > 0):
			print(playerMovesHistory[-1])

def isBalanced(board_to_check):
	balanced = (board_to_check[0] ^ board_to_check[1]) ^ (board_to_check[2] ^ board_to_check[3])
	
	if balanced == 0:
		return True
	else:
		return False

def drawGame(board_to_check):

	count = 1

	# Draw the board_to_check
	for el in board_to_check:
		print(count, ': ', end='')
		count = count + 1

		for _ in range(el):
			print(' O ', end='')
		print('')
	print('\n')
	
	# print('Balanced: ', isBalanced(board_to_check))

def getCorrectRow():
	row = int(input('--> Row to remove from: '))

	if not re.match('^[1-4]+$', str(row)):
		print("Error! We have 4 rows!")
		getCorrectRow()
	else:
		return row-1

def getCorrectAmount(row):
	amount = int(input('--> Amount to remove: '))
	
	if amount < 1 or amount > board[row]:
		print("Error! Illegal amount!")
		getCorrectAmount(row)
	else:
		print('Correct: ', amount)
		return amount


def remove():
	print('Player\'s turn!')
	row = getCorrectRow()
	amount = getCorrectAmount(row)

	board[row] -= amount or 0

	playerMovemessage = 'Player removed: ' + str(amount) + ' From row: ' + str(row)
	playerMovesHistory.append(playerMovemessage)
	drawGame(board)

def checkWin():
	global gameRunning

	for value in range(4):
		if board[value] > 0:
			changePlayer()
			return
	
	print('----------------------------')
	if(currentPlayer == 1):
		print('Player Won!')
	else:
		print('AI Won!')
	print('----------------------------')

	gameRunning = False

def aiMove():
	global board
	global playerVictory

	tempList = board.copy()
	foundBalanced = False
	rowTraversed = 0

	if(isBalanced(tempList)):
		# print('Stupid move needed')
		if(tempList[0]) > 0:
			tempList[0] -= 1
			board = tempList.copy()
			# print('Move made 1')

		elif(tempList[1] > 0):
			tempList[1] -= 1
			board = tempList.copy()
			# print('Move made 2')

		elif(tempList[2] > 0):
			tempList[2] -= 1
			board = tempList.copy()
			# print('Move made 3')

		elif(tempList[3] > 0):
			tempList[3] -= 1
			board = tempList.copy()
			# print('Move made 4')

		else:
			print('You won!')
			playerVictory = True
	else:
		# print('Balancing attempt')

		for row in range(4):
			amount = 0
			rowTraversed += 1
			if(tempList[row] > 0):
				for v in range(tempList[row]):
					tempList[row] -= 1
					amount += 1
					# print('Checking: ', tempList[0], tempList[1], tempList[2], tempList[3])

					if(isBalanced(tempList)):
						foundBalanced = True
						aiMoveMessave = 'AI removed: ' + str(amount) + ' From row: ' + str(rowTraversed)
						aiMovesHistory.append(aiMoveMessave)
						board = tempList.copy()
						# print('break 1')
						break
					# else:
						# print('Failed attempt')
						
					if(tempList[row] == 0):
						# Reseting row
						# print('Reseting row')
						tempList = board.copy()
						# print('Should be reset: ', tempList[0], tempList[1], tempList[2], tempList[3])
				if(foundBalanced):
					break

				amount = 0
	logLastMove('ai')

# Draw result board
# while gameRunning:
# 	drawGame(board)

# 	if(currentPlayer == 1):
# 		remove()
# 	else:
# 		# Clear old consonsole
# 		os.system('cls' if os.name == 'nt' else 'clear')
# 		aiMove()
	
# 	checkWin()

getCorrectAmount(1)