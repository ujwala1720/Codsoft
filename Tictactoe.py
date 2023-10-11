
board = [' ' for _ in range(9)]


def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], '|', board[i + 1], '|', board[i + 2])
        if i < 6:
            print('-' * 9)


def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False


def is_full(board):
    return ' ' not in board


def minimax(board, depth, is_maximizing):
  
    if check_win(board, 'X'):
        return -1
    if check_win(board, 'O'):
        return 1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score


def make_best_move(board):
    best_move = -1
    best_score = -float('inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move


while True:
    print_board(board)
    player_move = int(input("Enter your move (0-8): "))
    if board[player_move] == ' ':
        board[player_move] = 'X'
        if check_win(board, 'X'):
            print_board(board)
            print("You win! Congratulations!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        ai_move = make_best_move(board)
        board[ai_move] = 'O'
        if check_win(board, 'O'):
            print_board(board)
            print("AI wins! .")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
    else:
        print("That position is already taken. Try again.")


   
