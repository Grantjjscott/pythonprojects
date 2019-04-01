import numpy as np
import pygame
import sys
import math


BLUE = (0,0,200)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
GRAY =(125,125,125)


SQUARESIZE = 100


RADIUS = int(SQUARESIZE/2 - 5)
ROW_COUNT = 6
COLUMN_COUNT = 7
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
board_size = (ROW_COUNT*SQUARESIZE)
size = (width, height)

red_piece = pygame.image.load('smallred.png')
yellow_piece = pygame.image.load('smallyellow.png')
class board:
	ROW_COUNT = 6
	COLUMN_COUNT = 7
	def __init__(self, ):
		self.board= np.zeros((ROW_COUNT,COLUMN_COUNT))
       



	def drop_piece(self,row, col, piece):
	    self.board[row][col] = piece

	def is_valid_location(self, col):
	    return self.board[ROW_COUNT-1][col] == 0

	def get_next_open_row(self, col):
	    for r in range(ROW_COUNT):
		    if self.board[r][col] == 0:
			    return r

	def print_board(self,):
	    print(np.flip(self.board, 0))
	



	def winning_move(self, piece):
	    # Check horizontal locations for win
	    for c in range(COLUMN_COUNT-3):
		    for r in range(ROW_COUNT):
			    if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
				    return True

	# Check vertical locations for win
	    for c in range(COLUMN_COUNT):
		    for r in range(ROW_COUNT-3):
			    if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
				    return True

	# Check positively sloped diaganols
	    for c in range(COLUMN_COUNT-3):
		    for r in range(ROW_COUNT-3):
			    if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
				    return True

	# Check negatively sloped diaganols
	    for c in range(COLUMN_COUNT-3):
		    for r in range(3, ROW_COUNT):
			    if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
				    return True

	def draw_board(self, screen):
		for c in range(COLUMN_COUNT):
			for r in range(ROW_COUNT):
				pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
				pygame.draw.circle(screen, GRAY, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
		for c in range(COLUMN_COUNT):
			for r in range(ROW_COUNT):
				if self.board[r][c] == 1:
					#aw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
					screen.blit(red_piece, ((int(c * SQUARESIZE), (board_size -r*SQUARESIZE ))))
				elif self.board[r][c] == 2:
					#pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE), height-int(r*SQUARESIZE+SQUARESIZE)), RADIUS)
					screen.blit(yellow_piece, ((int(c * SQUARESIZE), (board_size - r*SQUARESIZE ))))
		pygame.display.update()


