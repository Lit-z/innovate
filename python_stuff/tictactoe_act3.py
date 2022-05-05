import random

# starting menu where user picks a side covering multiple input errors or ways
# choosing a side
def start():
    global marker, ai_marker
    x = input('Pick a side: O or X (noughts or crosses) \n')
    x = x.lower()
    if x == 'x' or x == 'crosses':
        print('you picked X')
        marker = 'X'
        ai_marker = 'O'
    elif x == 'o' or x == '0' or x == 'noughts':
        print('you picked O')
        marker = 'O'
        ai_marker = 'X'
    else:
        print('not a valid side, please choose correctly')
        start()
    return marker, ai_marker

# user picks if they wish to go first, second or let the ai decide (random)
# covering multiple inputs
def turn():
    global player
    y= input('Do you wish to go first, second or random (1, 2 or r)? ').lower()
    if y == 'r' or y == 'rand' or y == 'random':
        y = random.randint(1,2)
    else:
        pass
    if y == '1st' or y == 'first' or y == '1' or y == 1:
        player = True
        print('\nYou will go first')
    elif y == '2nd' or y == 'second' or y == '2' or y == 2:
        player = False
        print('\nYou will go second')
    else:
        print('Please enter a correct value')
        turn()
    return player

# prints out visually the starting board and names (numbers) of the locations
# the input line gives this menu a pause so it gives the user chance to read it
# especially helpful when the ai is going first
def help(x,y):
    j = 1
    k = 2
    l = 3

    for i in range(3):
        if i < 2:
            print(f'{x} {j} | {k} | {l} \n{x+y}')
        else:
            print(f'{x} {j} | {k} | {l} \n{x}')
        j += 3
        k += 3
        l += 3
    print('Positions for selection are represented by the above layout')
    input('Press Enter to continue')

# the players turn with checks to ensure the position entered is valid
# and unoccupied, then it checks after the move if it would result in a win
# or draw, if so the game will end
def user_turn():
    move = 0
    move = input('Choose a position: ')
    while move.isdigit() == False: 
        move = input('Enter an correct position (1-9): ')
    move = int(move)
    if 1 <= move <= 9:
        move = move - 1
        if b[move] != ' ':
            print('That space is occupied')
            user_turn()
        else:
            b[move] = marker
            check_win(b, marker)
            if game_over == True:
                print('You won, mircales happen')
            else:
                check_draw()
    else:
        print("That's impossible position try a actual move")
        user_turn()

# calculates the ai turn, prior_move() is related to moves that result in a side
# winning, so it runs them checks first. Then it will pick randomly from the 
# corners, centre, remaining 4 spots in that order if these spots are empty
# if the ai plays a winning or the last (drawing) move the game will end
def ai_turn(m):
    moves = []
    copy = copy_board(b)
    prior_move(copy, ai_marker, b)
    if places != []:
        moves = places
    else:
        copy = copy_board(b)
        prior_move(copy, marker, b)
        if places != []:
            moves = places
        else:
            for i in ([0, 2, 6, 8]):
                if copy[i] != ' ':
                    pass
                else:
                    moves.append(i)
            if len(moves) == 0 and copy[4] == ' ':
                moves.append(4)
            else:
                pass
            if len(moves) == 0:
                for j in ([1, 3, 5, 7]):
                    if copy[j] != ' ':
                        pass
                    else:
                        moves.append(j)
            else:
                pass
    ai_move = random.choice(moves)
    b[ai_move] = m
    check_win(b, m)
    if game_over == True:
        print('haha, you lost')
    else:
        check_draw()

# the prior_move() first checks for if the ai can make a move that will win,
# if it finds out it returns this value to ai_turn()
# then it checks if there are any moves it can play to prevent a loss in the 
# next turn and again returns this value to ai_turn()
# if neither, it will go back to ai_turn where the random checks explained there
# are completed
def prior_move(copy, mark, board):
    global game_over, places
    places = []
    for i in range(0,9):
        if copy[i] == ' ':
            copy[i] = mark
            check_win(copy, mark)
            if game_over == True:
                places.append(i)
                game_over = False
                return game_over, places
            else:
                copy = copy_board(board)
        else:
            pass

# making a duplicate board for the ai to figure out it's move that
# won't modify the current board, gets used a lot in calculating priority moves
def copy_board(b):
    dupe_b = []
    for k in b:
        dupe_b.append(k)
    return dupe_b

# displays the current board with positions filled in, is shown after every turn
def current_board(x,y):
    print(f'{x} {b[0]} | {b[1]} | {b[2]} \n{x+y}')
    print(f'{x} {b[3]} | {b[4]} | {b[5]} \n{x+y}')
    print(f'{x} {b[6]} | {b[7]} | {b[8]} \n{x}')

# checking if the board is full therefore a draw
def check_draw():
    global game_over
    if ' ' not in b:
        game_over = True
        print("How boring, it's a draw")
        return game_over
    else:
        pass

# winning combos: 1,2,3 & 4,5,6 & 7,8,9 & 1,4,7 & 2,5,8 & 3,6,9 & 1,5,9 & 3,5,7
# as indexes: [0,1,2] [3,4,5] [6,7,8] [0,3,6] [1,4,7] [2,5,8] [0,4,8] [2,4,6]
def check_win(b, m):
    global game_over
    if (b[0] == m and b[1] == m and b[2] == m) or (         # top
        b[3] == m and b[4] == m and b[5] == m) or (         # mid across
        b[6] == m and b[7] == m and b[8] == m) or (         # bottom
        b[0] == m and b[3] == m and b[6] == m) or (         # left
        b[1] == m and b[4] == m and b[7] == m) or (         # mid down
        b[2] == m and b[5] == m and b[8] == m) or (         # right
        b[0] == m and b[4] == m and b[8] == m) or (         # diagonal
        b[2] == m and b[4] == m and b[6] == m):             # alt diagonal
        game_over = True
        return game_over
    else:
        pass

# variables set to defaults
game_over = False
b = [' '] * 9                       # b shorthand for board to minimise typing
x = '   |   |   \n'                 # used in making the picture of the board
y = '-----------'                   # likewise

# starts the game doing initial checks of what the user wants in terms of turn
# order or side picked, then displays the positions on the board
start()
turn()
help(x,y)

# runs the game accounting for the different order depending on who goes first
while game_over == False:
    if player == True:
        user_turn()
        current_board(x,y)
        if game_over == False:
            ai_turn(ai_marker)
            current_board(x,y)
        else:
            break
    else:
        ai_turn(ai_marker)
        current_board(x,y)
        if game_over == False:
            user_turn()
            current_board(x,y)
        else:
            break