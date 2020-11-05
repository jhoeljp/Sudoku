#Sudoku solver -- Text based
import sys,os


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
    for i in range(x_1,y_1):
        for j in range(x_2,y_2):
            # print(board[i][j])
            if board[i][j] in total_options:
                total_options.remove(board[i][j])
    return total_options

def get_sides(board,pos_x,EDGE_1,EDGE_2):
    #check horizontal
    hor = board[pos_x][EDGE_1:EDGE_2]
    #check vertical
    ver = []
    for i in range(EDGE_2):
        # print("%d , %d --> %s"%(pos_x,i,board[pos_x][i]))
        ver.append(board[i][pos_x])
    return hor,ver

def check_sides(hor,ver,option):

    return True
def backtrack(squares,pos_x,pos_y):
    EDGE_1 = 0
    EDGE_2 = 9

    if pos_x ==9 and pos_y==9:
        return board
    #solve from top to bottom
    for key in squares.keys():
        if key == "1":
            options = []
            x_1, y_1, x_2, y_2 = squares[key]
            #options available for squares
            options = get_options(board,x_1,y_1,x_2,y_2)
            #check perpendicular sides - horizontal and vertical
            hor, ver = get_sides(board,pos_x,EDGE_1,EDGE_2)
            #exhast options 1 by 1 a.k.a backtrack to right sol
            for attempt in options:
                #if attempt not in hor or ver keep going
                valid = check_sides(hor,ver,attempt)

            #replace '0'

#backtracking solver
def solve(board):
    #square coordinates
    squares = {"1":(0,3,0,3),"2":(0,3,3,6),"3":(0,3,6,9),
    "4":(3,6,0,3),"5":(3,6,3,6),"6":(3,6,6,9),
    "7":(6,9,0,3),"8":(6,9,3,6),"9":(6,9,6,9)}

    new_board = backtrack(squares,0,0)


board = load_board("sudoku1.txt")
# print(board)
solve(board)
