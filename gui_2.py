
#GUI imports
import pygame, sys
from pygame.locals import *


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
        board_print(board)
        # raise Exception("BOARD SOLVED ! ")
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
    return board

#backtracking solver
def solve(board):
    new_board = backtrack2(0,0,board)
    board_print(new_board)
def main():
    board = load_board("sudoku1.txt")
    # print(board)
    board = solve(board)
    board_print(board)
    return board

try:
    MAIN_BOARD = main()
except SystemExit:
    board_print(MAIN_BOARD)
#end SOLVER

#GUI ----------------------------
WIDTH = 30
HEIGHT = 30
WINDOW_SIZE = [320,320]
Sudoku_N = 9
MARGIN = 5

WHITE = (255, 255, 255)
BLACK = (0,0,0)

pygame.init()
DISPLAY = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku UU")

background = pygame.Surface(DISPLAY.get_size())
background = background.convert()
background.fill((250, 250, 250))

#main loop gmae
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
        #     # # Set that location to one
        #     # grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
        #
        # # elif event.type == pygame.MOUSEBUTTONUP:
        #     font = pygame.font.SysFont('arial', 50)
        #     text = font.render(str(9), True, (0, 0, 0))
        #     DISPLAY.window.blit(text, pos)
        #     pygame.display.update()

            font = pygame.font.SysFont('arial', 36)
            text = font.render("9", 1, (150, 150, 150))
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            background.blit(text, textpos)

            # Blit everything to the screen
            DISPLAY.blit(background, (0, 0))
            pygame.display.flip()

    # Blit everything to the screen
    DISPLAY.blit(background, (0, 0))
    pygame.display.flip()

    #sudoku board
    DISPLAY.fill(BLACK)

    for row in range(Sudoku_N):
        color = WHITE
        for col in range(Sudoku_N):
            pygame.draw.rect(DISPLAY,
                             color,
                             [(MARGIN + WIDTH) * col + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    DISPLAY.blit(background, (0, 0))
    pygame.display.flip()
    pygame.display.update()
