#Sudoku solver -- Text based
#Name: Jhoel Perez
#Date: 6/11/2020
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

def get_sides(board,pos_x,pos_y,EDGE_1,EDGE_2):
    #check horizontal
    hor = board[pos_x][EDGE_1:EDGE_2]
    #check vertical
    ver = []
    for i in range(EDGE_2):
        ver.append(board[i][pos_y])
    return hor,ver

def board_print(board):
    for line in board:
        print(line)

def options2(hor,ver):
    total_options = ['1','2','3','4','5','6','7','8','9']
    options = []
    for option in total_options:
        if (option not in ver) and (option not in hor) and option!='0':
            options.append(option)
    return options

def backtrack2(pos_x,pos_y,board):
    old_board = board
    EDGE_1 = 0
    EDGE_2 = 9
    EMPTY = '0'
    STEPS = []

    if pos_x ==8 and ('0' not in board[pos_x]):
        board_print(board)
        sys.exit()
    #solve from top to bottom & left to right
    for i in range(EDGE_2):
        for j in range(EDGE_2):

            #empty slot found
            if board[i][j] == '0':
                #try filling empty slot
                #check perpendicular sides - horizontal and vertical
                hor, ver = get_sides(board,i,j,EDGE_1,EDGE_2)
                #get possible options
                options = options2(hor,ver)

                #if empty and not available options, backtrack
                if options == []:
                    return False
                for opt in options:
                    #attempt to replace empty slot w/ possible options
                    board[i][j] = opt
                    #recurse to next
                    solved = backtrack2(i,j,board)
                    #undo bad step
                    board[i][j]= EMPTY
                    #remove wrong solution
                    options.remove(opt)

                    if options == []:
                        return False
    return True

#backtracking solver
def solve(board):
    new_board = backtrack2(0,0,board)


board = load_board("sudoku1.txt")
# print(board)
board = solve(board)
board_print(board)
