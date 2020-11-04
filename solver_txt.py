#Sudoku solver -- Text based
import sys,os
#load txt sudoku
def load_board(file):
    path = os.path.isfile(os.getcwd() + '/' + file)

    if path:
        print("Loading Sudoku board from " + file)
        #read
        file = open(path,'r')
        pass
    else:
        print("Invalid path, no board in here! ")
        sys.exit()


board = load_board("sudoku1.txt")
