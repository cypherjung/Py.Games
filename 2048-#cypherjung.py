#2048
import random

# Board dimensions
BOARD_SIZE = 4

# Empty tile value
EMPTY_TILE = 0

# Directions
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# Initialize the board
def initialize_board():
    board = [[EMPTY_TILE] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    return board

# Add a new random tile to the board
def add_new_tile(board):
    empty_tiles = []
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == EMPTY_TILE:
                empty_tiles.append((i, j))
    if empty_tiles:
        row, col = random.choice(empty_tiles)
        board[row][col] = 2 if random.random() < 0.9 else 4

# Check if the board is full
def is_board_full(board):
    for row in board:
        if EMPTY_TILE in row:
            return False
    return True

# Check if the game is over (no more moves possible)
def is_game_over(board):
    for direction in [UP, DOWN, LEFT, RIGHT]:
        if can_move(board, direction):
            return False
    return True

# Rotate the board 90 degrees clockwise
def rotate_board(board):
    return [list(reversed(col)) for col in zip(*board)]

# Move the tiles in the board in the specified direction
def move(board, direction):
    if direction == UP:
        board = rotate_board(board)
        board = move_left(board)
        board = rotate_board(board)
    elif direction == DOWN:
        board = rotate_board(board)
        board = move_right(board)
        board = rotate_board(board)
    elif direction == LEFT:
        board = move_left(board)
    elif direction == RIGHT:
        board = move_right(board)
    return board

# Move the tiles to the left
def move_left(board):
    new_board = []
    for row in board:
        new_row = merge_tiles(row)
        new_board.append(new_row)
    return new_board

# Move the tiles to the right
def move_right(board):
    new_board = []
    for row in board:
        new_row = merge_tiles(list(reversed(row)))
        new_board.append(list(reversed(new_row)))
    return new_board

# Merge the tiles in a row
def merge_tiles(row):
    new_row = [tile for tile in row if tile != EMPTY_TILE]
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = EMPTY_TILE
    new_row = [tile for tile in new_row if tile != EMPTY_TILE]
    new_row += [EMPTY_TILE] * (len(row) - len(new_row))
    return new_row

# Check if a move is valid
def can_move(board, direction):
    if direction == UP:
        board = rotate_board(board)
        result = can_move_left(board)
        board = rotate_board(board)
        return result
    elif direction == DOWN:
        board = rotate_board(board)
        result = can_move_right(board)
        board = rotate_board(board)
        return result
    elif direction == LEFT:
        return can_move_left(board)
    elif direction == RIGHT:
        return can_move_right(board)

# Check if a move to the left is valid
def can_move_left(board):
    for row in board:
        if EMPTY_TILE in row:
            return True
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                return True
    return False

# Check if a move to the right is valid
def can_move_right(board):
    return can_move_left([list(reversed(row)) for row in board])

# Print the board
def print_board(board):
    for row in board:
        print(row)
    print()

# Play the game
def play_game():
    board = initialize_board()
    add_new_tile(board)
    add_new_tile(board)
    print_board(board)

    while True:
        direction = input("Enter a direction (up/down/left/right): ").lower()
        if direction not in [UP, DOWN, LEFT, RIGHT]:
            print("Invalid direction. Please try again.")
            continue
        
        if can_move(board, direction):
            board = move(board, direction)
            add_new_tile(board)
            print_board(board)
            
            if is_game_over(board):
                print("Game over!")
                break
        else:
            print("Invalid move. Please try again.")

# Start the game
play_game()
exit()
