
import math
import board
import random
import copy


EMPTY = 0
TARGET = 4


class AI_player:

    def __init__(self, ai_piece, opp_piece, current_level):
        self.AI_PIECE = ai_piece
        self.PLAYER_PIECE = opp_piece
        self.level = current_level

    def set_level(self, level):
        self.level = level

    # checks the given set for possible wins and scores options
    def score_move_set(self, set, piece):
        score = 0
        opp_piece = self.PLAYER_PIECE
        if piece == self.PLAYER_PIECE:
            opp_piece = self.AI_PIECE
        if set.count(opp_piece) == 4:
            score += 100
        elif set.count(opp_piece) == 3 and set.count(EMPTY) == 1:
            score += 8
        elif set.count(opp_piece) == 2  and set.count(EMPTY) == 2:
            score += 4
        elif set.count(opp_piece) == 1 and  set.count(EMPTY) == 3:
            score -= 8
        return score

    # this generates all moves available to the AI
    def get_move_set(self,  board, piece):
        score = 0
        center = [int(i) for i in list(board.board[:, board.COLUMN_COUNT//2])]
        center_count = center.count(piece)
        score += center_count * 3

        # horizontal
        for r in range(board.ROW_COUNT):
            row_array = [int(i) for i in list(board.board[r, :])]
            for c in range(board.COLUMN_COUNT -3):
                window = row_array[c:c+TARGET]
                score += self.score_move_set(window, piece)

        # vertical
        for c in range(board.COLUMN_COUNT):
            col_array = [int(i) for i in list(board.board[:, c])]
            for r in range(board.ROW_COUNT - 3):
                window = col_array[r:r + TARGET]
                score += self.score_move_set(window, piece)
        # postitive slope
        for r in range(board.ROW_COUNT - 3):
            for c in range(board.COLUMN_COUNT - 3):
                window = [board.board[r + i][c + i] for i in range(TARGET)]
                score += self.score_move_set(window, piece)
        # negative slope
        for r in range(board.ROW_COUNT - 3):
            for c in range(board.COLUMN_COUNT - 3):
                window = [board.board[r + 3 - i][c + i] for i in range(TARGET)]
                score += self.score_move_set(window, piece)
        return score

    # find game ending nodes

    def terminal_node(self, board: board):
        return board.winning_move(self.PLAYER_PIECE) or board.winning_move(self.AI_PIECE) or len(self.get_valid_locations(board)) == 0

    def get_valid_locations(self, board: board):
        valid_locations = []
        for col in range(board.COLUMN_COUNT):
            if board.is_valid_location( col):
                valid_locations.append(col)
        return valid_locations
        
    #minimax descion
    def minimax(self, board: board, depth, alpha, beta, maximizingPlayer):
        valid_locations = self.get_valid_locations(board)
        is_terminal = self.terminal_node(board)
        if depth == 0 or is_terminal:
            if is_terminal:
                if board.winning_move( self.AI_PIECE):
                    return (None, 100000000000000)
                elif board.winning_move( self.PLAYER_PIECE):
                    return (None, -10000000000000)
                else:  # Game is over, no more valid moves
                    return (None, 0)
            else:  # Depth is zero
                return (None, self.get_move_set(board, self.AI_PIECE))
        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = board.get_next_open_row( col)
                b_copy = copy.deepcopy(board)
                
                b_copy.drop_piece( row, col, self.AI_PIECE)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else:  # Minimizing player
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = board.get_next_open_row( col)
                b_copy = copy.deepcopy(board)
                b_copy.drop_piece(row, col, self.PLAYER_PIECE)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    #make move
    def computer_turn(self, board: board, gameover):
        col, minimax_score = self.minimax(board, 5, -math.inf, math.inf, self.level)

        if not gameover:
            if board.is_valid_location( col):
                #pygame.time.wait(500)
                row = board.get_next_open_row(col)
                board.drop_piece( row, col, self.AI_PIECE)

        



