#Sudoku solver -- Text based
import sys,os
import time

MAIN_BOARD = [[]]

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
    fn_board = board
    EDGE_1 = 0
    EDGE_2 = 9
    EMPTY = '0'
    STEPS = []

    if pos_x ==8 and (EMPTY not in board[pos_x]):
        fn_board = board
        raise SystemExit
        # sys.exit()
        # return board
        # return True
        # break
    #solve from top to bottom & left to right
    for i in range(EDGE_2):
        for j in range(EDGE_2):

            #empty slot found
            if board[i][j] == EMPTY:
                #try filling empty slot
                #check perpendicular sides - horizontal and vertical
                hor, ver = get_sides(board,i,j,EDGE_1,EDGE_2)
                #get possible options
                options = options2(hor,ver)

                #if empty and not available options, backtrack
                if options == []:
                    return board
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
                        return board
    return fn_board

#backtracking solver
def solve(board):
    new_board = backtrack2(0,0,board)
    board_print(new_board)
def main(new_board):
    # print(board)
    board = solve(new_board)
    board_print(board)
    print("Board is finally solved.")
    return board

try:
    OLD_board = load_board("sudoku1.txt")
    SOLVED_board = OLD_board
    SOLVED_board = main(SOLVED_board)
except SystemExit:
    board_print(SOLVED_board)
#end SOLVER

def approximate(pos):
    # Change the x/y screen coordinates to grid coordinates
    col = pos[0] // (WIDTH + MARGIN)
    row = pos[1] // (HEIGHT + MARGIN)
    old_row, old_col,draw = Sudoku_grid[col][row]
    #approximate inner cell coordinates to center
    new_row = old_row + ((WIDTH-MARGIN)/4)
    new_col = old_col + ((HEIGHT-MARGIN)/4)

    return new_row,new_col

def approximate_pos(pos):
    # Change the x/y screen coordinates to grid coordinates
    col = pos[0] // (WIDTH + MARGIN)
    row = pos[1] // (HEIGHT + MARGIN)

    return row,col

def draw(col,row,number,draw):
    if draw:
        font = pygame.font.SysFont(FONT, 30)
        text = font.render(str(number), True, (0, 0, 0))
        # DISPLAY.blit(text, (pos[0],pos[1]))
        DISPLAY.blit(text, (col,row))
        pygame.display.flip()
        pygame.display.update()

#GUI ----------------------------
#GUI imports
import pygame, sys
from pygame.locals import *

#global variables
WIDTH = 30
HEIGHT = 30
WINDOW_SIZE = [320,350]
N = 9
MARGIN = 5
Sudoku_grid = []
OLD_board = load_board("sudoku1.txt")

FONT = 'arial'

WHITE = (255, 255, 255)
BLACK = (0,0,0)

pygame.init()
DISPLAY = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku GUI")

#Sudoku board
DISPLAY.fill(BLACK)

for row in range(N):
    color = WHITE
    tmp_grid = []
    for col in range(N):
        Margin_1 =(MARGIN + WIDTH) * col + MARGIN
        Margin_2 = (MARGIN + HEIGHT) * row + MARGIN
        pygame.draw.rect(DISPLAY,
                         color,
                         [(MARGIN + WIDTH) * col + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT])
        # print("@(%d,%d) margins are %d till %d" % (row,col,Margin_1,Margin_2))
        # print("approximate @ %d,%d" %(grid_row,grid_col))

        tmp_grid.append((Margin_1,Margin_2,True))
    Sudoku_grid.append(tmp_grid)

#draw board start
for row in range(N):
    color = WHITE
    for col in range(N):
        if OLD_board[row][col] != '0':
            # Margin_1 =(MARGIN + WIDTH) * col + MARGIN
            Margin_1,Margin_2, can_draw = Sudoku_grid[row][col]
            # Margin_2 = (MARGIN + HEIGHT) * row + MARGIN
            # draw(grid_col,grid_row,OLD_board[row][col])
            # print(OLD_board[row][col])
            grid_row, grid_col = approximate([Margin_1,Margin_2])
            # print("%d %d" % (grid_row,grid_col))
            # font = pygame.font.SysFont('arial', 30)
            # text = font.render(str(OLD_board[row][col]), True, (0, 0, 0))
            # # DISPLAY.blit(text, (pos[0],pos[1]))
            # DISPLAY.blit(text, (grid_col,grid_row))
            draw(grid_col,grid_row,str(OLD_board[row][col]),can_draw)
            #update to not editable
            Sudoku_grid[row][col] = (Margin_1,Margin_2,False)

        # pygame.display.flip()
        # pygame.display.update()

#main game loop
while True:
    for event in pygame.event.get():
        #QUIT
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #try sudoku option
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks
            pos = pygame.mouse.get_pos()
            new_row, new_col = approximate_pos(pos)
            #get draw boolean
            print("Click ", pos, "Grid coordinates: ", new_row, new_col)
            margin1, margin2, can_draw = Sudoku_grid[new_row][new_col]


            #draw number
            if can_draw:
                draw(margin1,margin2,str(1),can_draw)
            # font = pygame.font.SysFont('arial', 30)
            # text = font.render(str(1), True, (0, 0, 0))
            # # DISPLAY.blit(text, (pos[0],pos[1]))
            # DISPLAY.blit(text, (new_col,new_row))
            #
            # pygame.display.update()

            # Blit everything to the screen
            # DISPLAY.blit(background, (0, 0))
            # pygame.display.flip()

    # Blit everything to the screen
    # DISPLAY.blit(background, (0, 0))
    # pygame.display.flip()

    # DISPLAY.blit(background, (0, 0))
    pygame.display.flip()
    pygame.display.update()
