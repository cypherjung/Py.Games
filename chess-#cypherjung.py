#chess
# Chess board initialization
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

# Function to print the board
def print_board(board):
    for row in board:
        print(' '.join(row))

# Function to check if the move is valid
def is_valid_move(move):
    if len(move) != 4:
        return False

    file1, rank1, file2, rank2 = move
    if file1 not in 'abcdefgh' or rank1 not in '12345678' or file2 not in 'abcdefgh' or rank2 not in '12345678':
        return False

    piece = board[8 - int(rank1)][ord(file1) - ord('a')]

    if piece == '.':
        return False

    if piece.isupper() != len(board) % 2 == 0:
        return False

    return True

# Function to check if the move is a valid capture
def is_valid_capture(move):
    file1, rank1, file2, rank2 = move
    piece1 = board[8 - int(rank1)][ord(file1) - ord('a')]
    piece2 = board[8 - int(rank2)][ord(file2) - ord('a')]

    if piece2 == '.':
        return False

    if piece1.isupper() == piece2.isupper():
        return False

    return True

# Function to check if the move is a valid pawn move
def is_valid_pawn_move(move):
    file1, rank1, file2, rank2 = move
    piece = board[8 - int(rank1)][ord(file1) - ord('a')]
    direction = -1 if piece.islower() else 1

    if rank2 == str(int(rank1) + direction) and file2 == file1 and board[8 - int(rank2)][ord(file2) - ord('a')] == '.':
        return True

    if rank2 == str(int(rank1) + 2 * direction) and rank1 in '27' and file2 == file1 and board[8 - int(rank2)][ord(file2) - ord('a')] == '.':
        return True

    if rank2 == str(int(rank1) + direction) and abs(ord(file2) - ord(file1)) == 1 and is_valid_capture(move):
        return True

    return False

# Function to check if the move is a valid knight move
def is_valid_knight_move(move):
    file1, rank1, file2, rank2 = move
    file_diff = abs(ord(file2) - ord(file1))
    rank_diff = abs(int(rank2) - int(rank1))
    return file_diff + rank_diff == 3 and file_diff > 0 and rank_diff > 0

# Function to check if the move is a valid bishop move
def is_valid_bishop_move(move):
    file1, rank1, file2, rank2 = move
    file_diff = abs(ord(file2) - ord(file1))
    rank_diff = abs(int(rank2) - int(rank1))
    return file_diff == rank_diff and file_diff > 0

# Function to check if the move is a valid rook move
def is_valid_rook_move(move):
    file1, rank1, file2, rank2 = move
    return file1 == file2 or rank1 == rank2

# Function to check if the move is a valid queen move
def is_valid_queen_move(move):
    return is_valid_bishop_move(move) or is_valid_rook_move(move)

# Function to check if the move is a valid king move
def is_valid_king_move(move):
    file1, rank1, file2, rank2 = move
    file_diff = abs(ord(file2) - ord(file1))
    rank_diff = abs(int(rank2) - int(rank1))
    return file_diff <= 1 and rank_diff <= 1

# Function to make a move
def make_move(move):
    file1, rank1, file2, rank2 = move
    piece = board[8 - int(rank1)][ord(file1) - ord('a')]
    board[8 - int(rank1)][ord(file1) - ord('a')] = '.'
    board[8 - int(rank2)][ord(file2) - ord('a')] = piece

# Function to check if a player is in check
def is_check(player):
    king = 'k' if player == 'Black' else 'K'
    opponent = 'White' if player == 'Black' else 'Black'

    for rank in range(8):
        for file in range(8):
            if board[rank][file] == king:
                king_file = chr(file + ord('a'))
                king_rank = str(8 - rank)

                for rank2 in range(8):
                    for file2 in range(8):
                        if board[rank2][file2].isupper() == (player == 'Black'):
                            piece_file = chr(file2 + ord('a'))
                            piece_rank = str(8 - rank2)
                            move = f"{piece_file}{piece_rank}{king_file}{king_rank}"

                            if is_valid_move(move) and is_valid_capture(move):
                                return True

                            if board[rank2][file2].lower() == 'p':
                                pawn_moves = [(file2 - 1, rank2 - 1), (file2 + 1, rank2 - 1)]
                                for pawn_file, pawn_rank in pawn_moves:
                                    if pawn_file >= 0 and pawn_file < 8 and pawn_rank >= 0 and pawn_rank < 8:
                                        move = f"{chr(file2 + ord('a'))}{str(8 - rank2)}{chr(pawn_file + ord('a'))}{str(8 - pawn_rank)}"
                                        if is_valid_move(move) and is_valid_capture(move):
                                            return True

    return False

# Function to check if a player is in checkmate
def is_checkmate(player):
    moves = generate_all_moves(player)

    for move in moves:
        if not is_check_after_move(player, move):
            return False

    return True

# Function to generate all possible moves for a player
def generate_all_moves(player):
    moves = []

    for rank1 in range(8):
        for file1 in range(8):
            piece = board[rank1][file1]

            if piece.isupper() == (player == 'White'):
                for rank2 in range(8):
                    for file2 in range(8):
                        move = f"{chr(file1 + ord('a'))}{str(8 - rank1)}{chr(file2 + ord('a'))}{str(8 - rank2)}"

                        if is_valid_move(move) and is_valid_capture(move):
                            moves.append(move)

    return moves

# Function to check if a player is in check after a move
def is_check_after_move(player, move):
    file1, rank1, file2, rank2 = move
    piece = board[8 - int(rank1)][ord(file1) - ord('a')]
    target = board[8 - int(rank2)][ord(file2) - ord('a')]

    board[8 - int(rank1)][ord(file1) - ord('a')] = '.'
    board[8 - int(rank2)][ord(file2) - ord('a')] = piece

    result = is_check(player)

    board[8 - int(rank1)][ord(file1) - ord('a')] = piece
    board[8 - int(rank2)][ord(file2) - ord('a')] = target

    return result

# Main game loop
while True:
    print_board(board)
    player = 'White' if len(board) % 2 == 0 else 'Black'
    move = input(f"{player}'s move: ")

    if move == 'quit':
        break

    if not is_valid_move(move):
        print('Invalid move. Try again.')
        continue

    if not is_valid_capture(move) and not is_valid_pawn_move(move) and not is_valid_knight_move(move) and not is_valid_bishop_move(move) and not is_valid_rook_move(move) and not is_valid_queen_move(move) and not is_valid_king_move(move):
        print('Invalid move. Try again.')
        continue

    if is_check(player) and not is_check_after_move(player, move):
        print('You cannot move your king into check. Try again.')
        continue

    make_move(move)

    if is_checkmate(player):
        print('Checkmate!')
        break

# End of the game
print('Game over.')
print("Thank you for playing")
exit()
