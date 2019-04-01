import pygame
import sys
import math
import Ai, board

BLUE = (0,0,200)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE =(255,255,255)
GRAY = (120,120,120)
ROW_COUNT = 6
COLUMN_COUNT = 7


game_board= board.board()

red_piece = pygame.image.load('smallred.png')
yellow_piece = pygame.image.load('smallyellow.png')

game_board.print_board()
game_over = False
turn = 0
player2 = Ai.AI_player(2, 1, True)

pygame.init()

PLAYER = 0
AI = 1

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
game_board.draw_board(screen)
pygame.display.update()

myfont = pygame.font.SysFont("comic sans ", 75)

while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, GRAY, (0,0, width, SQUARESIZE))

			posx = event.pos[0]
			if turn == 0:

				pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
				screen.blit(red_piece,(int(posx)-50,0))
			else: 
				pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, GRAY, (0,0, width, SQUARESIZE))

			# Ask for Player 1 Input
			if turn == 0:
				#cursor
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if game_board.is_valid_location(col):
					row = game_board.get_next_open_row( col)
					game_board.drop_piece( row, col, 1)

					if game_board.winning_move( 1):
						label = myfont.render("Player 1 wins!!", 1, RED)
						screen.blit(label, (40,10))
						game_over = True
					
					turn+=1 
					turn = turn % 2


					game_board.draw_board(screen)

			# # Ask for Player 2 Input
			if turn == 1:			
				posx = event.pos[0]
				player2.computer_turn(game_board,game_over)
				nextlvl = not player2.level
				

				if game_board.winning_move( player2.AI_PIECE):
					label = myfont.render("Computer wins!!", 1, YELLOW)
					screen.blit(label, (40,10))
					game_over = True

				game_board.print_board()
				game_board.draw_board(screen)

			turn += 1
			turn = turn % 2
	if game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		pygame.time.wait(9000)

			
				
