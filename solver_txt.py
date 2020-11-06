#Sudoku solver -- Text based
import sys,os
import time

#load txt sudoku
def load_board(file):
    path = os.path.isfile(os.getcwd() + '/' + file)
    board = []
    if path:
        print("Loading Sudoku board from " + file)
        #read
        file = open(file)
        for line in file.readlines():
            #clean
            # print(line)
            tmp_line = line[:-1].split(',')
            # print(tmp_line)
            tmp_line = [x for x in tmp_line if x.isnumeric()]
            board.append(tmp_line)

        file.close()
        return board
        # pass
    else:
        print("Invalid path, no board in here! ")
        sys.exit()

#get ints on current square
def get_options(board,x_1,y_1,x_2,y_2):
    # print(x_1,y_1,x_2,y_2)
    total_options = ['1','2','3','4','5','6','7','8','9']
    empty_slots = []
    for i in range(x_1,y_1):
        for j in range(x_2,y_2):
            # print(board[i][j])
            if board[i][j] in total_options:
                total_options.remove(board[i][j])
            #record empty location coordinates
            if board[i][j] == '0':
                empty_slots.append((i,j))
    return total_options,empty_slots

def get_sides(board,pos_x,pos_y,EDGE_1,EDGE_2):
    #check horizontal
    hor = board[pos_x][EDGE_1:EDGE_2]
    #check vertical
    ver = []
    for i in range(EDGE_2):
        # print("%d , %d --> %s"%(pos_x,i,board[pos_x][i]))
        # print("board [%d][%d]" %(i,pos_y))
        ver.append(board[i][pos_y])
    return hor,ver

def board_print(board):
    for line in board:
        print(line)

# def backtrack(squares,pos_x,pos_y,board):
#     EDGE_1 = 0
#     EDGE_2 = 9
#     EMPTY = '0'
#
#     if pos_x ==8 and pos_y==8:
#         return board
#     #solve from top to bottom
#     for key in squares.keys():
#         # if key == "1":
#         options = []
#         empty = []
#
#         x_1, y_1, x_2, y_2 = squares[key]
#         #options available for squares
#         options,empty = get_options(board,x_1,y_1,x_2,y_2)
#         # print(options)
#         #exhast options 1 by 1 a.k.a backtrack to right sol
#         for x_coor,y_coor in empty:
#             # print("(%s,%s)"%(x_coor,y_coor))
#             #check perpendicular sides - horizontal and vertical
#             hor, ver = get_sides(board,x_coor,y_coor,EDGE_1,EDGE_2)
#             #chose empty slot and replace with available option
#             for opt in options:
#                 if (opt not in hor) and (opt not in ver):
#                     board[x_coor][y_coor]=opt
#                     print("option %s @ (%s,%s)" %(opt,x_coor,y_coor))
#                     print(hor)
#                     print(ver)
#                     print("-----------")
#                     # time.sleep(10)
#                     board_print(board)
#                     #recurse to next
#                     backtrack(squares,x_coor,y_coor,board)
#                     #try next option if recursion returns
#                     board[x_coor][y_coor]= EMPTY
#
#             # for attempt in options:
#             #     #if attempt not in hor or ver keep going
#             #     valid = check_sides(hor,ver,attempt)
#
#             #replace '0'
#     return board

def options2(hor,ver):
    total_options = ['1','2','3','4','5','6','7','8','9']
    options = []
    for option in total_options:
        if (option not in ver) and (option not in hor) and option!='0':
            options.append(option)
    return options

def backtrack2(squares,pos_x,pos_y,board):
    old_board = board
    EDGE_1 = 0
    EDGE_2 = 9
    EMPTY = '0'
    STEPS = []

    if pos_x ==8 and pos_y==8:
        return board
    #solve from top to bottom & left to right
    for i in range(EDGE_2):
        if i == 0:
            i = pos_x
        for j in range(EDGE_2):
            if j == 0:
                j=pos_y

            #empty slot found
            if board[i][j] == '0':
                #try filling empty slot
                #check perpendicular sides - horizontal and vertical
                hor, ver = get_sides(board,i,j,EDGE_1,EDGE_2)
                #get possible options
                options = options2(hor,ver)
                # print(options)

                #if empty and not available options, backtrack
                if options == []:
                    # print("No options available for (%d,%d)" %(i,j))
                    # last_i, last_j = STEPS.pop()
                    return False
                for opt in options:
                    #attempt to replace empty slot w/ possible options
                    board[i][j] = opt
                    # print(options)
                    # print("option %s @ (%s,%s)" %(opt,i,j))
                    # board_print(board)
                    # time.sleep(10)

                    #recurse to next
                    # STEPS.append((i,j))
                    solved = backtrack2(squares,i,j,board)
                    #undo bad step
                    print("Back @ (%d,%d)" % (i,j))
                    board[i][j]= EMPTY
                    #remove wrong solution
                    options.remove(opt)

                    if options == []:
                        # print("No options available for (%d,%d)" %(i,j))
                        # last_i, last_j = STEPS.pop()
                        return False

    return True

#backtracking solver
def solve(board):
    #square coordinates
    squares = {"1":(0,3,0,3),"2":(0,3,3,6),"3":(0,3,6,9),
    "4":(3,6,0,3),"5":(3,6,3,6),"6":(3,6,6,9),
    "7":(6,9,0,3),"8":(6,9,3,6),"9":(6,9,6,9)}

    new_board = backtrack2(squares,0,0,board)


board = load_board("sudoku1.txt")
# print(board)
board = solve(board)
board_print(board)
