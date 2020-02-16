# level 2 solving strategies
# functions here:
# from level2 import Naked_Multiple,Hidden_Multiple,Lines_2,NT,NT_chains,Y_Wing,

def Naked_Multiple(unit):
    found = False
    for mult in range(3,8):

        done = []
        for cell in range(len(unit)):
            if type(unit[cell]) == str:
                if len(unit[cell]) == mult and cell not in done:
                    if unit.count(unit[cell]) == mult:
                        indexes = [i for i in range(len(unit)) if unit[i] == unit[cell]]
                        nums = [i for i in unit[cell]]
                        done.extend(indexes)
                        for c in range(len(unit)):
                            if type(unit[c]) == str and c not in indexes:
                                for num in nums:
                                    if num in unit[c]:
                                        found = True
                                        unit[c] = unit[c].replace(num,'')
        if found:
            return [unit,found]
                            
    return [unit,found]




def Hidden_Multiple(unit):
    found = False
    for mult in range(3,8):
        nums = [None]
        for num in range(1,10):
            nums.append([])
            if num in unit:
                continue
            num = str(num)
            for ind in range(len(unit)):
                if type(unit[ind]) == str:
                    if num in unit[ind]:
                        nums[-1].append(ind)
        for num in range(1,len(nums)):
            if len(nums[num]) == mult:
                if nums.count(nums[num]) == mult:

                    multiple = ''.join([str(v) for v in range(len(nums)) if nums[v] == nums[num]])

                    for ind in nums[num]:
                        if unit[ind] != multiple:
                            found = True
                            unit[ind] = multiple
        if found:
            return [unit,found]
        
    return [unit,found]

def Lines_2(grid):
    found = False
    for num in range(1,10):
        rows = []
        cols = []
        num = str(num)
        for x in range(9):
            r= [y for y in range(9) if (type(grid[x][y]) == str and num in grid[x][y])]

            c= [y for y in range(9) if (type(grid[y][x]) == str and num in grid[y][x])]
            rows.append(r)
            cols.append(c)
        rowind = []
        for r in rows:
            if len(r) == 2 and rows.count(r) == 2:
                s = [i for i in range(len(rows)) if rows[i] == r]
                if s not in rowind:
                    rowind.append(s)
        colind = []
        for c in cols:
            if len(c) == 2 and cols.count(c) == 2:
                s = [i for i in range(len(cols)) if cols[i] == c]
                if s not in colind:
                    colind.append(s)
        if colind or rowind:
            for pair in rowind:
                keep = []
                c = []
                for x in pair:
                    for y in rows[x]:
                        if [x,y] not in keep:
                            keep.append([x,y])
                            c.append(y)
                for y in c:
                    for x in range(9):
                        if [x,y] not in keep:
                            if type(grid[x][y]) == str:
                                if num in grid[x][y]:
                                    found = True
                                    grid[x][y] = grid[x][y].replace(num,'')
            for pair in colind:
                keep = []
                r = []
                for y in pair:
                    for x in rows[x]:
                        if [x,y] not in keep:
                            keep.append([x,y])
                            r.append(y)
                for x in c:
                    for y in range(9):
                        if [x,y] not in keep:
                            if type(grid[x][y]) == str:
                                if num in grid[x][y]:
                                    found = True
                                    grid[x][y] = grid[x][y].replace(num,'')
    return [grid,found]

def NT(grid):
    nt = []
    for x in range(9):
        for y in range(9):
            if type(grid[x][y]) == str:
                if len(grid[x][y]) == 2:
                    nt.append([grid[x][y],x,y,str(int(x/3))+str(int(y/3))])
    return nt #[ [value,x,y,sqr] , ... ]

def NT_chains(nakedtwos = []):

    chains = []
    for c in range(len(nakedtwos)):
        usedchain = [c]
        cell = nakedtwos[c]
        available = []
        for c2 in range(len(nakedtwos)):
            if c2 not in usedchain:
                ncell = nakedtwos[c2]
                com1 = (cell[0][0] in ncell[0])
                com2 = (cell[0][1] in ncell[0])
                com = ((com1 or com2))# and com1 != com2 )
                inrow = (cell[1] == ncell[1])
                incol = (cell[2] == ncell[2])
                insqr = (cell[3] == ncell[3])
                relevant = ((inrow or incol or insqr) and com)
                if relevant:
                    usedchain.append(c2)
                    available.append([c2,com1,com2,inrow,incol,insqr])
        chains.append(available)
    return chains # [[[1, False, True, False, False, True]], [[0, True, False, False, False, True]],

def Y_Wing(grid):

    found = False
    nakedtwos = NT(grid)
#    print(nakedtwos)
    if not nakedtwos:
        return [grid,found]

    chains = NT_chains(nakedtwos)
#    print(chains)
    for c in range(len(chains)):
        cc = chains[c]
        if len(cc) > 1:
            for cell in cc:
                for cell2 in cc:
                    if cell != cell2:
                        difval = ( cell[1] == cell2[2] )
                        rowcol = ( ( cell[3] and cell2[4] ) or ( cell[4] and cell2[3] ) )
                        rowsqr = ( ( cell[3] and cell2[5] ) or ( cell[5] and cell2[3] ) )
                        colsqr = ( ( cell[4] and cell2[5] ) or ( cell[5] and cell2[4] ) )
                        if difval and (rowcol or rowsqr or colsqr):
                            # almost bingo
                            indexes = [c,cell[0],cell2[0]]
#                            print(indexes)
                            # last check needed
                            vals = []
                            for index in indexes:
                                for v in nakedtwos[index][0]:
                                    vals.append(v)
                            vals = set(vals)
                            if len(vals) == 3:
                                # bingo !
                                cant = [v for v in vals if v not in nakedtwos[c][0]]
#                                print(f'nak {c} = {nakedtwos[c][0]}')

#                                print(f'cant = {cant}')
                                cant = cant[0]
#                                print(f' ntc = {nakedtwos[c]}')
#                                print(f'cant = {cant}')
                                if rowcol:
                                    if cell[3] and cell2[4]:
                                        # cell in row, == c[x] == cell[x]
                                        # cell2 in col == c[y] == cell2[y]
                                        xx = 1
                                        yy = 2
                                    else:
                                        xx = 2
                                        yy = 1
                                    newy = nakedtwos[indexes[xx]][yy]
                                    newx = nakedtwos[indexes[yy]][xx]
                                    if type(grid[newx][newy]) == str:
                                        if cant in grid[newx][newy]:
                                            found = True
                                            grid[newx][newy] = grid[newx][newy].replace(cant,'')
                                else: # sqr included
                                    checkxy = []
#                                    print(cell,cell2)
#                                    print(indexes)
                                    if cell[-1]: # sqr
                                        sq = indexes[1]
                                        ot = indexes[2]
                                        ot2 = cell2
#                                        print(sq,ot,ot2)
                                    else:
                                        sq = indexes[2]
                                        ot = indexes[1]
                                        ot2 = cell
                                    if ot2[3]:# row

                                        xx = nakedtwos[ot][1]
                                        yy = nakedtwos[sq][2]
                                        checkxy.append([xx,yy])
                                        xx = nakedtwos[sq][1]
#                                       modx = int(nakedtwos[sq])[3][0]
                                        mody = int(nakedtwos[ot][3][1])
                                        for y in range(mody*3,(mody+1)*3):
                                            checkxy.append([xx,y])
                                    else: # sqr col
                                        yy = nakedtwos[ot][2]
                                        xx = nakedtwos[sq][1]
                                        checkxy.append([xx,yy])
                                        yy = nakedtwos[sq][2]
                                        modx = int(nakedtwos[ot])[3][0]
                                        for x in range(modx*3,(modx+1)*3):
                                            checkxy.append([xx,yy])
#                                    print(checkxy)
                                    for coord in checkxy:
                                        x = coord[0]
                                        y = coord[1]
                                        if type(grid[x][y]) == str:
                                            if cant in grid[x][y]:
                                                found = True
                                                grid[x][y] = grid[x][y].replace(cant,'')
    return [grid,found]

