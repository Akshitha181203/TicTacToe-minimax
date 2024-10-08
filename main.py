import sys
import numpy as np
import pygame

pygame.init()

#colours = {white, red, blue, green, black}
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Board Dimensions
HEIGHT = 300
WIDTH = 300
LINE_WIDTH = 5
COLOUMNS = 3
ROWS = 3
SQUARE_SIZE = HEIGHT // COLOUMNS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 10
CROSS_WIDTH = 15

#Screen Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BLACK)

# Screen Intialization
def Board_Lines(color = WHITE):
    for i in range(ROWS):
        pygame.draw.line(screen, color, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, color, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)

#player initialization
def Board_Players(color = WHITE):
    for i in range(ROWS):
        for j in range(COLOUMNS):
            if board[i][j] == 1:
                pygame.draw.circle(screen, color, (int(j * SQUARE_SIZE + SQUARE_SIZE / 2), int(i * SQUARE_SIZE + SQUARE_SIZE / 2)),CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[i][j] == 2:
                pygame.draw.line(screen, color, (j * SQUARE_SIZE + SQUARE_SIZE // 4, i * SQUARE_SIZE + SQUARE_SIZE // 4), (j * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, i * SQUARE_SIZE + 3 * SQUARE_SIZE // 4), CROSS_WIDTH)
                pygame.draw.line(screen, color, (j * SQUARE_SIZE + SQUARE_SIZE // 4, i * SQUARE_SIZE + 3 * SQUARE_SIZE // 4), (j * SQUARE_SIZE + 3 * SQUARE_SIZE // 4, i * SQUARE_SIZE + SQUARE_SIZE // 4), CROSS_WIDTH)


# Board initalization
board = np.zeros((ROWS, COLOUMNS))

def Mark_Player(row,col,player):
    board[row][col] = player

def is_square_available(row, col):
    return board[row][col] == 0

def is_board_full(cheack_board = board):
    for row in range(ROWS):
        for col in range(COLOUMNS):
            if cheack_board[row][col] == 0:
                return False
    return True

def Check_Win(player, cheack_board = board):
    for row in range(ROWS):
        if cheack_board[row][0] == player and cheack_board[row][1] == player and cheack_board[row][2] == player:
            return True

    for col in range(COLOUMNS):
        if cheack_board[0][col] == player and cheack_board[1][col] == player and cheack_board[2][col] == player:
            return True

    if cheack_board[0][0] == player and cheack_board[1][1] == player and cheack_board[2][2] == player:
        return True

    if cheack_board[0][2] == player and cheack_board[1][1] == player and cheack_board[2][0] == player:
        return True

    return False


# here the AI is contiouasly cheacking the board position and by simulating fake senarios for all possible moves of the computer(player == 2) and the player1's futer possible moves
def minimax(minimax_board, depth, is_maximizing):
    if Check_Win(2, minimax_board):
        return float('inf')

    elif Check_Win(1, minimax_board):
        return float('-inf')

    elif is_board_full(minimax_board):
        return 0

    if is_maximizing:
        best_score = -1000
        for row in range(ROWS):
            for col in range(COLOUMNS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax(minimax_board, depth + 1, False)
                    minimax_board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score

    else:
        best_score = 1000
        for row in range(ROWS):
            for col in range(COLOUMNS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax(minimax_board, depth + 1, True)
                    minimax_board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score

def Best_move():
    best_score = -1000
    move = (-1,-1)    # invalid move
    for row in range(ROWS):
        for col in range(COLOUMNS):
            if is_square_available(row, col):
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)
    
    if move != (-1,-1):
        Mark_Player(move[0], move[1], 2)
        return True
    return False

def Restart_game():
    screen.fill(BLACK)
    Board_Lines()
    for row in range(ROWS):
        for col in range(COLOUMNS):
            board[row][col] = 0

def display_results(message):
    Font = pygame.font.Font(None, 34)
    text = Font.render(message, True, BLACK)
    background_rect = pygame.Rect((WIDTH - text.get_width()) // 2 - 10, (HEIGHT - text.get_height()) // 2 - 10, text.get_width() + 20, text.get_height() + 20)
    pygame.draw.rect(screen, WHITE, background_rect)
    screen.blit(text, ((WIDTH - text.get_width()) // 2, (HEIGHT - text.get_height()) // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

Board_Lines()

player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // SQUARE_SIZE
            mouseY = event.pos[1] // SQUARE_SIZE

            if is_square_available(mouseY, mouseX):
                Mark_Player(mouseY, mouseX, player)
                if Check_Win(player):
                    game_over = True
                player = player % 2 + 1

                if not game_over:
                    if Best_move():
                        if Check_Win(2):
                            game_over = True
                        player = player % 2 + 1
                
                if not game_over:
                    if is_board_full():
                        game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                Restart_game()
                game_over = False
                player = 1

    if not game_over:
        Board_Players()
    else:
        if Check_Win(1):
            Board_Players(GREEN)
            Board_Lines(GREEN)
            display_results("Player wins!!!")

        elif Check_Win(2):
            Board_Players(RED)
            Board_Lines(RED)
            display_results("Computer wins!!!")

        elif is_board_full():
            Board_Players(BLUE)
            Board_Lines(BLUE)
            display_results("It's a tie!")

    pygame.display.update()