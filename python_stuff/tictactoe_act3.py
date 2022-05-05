import random

# starting menu where user picks a side 
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

# user picks if they wish to go first or second
def turn():
    global player
    y= input('Do you wish to go first? (Y/N)').lower()
    if y == 'yes' or y == 'y' or y == '1st' or y == 'first' or y == '1':
        player = True
        print('You will go first')
    elif y == 'no' or y == 'n' or y == '2nd' or y == 'second' or y == '2':
        player = False
        print('You will go second')
    else:
        print('Enter a correct value')
        turn()
    return player

# prints out visually the starting board and names (numbers) of the locations
# on the board, will be callable as a help menu
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
    print('positions for selection are represented by the above layout')

# the players turn
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

# calculates the ai turn, currently just picks corners, mid then rest randomly
# if they are empty, need to add to it to check if it can win/ lose next go
def ai_turn(m):
    moves = []
    copy = copy_board(b)
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
    print(moves)
    ai_move = random.choice(moves)
    b[ai_move] = m
    check_win(b, m)
    if game_over == True:
        print('haha, you lost')
    else:
        check_draw()

# making a duplicate board for the ai to figure out it's move that
# won't modify the current board
def copy_board(b):
    dupe_b = []
    for k in b:
        dupe_b.append(k)
    return dupe_b

# displays the current board
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

# some needed variables set to defaults
game_over = False
b = [' '] * 9                       # b shorthand for board to minimise typing
x = '   |   |   \n'
y = '-----------'
start()
turn()
help(x,y)

# run the game
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




