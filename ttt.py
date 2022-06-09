boardSize = 3
player_txt = ['bad player','\x1b[35mX\x1b[0m',
              '\x1b[34mO\x1b[0m']

def main():
    current_player = 1
    cc = get_colors()
    winner = False
    board = [[' '] * boardSize for i in range(boardSize)]
    while winner == False:
        draw_screen(board, boardSize, current_player)
        while True:
            move = fancy_input(f"Player {current_player}, enter your move: ")
            move -= 1 # Convert to 1-indexed
            if is_invalidate_move(board, move, current_player):
                continue
            else:
                break
        board[int(move / boardSize)][move % boardSize] = player_txt[current_player]
        winner = check_winner(board, boardSize)
        if winner == True:
            draw_screen(board, boardSize, current_player)
            print(f"{cc['r']}{cc['red']}Player {current_player} wins!{cc['r']}")
            break

        if current_player == 1:
            current_player = 2
        else:
            current_player = 1
    print("\n")
def is_invalidate_move(board, move, current_player):
    cc = get_colors()
    if move > boardSize * boardSize:
        print(f"{cc['r']}{cc['red']}Please enter a number between 1 and {boardSize * boardSize}")
        return True
    if board[int(move / boardSize)][move % boardSize] != ' ':
        print(f"{cc['r']}{cc['red']}That space is already taken")
        return True
    return False
def check_winner(board, boardSize):
    """ Check if there is a winner """
    for i in range(boardSize):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
    for i in range(boardSize):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False
    
def draw_screen(board, boardSize, current_player):
    cc = get_colors()
    print(cc['clear'], end="")
    print("Welcome to Tic Tac Toe!")
    print(f"Player {current_player}'s ({player_txt[current_player]}) turn")

    draw_board(board, boardSize)

def fancy_input(text_to_show):
    cc = get_colors()
    while True:
        # Show input prompt with no line ending
        print(f"{cc['r']}{cc['gry']}{text_to_show}{cc['u']}{cc['bwt']}", end="")
        value_input = input()
        print(cc['r'], end="")
        if value_input.isnumeric():
            return int(value_input)
        else:
            print(f"{cc['r']}{cc['red']}Please enter a number{cc['r']}")

def draw_board(board, boardSize):
    cc = get_colors()
    cnt = 0
    for i in range(boardSize):
        print(' ', end='')
        for j in range(boardSize):
            cnt += 1
            if board[i][j] == ' ':
                print(f"{cc['gry']}{cnt}{cc['r']}" , end='')
            else:
                print(board[i][j], end="")
            if j != boardSize - 1:
                print(f" {cc['bwt']}|{cc['r']} ", end="")
            else:
                print("")
        if i != boardSize - 1:
            print(f"{cc['bwt']}-{cc['r']}" * (boardSize * 3 + (boardSize - 1)))
def get_colors():
    """ Get the colors for the console """
    return {
        'r': '\x1b[0m', # reset
        'u': '\x1b[4m', # underline
        'clear':'\033c',# clear screen
        'white': '\x1b[37m',# white
        'gry': '\x1b[90m',# gray
        'red': '\x1b[31m',# red
        'grn': '\x1b[32m',# green
        'ylw': '\x1b[33m',# yellow
        'blu': '\x1b[34m',# blue
        'mgt': '\x1b[35m',# magenta
        'cyn': '\x1b[36m',# cyan
        'bwt': '\x1b[97m',
        }

def clear_console():
    print(cclr['clear'])
if __name__ == "__main__":
    main()
