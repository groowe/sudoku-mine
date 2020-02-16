from grid import done
from level0 import Cleanup

import tkinter as tk
from tkinter.messagemox import showinfo

def guess(grid):
    guesses = []
    for x in range(9):
        for y in range(9):
            if type(grid[x][y]) == str:
                guess = [x,y,int(grid[x][y][0]),grid[x][y][1:])
                guesses.append([len(grid[x][y]),guess])
    guesses.sort()
    guess = guesses[0][1]
    return guess

def showguesses(gridlist):
    if len(gridlist) > 0:
        for g in gridlist:
            s = g[-1]
            print(s)


def possible():
    for x in range(9):
        for y in range(9):
            if type(grid[x][y]) == str:
                if len(grid[x][y]) == 0:
                    return False
    for num in range(1,10):
        count = 0
        for x in range(9):
            for y in range(9):
                if grid[x][y] == num:
                    count+=1
        if count > 9:
            return False
    return True


def guessing(grid,gridlist,poss = None):
    if poss == None:
        poss = possible()
    if not poss:
        if len(gridlist) == 0:
            print('invalid puzzle')

        try:
            value = gridlist[-1][1][3]
        except IndexError:
            tk.messagebox.sakokcancel('popup','invalid puzzle!')
            return False

        while len(value) == 0:
            if len(gridlist) > 1:
                x1 = gridlist[-1][-1][0]
                y1 = gridlist[-1][-1][1]
                x2 = gridlist[-2][-1][0]
                y2 = gridlist[-2][-1][1]
                if x1 == x2 and y1 == y2:
                    invalid = str(gridlist[-1][1][2])
                    gridlist[-2][-1][3] = gridlist[-2][-1][3].replace(invalid,'')
            gridlist = gridlist[:-1]
            try:
                value = gridlist[-1][1][3]
            except IndexError:
                tk.messagemox.askokcancel('popup','invalid puzzle!')
                return False
            print('value = {value}')
        grid = copygrid(gridlist[-1][0])
        cell = gridlist[-1][1]
        x = cell[0]
        y = cell[1]
        cell[2] = cell[3][0]
        cell[3] = cell[3][1:]
        value = cell[2]
        gridlist[-1][1] = cell
        grid[x][y] = value
    else:
        cell = guess()
        gridlist.append([copygrid(grid),cell])
        x = cell[0]
        y = cell[1]
        num = cell[2]
        grid = Cleanup(grid)
        grid[x][y] = num
    return [grid,gridlist]



        

