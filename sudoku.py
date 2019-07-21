# sudoku
# source of ideas :
# https://www.rharriso.com/generating-sudoku-boards-pt-1-structures.html?source=post_page---------------------------

#One effective strategy is to look at each cell in turn and then try to eliminate possible numbers. The more neighbors (which I define as cells that are in the same row, column, or block) that a cell has filled in the fewer possibility options that cell has. If a cell only has one valid possible move, is can be filled. As cells get filled it’s neighbors get fewer and fewer options, and more cells can be filled.

#More difficult puzzles require a bit more work as there aren’t enough cells filled in for this simple method.


# naive way :
#####
#Rough Naive Algorithm 

# Start at first cell
# Pick a value that isn’t present in any neighbors
# If at last cell, exit
# Other wise go to next cell
# Go to step 2

import random

numbers = [i for i in range(1,10)]

grid = [[[] for i in range(9)] for i in range(9)]
print(grid)

for row in range(len(grid)):
    print(f'row = {row}')
    print(grid[row])
    for cell in range(len(grid)):
        print(f'cell = {cell}')
        print(grid[row][cell])
        r = random.randint(0,8)
        print(f'randomint = {r}')
        print('numbers r = {}'.format(numbers[r]))
        grid[row][cell] = numbers[r]
        print('grid[row][cell] = {}'.format(grid[row][cell]))
for line in grid:
    print(line)
