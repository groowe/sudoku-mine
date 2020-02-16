# level 3 strategies
# functions here:
# from level3 import XY_chain,Rectangle
######### !!!!!!! DOESN'T WORK YET !!!!!!!! #############
from level2 import NT, NT_chains
#def NT(grid):
#    nt = []
#    for x in range(9):
#        for y in range(9):
#            if type(grid[x][y]) == str:
#                if len(grid[x][y]) == 2:
#                    nt.append([grid[x][y],x,y,str(int(x/3))+str(int(y/3))])
#    return nt #[ [value,x,y,sqr] , ... ]
#
#def NT_chains(nakedtwos = []):
#    chains = []
#    for c in range(len(nakedtwos)):
#        usedchain = [c]
#        cell = nakedtwos[c]
#        available = []
#        for c2 in range(len(nakedtwos)):
#            if c2 not in usedchain:
#                ncell = nakedtwos[c2]
#                com1 = (cell[0][0] in ncell[0])
#                com2 = (cell[0][1] in ncell[0])
#                com = ((com1 or com2) and com1 != com2 )
#                inrow = (cell[1] == ncell[1])
#                incol = (cell[2] == ncell[2])
#                insqr = (cell[3] == ncell[3])
#                relevant = ((inrow or incol or insqr) and com)
#                if relevant:
#                    usedchain.append(c2)
#                    available.append([c2,com1,com2,inrow,incol,insqr])
#        chains.append(available)
#    return chains

def XY_chain(grid):
    found = False
    nakedtwos = NT(grid) #    return nt #[ [value,x,y,sqr] , ... ]
    #print(nakedtwos)
    if not nakedtwos:
        return [grid,found]
    chains = NT_chains(nakedtwos)
#    for chain in chains:
        #print(chain)
#    input()
    for c in range(len(chains)):
        cc = chains[c]

        startvals = {v for v in nakedtwos[c][0]}
        #print(f' startvals = {startvals}')
        startx = nakedtwos[c][1]
        starty = nakedtwos[c][2]
        startsqrxy = nakedtwos[c][3]
        origvals = {v for v in nakedtwos[c][0]}
        vals = {v for v in nakedtwos[c][0]}
        if len(cc) > 1:
            for cell in cc:
                #print(f'cell {cell}')
                if len(vals) != 3:
                    vals = {v for v in nakedtwos[c][0]}
                    vals.update([i for i in nakedtwos[cell[0]][0]])
                #print(f' vals = {vals}')
                inchain = [c,cell[0]]
                current = chains[cell[0]]
                valid = True
                while ((len(vals) != len(inchain)) and valid):
                    if len(current) == 1:
                        valid = False
                        break
                    else:
                        for cur in current:
                            if cur[0] not in inchain:
                                #print(cur[0])
                                #print(inchain)
                                inchain.append(cur[0])
                                current = chains[cur[0]]
                                vals.update([i for i in nakedtwos[cur[0]][0]])

                                #print(f' vals = {vals}')
                                break
                if len(vals) == len(inchain):
                    lastvals = nakedtwos[inchain[-1]][0]
                    lastx = nakedtwos[inchain[-1]][1]
                    lasty = nakedtwos[inchain[-1]][2]
                    lastsqrxy = nakedtwos[inchain[-1]][3]
                    common = [i for i in lastvals if i not in startvals]
                    if len(common) != 1:
                        continue
                    common = common[0]
                    row = ( lastx == startx )
                    col = ( lasty == lasty )
                    sqr = ( startsqrxy == lastsqrxy )
                    if row:
                        ex = [starty,lasty]
                        for y in range(9):
                            if y not in ex:
                                if type(grid[startx][y]) == str:
                                    if common in grid[startx][y]:
                                        found = True
                                        grid[startx][y] = grid[startx][y].replace(common,'')
                    if col:
                        ex = [startx,lastx]
                        for x in range(9):
                            if x not in ex:
                                if type(grid[x][starty]) == str:
                                    if common in grid[x][starty]:
                                        found = True
                                        grid[x][starty] = grid[x][starty].replace(common,'')
                    if sqr:
                        modx = int(startsqrxy[0])
                        mody = int(startsqrxy[1])
                        ex = [[startx,starty],[lastx,lasty]]
                        for x in range(modx,(modx+1)*3):
                            for y in range(mody,(mody+1)*3):
                                if [x,y] not in ex:
                                    if type(grid[x][y]) == str:
                                        if common in grid[x][y]:
                                            found = True
                                            grid[x][y] = grid[x][y].replace(common,'')

    return [grid,found]


def Rectangle(grid):
    nums = []
    validrec =[ [0,1,4,3],[0,2,5,3],[0,1,7,6],
            [0,2,8,6],[1,2,5,4],[1,2,8,7],
            [3,4,7,6],[3,5,8,6],[4,5,8,7]
            ]
    for i in range(1,10):
        sti = str(i)
        rec = []
        for modx in range(3):
            for mody in range(3):
                for x in range(modx,(modx+1)*3):
                    for y in range(mody,(modx+1)*3):
#                        if grid[x]
                        return

