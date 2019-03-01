arr [row][col]
import random
import pprint
import time

def make_make(size, lvl):

    matrix = [[random.randint(0,10) for row in range(size)] for col in range(size)]

    for row in range(len(matrix)):
        for col in range(len(matrix)):

            if matrix[row][col] > lvl:
                matrix[row][col] = '.'
            else:
                matrix[row][col] = '!'

    matrix[0][0] = '.'
    matrix[1][0] = '.'
    matrix[0][1] = '.'
    matrix[-1][-1] = '.'
    matrix[-2][-1] = '.'
    matrix[-1][-2] = '.'

    return matrix



def maze_nav(matrix):

    row = 0
    col = 0
    maze = matrix
    maze[0][0] = '0'
    t0 = time.time()

    while maze[-1][-1] != '0' :

        pprint.pprint(maze)

        maze[row][col] = 'X'

        maze_dir = input('Right, Left, Up, Down?')

        if row and col == -1:
            print('you did it')


        elif maze_dir == 'Right':
            if maze[row][col+1] == '.':
                maze[row][col+1] = '0'
                col = col + 1

            elif maze[row][col+1] == '!':
                print('you lose')

        elif maze_dir == 'Left':
            if maze[row][col-1] == '.':
                maze[row][col-1] = '0'
                col = col - 1
            elif maze[row][col-1] == '!':
                print('you lose')

        elif maze_dir == 'Up':
            if maze[row-1][col] == '.':
                maze[row-1][col] = '0'
                row = row - 1
            elif maze[row-1][col] == '!':
                print('you lose')

        elif maze_dir == 'Down':
            if maze[row+1][col] == '.':
                maze[row+1][col] = '0'
                row = row + 1
            elif maze[row+1][col] == '!':
                print('you lose')


    maze[row][col] = 'X'
    maze[-1][-1] = 'X'
    pprint.pprint(maze)
    t1 = time.time()

    print("you did it in", t1-t0, "seconds" )


maze = make_make(5, 1)
maze_nav(maze)
