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
            tmp_line = line[:-2].split(',')
            tmp_line = [x for x in tmp_line if x.isnumeric()]
            board.append(tmp_line)

        file.close()
        return board
        # pass
    else:
        print("Invalid path, no board in here! ")
        sys.exit()


board = load_board("sudoku1.txt")
print(board)
