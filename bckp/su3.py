# next try, doing it as efficiently as possible with 
# help from pdf

# first, defining empty cell
# every cell will hold only one number
# 8176
#grid_empty = [[8176 for i in range(9)] for i in range(9)]
#for g in grid:
#    print(g)
#why ?
#>>> bin(8176)
#'0b1111111110000'
# 2**4 is first power of nine bigger than 9
# if value & 2**4 == 2**4 , then 1 is possible in cell
# 
# if value & 2**5 == 2**5 , then 2 is possible in cell
# etc ..
# if 0 < value < 16 (= 2**4) , then cell is solved
# if value == 0 , invalid
# 
# import for hard copy grid
from copy import deepcopy as dc

def basicgrid():
    return [[8176 for i in range(9)] for i in range(9)]

def standardize(grid):
    for x in range(9):
        for y in range(9):
            if grid[x][y] == None or grid[x][y] == 0:
                grid[x][y] = 8176
    return Cleanup(grid)

def Cleanup(grid):
#When you solve a cell, the number that solves it cannot be
# a candidate anywhere else in any of the units to
# which the cell belongs.
    for x in range(9):
        for y in range(9):
            if grid[x][y] < 16:
                modx = int(x/3) # square x
                mody = int(y/3) # square y
                num = grid[x][y] # value
                poww = 2**(num+3) # conversion 
                for ix in range(9):
                    modix = int(ix/3)
                    inrow = (x == ix)
                    for iy in range(9):
                        if grid[ix][iy] >= 16:
                            modiy = int(iy/3)
                            incul = (y == iy)
                            numing = (grid[ix][iy] & poww == poww)
                            diff = not (inrow and incul)
                            insqr = ((modx == modix) and (mody == modiy))
                            if numing and diff and (inrow or incul or insqr):
                                grid[ix][iy] = grid[ix][iy] ^ poww
#                                    if grid[ix][iy] == 0:
#                                        return False
    return grid


# some basic sudokus
#####################################################
def easy():
    grid = basicgrid()
    grid[0] = [0,3,0,8,1,0,7,0,6]
    grid[1] = [6,0,1,7,9,5,0,3,8]
    grid[2] = [0,0,7,3,0,6,0,0,5]
    grid[3] = [0,7,8,5,0,0,0,0,1]
    grid[4] = [0,0,6,4,0,7,3,0,0]
    grid[5] = [3,0,0,0,0,9,8,6,0]
    grid[6] = [4,0,0,6,0,8,5,0,0]
    grid[7] = [8,6,0,9,3,4,1,0,2]
    grid[8] = [7,0,3,0,5,1,0,8,0]
    grid = standardize(grid)
#    print("whoooo")
    return grid


def medium():
    grid = basicgrid()
    grid[0] = [1,0,0,2,0,6,9,0,0]
    grid[1] = [0,5,0,0,3,0,2,0,0]
    grid[2] = [0,0,0,7,0,9,0,6,0]
    grid[3] = [9,0,0,0,0,0,8,4,5]
    grid[4] = [5,0,0,0,0,0,0,0,7]
    grid[5] = [2,8,4,0,0,0,0,0,6]
    grid[6] = [0,1,0,6,0,7,0,0,0]
    grid[7] = [0,0,2,0,1,0,0,5,0]
    grid[8] = [0,0,6,8,0,5,0,0,9]
    grid = standardize(grid)
    return grid


def hard():
    grid = basicgrid()
    grid[0] = [3,0,1,4,0,0,0,0,0]
    grid[1] = [9,0,0,0,0,0,6,2,7]
    grid[2] = [0,0,0,9,0,8,0,0,4]
    grid[3] = [0,0,0,0,0,0,1,7,2]
    grid[4] = [0,3,0,0,6,0,0,9,0]
    grid[5] = [1,2,9,0,0,0,0,0,0]
    grid[6] = [6,0,0,3,0,9,0,0,0]
    grid[7] = [7,9,5,0,0,0,0,0,1]
    grid[8] = [0,0,0,0,0,7,9,0,6]
    return standardize(grid)



def extreme():
    grid = basicgrid()
    grid[0] = [4,3,0,0,0,0,0,0,0]
    grid[1] = [6,0,0,0,0,0,0,2,5]
    grid[2] = [2,0,0,0,3,8,0,0,0]
    grid[3] = [0,0,4,0,5,0,0,1,0]
    grid[4] = [0,0,5,8,0,9,6,0,0]
    grid[5] = [0,9,0,0,1,0,5,0,0]
    grid[6] = [0,0,0,1,9,0,0,0,6]
    grid[7] = [3,7,0,0,0,0,0,0,9]
    grid[8] = [0,0,0,0,0,0,0,3,1]
    return standardize(grid)

def hardest():

    grid = basicgrid()
    grid[0] = [8,0,0,0,0,0,0,0,0]
    grid[1] = [0,0,3,6,0,0,0,0,0]
    grid[2] = [0,7,0,0,9,0,2,0,0]
    grid[3] = [0,5,0,0,0,7,0,0,0]
    grid[4] = [0,0,0,0,4,5,7,0,0]
    grid[5] = [0,0,0,1,0,0,0,3,0]
    grid[6] = [0,0,1,0,0,0,0,6,8]
    grid[7] = [0,0,8,5,0,0,0,1,0]
    grid[8] = [0,9,0,0,0,0,4,0,0]
    return standardize(grid)

def hardest2():
    grid = basicgrid()
    grid[0] = [1,0,0,0,0,7,0,9,0]
    grid[1] = [0,3,0,0,2,0,0,0,8]
    grid[2] = [0,0,9,6,0,0,5,0,0]
    grid[3] = [0,0,5,3,0,0,9,0,0]
    grid[4] = [0,1,0,0,8,0,0,0,2]
    grid[5] = [6,0,0,0,0,4,0,0,0]
    grid[6] = [3,0,0,0,0,0,0,1,0]
    grid[7] = [0,4,0,0,0,0,0,0,7]
    grid[8] = [0,0,7,0,0,0,3,0,0]
    return standardize(grid)

def hardestinvalid():
    grid  = hardest()
    grid[8][8] = 3
    return grid

def extremeinvalid():
    grid = extreme()
    grid[4][4] = 6
    return grid


#####################################################

def done():
    for x in range(9):
        for y in range(9):
            if grid[x][y] > 10:
                return False , False
    return True , validate_solution()

def validate_solution():
    nums = [i for i in range(1,10)]
    for num in nums:
        ind = [i for i in range(9)]
        for x in range(9):
            if grid[x].count(num) != 1:
                return False
            try:
                ind.remove(grid[x].index(num))
            except ValueError:
                return False
            except Exception as ex:
                print(f'exception catched')
                print(f'function : validate_solution:')
                print(f'exception name : {ex}')
                return False
    return True

def copygrid(fromgrid = False):
    if fromgrid:
        return dc(fromgrid)
    return dc(grid)

# techniques
#####################################################
# level 0

def Naked_Single():
#    If a cell only has a single candidate, that candidate solves the cell.
    global grid
    nums = [2**(i+4) for i in range(9)]
    found = False
    for x in range(9):
        for y in range(9):
            if grid[x][y] in nums:
                grid[x][y] = nums.index(grid[x][y])+1
                found = True
    return found

def Unique(unit): # unit = list  == row/ column/ sqr
#   If you find a candidate for a particular number
#   in a single cell of a unit, the candidate must solve the cell.
    nums = [2**(i+4) for i in range(9)]
    found = False
    for num in nums:
        ind = []
        for cell in unit:
            if cell & num == num:
                ind.append(unit.index(cell))
        if len(ind) == 1:
            unit[ind[0]] = nums.index(num)+1
            found = True
    if found:
        return unit
    return False



    
# level0 Cleanup is already coded
#When you solve a cell, the number that solves it cannot be
# a candidate anywhere else in any of the units to
# which the cell belongs.

############################################################
# level1

def Naked_Pair(unit): # unit = list  == row/ column/ sqr
#If two cells in the same unit only contain the same two candidates,
#it means that one of those candidates will
#solve one of the two cells, and the other candidate will solve the other cell.
#Therefore, you can remove the
#same candidates from all other cells of the unit.

    nums = [2**(i+4) for i in range(9)]

    pairs = []
    uniqes = []
    for a in range(len(nums)):
        for b in range(len(nums)):
            if a < b:
                pairs.append(nums[a]*nums[b])
                uniqes.append([a,b])
    found = False
    for pair in pairs:
        if unit.count(pair) == 2:
            p = uniqes[pairs.index(pair)]
            for un in unit:
                if un != pair:
                    for i in p:
                        if un & i == i:
                            unit[unit.index(un)] = un ^ i
                            found = True
    if found:
        return unit
    return False

def Hidden_Pair(unit):   # unit = list  == row/ column/ sqr
#if two candidates only appear in two cells of a unit,
#it means that one of those candidates will solve one of the
#two cells, and the other candidate the other cell.
#Therefore, you can remove all other candidates in the two cells
    nums = [2**(i+4) for i in range(9)]
    inds = []
    for num in nums:
        inds.append([])

        for cell in range(len(unit)):
            if unit[cell] & num == num:
                inds[-1].append(cell)
    twos = []
    for ind in range(len(inds)):
        if len(inds[ind]) == 2:
            twos.append([nums[ind],inds[ind]])
    found = False
    if len(twos) > 1:
        for x in range(len(twos)):
            for y in range(len(twos)):
                if x < y:
                    if twos[x][1] == twos[y][1]:
                        n = twos[x][0]+twos[y][0]
                        for tw in twos[x][1]:
                            if unit[tw] != n:
                                unit[tw] = n
                                found = True
    if found:
        return unit
    return False

def Box_Line():
#When a specific candidate within a row or a column
#only occurs in a single box, one of those occurrences
#must be a solution. Therefore, you can remove the
#same candidate from all other cells of the same box.
    global grid
    nums = [2**(i+4) for i in range(9)]
    found = False
    for x in range(9):
        for num in nums:
            line = [i for i in range(9) if grid[x][i] & num == num]
            cul = [i for i in range(9) if grid[i][x] & num == num]
            modline = (len(set([int(i/3) for i in line]))==1)

            modcul = (len(set([int(i/3) for i in cul]))==1)
            if (modline or modcul):
                if modline:
                    modx = int(x/3)
                    mody = int(line[0]/3)
                    orig = [[x,y] for y in line]
                else:
                    modx = int(cul[0]/3)
                    mody = int(x/3)
                    orig = [[y,x] for y in cul]

                for xx in range(9):
                    modxx = int(xx/3)
                    if modx == modxx:
                        for yy in range(9):
                            modyy = int(yy/3)
                            if modyy = mody:
                                if [xx,yy] not in orig:
                                    if grid[xx][yy] & num == num:
                                        found = True
                                        grid[xx][yy] = grid[xx][yy] ^ num
    
    return found

def Pointing_Line():
    global grid

    nums = [2**(i+4) for i in range(9)]
#when all the cells containing a
#particular candidate within a box belong to the same line 
#(row or column), you can remove the candidates
#for the same number that appear in the line but outside that box.
    found  = False
    for modx in range(3):
        for mody in range(3):
            sqr = []
            for x in range(modx*3,(modx+1)*3):
                for y in range(mody*3,(mody+1)*3):
                    sqr.append(grid[x][y])
            for num in nums:
                nn = []
                row = []
                cul = []
                for s in range(len(sqr)):
                    if sqr[s] & num == num:
                        nn.append(s)
                        row.append(int(s/3)) # 0 0 0 1 1 1 2 2 2 
                        cul.append(s%3)     # 0 1 2 0 1 2 0 1 2
                inrow = (len(set(row)) == 1)
                incul = (len(set(cull)) == 1)
                if (inrow or incul):
                    if inrow:
                        stat = row[0] +( modx*3)
                        coords = [[stat,y] for y in range(9) if int(y/3) != mody]
                    else:
                        stat = cul[0] + (mody*3)
                        coords = [[y,stat] for y in range(9) if int(y/3) != modx]
                    for xx,yy in coords:
                        if grid[xx][yy] & num == num:
                            found = True
                            grid[xx][yy] = grid[xx][yy] ^ num
    return found


############################################################
# level2 ###################################################

#The strategies are naked triple, hidden triple, lines-2, naked quad, and
#Y-wing.

def Naked_Multiple(unit):
# similiar to Naked_Pair
# it just tries more

    nums = [2**(i+4) for i in range(9)]

    mult = 3

    found = False
    while mult < 8:
        multiples = []
        uniqes = []

        for a in range(len(nums)):
            for b in range(len(nums)):
                for c in range(len(nums)):
                    if mult == 3 and a<b<c :
                        multiples.append(nums[a]*nums[b]*nums[c])
                        uniqes.append([a,b,c])
                    elif mult > 3:
                        for d in range(len(nums)):
                            if a<b<c<d:
                                if mult == 4:
                                    multiples.append(nums[a]*nums[b]*nums[c]*nums[d])
                                    uniqes.append([a,b,c,d])
                                elif mult > 4:
                                    for e in range(len(nums)):
                                        if d<e:
                                            if mult == 5:
                                                multiples.append(nums[a]*nums[b]*nums[c]*nums[d]
                                                    *nums[e])

                                                uniqes.append([a,b,c,d,e])
                                            elif mult > 5:
                                                for f in range(len(nums)):
                                                    if e<f:
                                                        if mult == 6:
                                                            multiples.append(nums[a]*nums[b]*nums[c]*nums[d]
                                                                *nums[e]*nums[f])
                                                            uniqes.append([a,b,c,d,e,f])
                                                        elif mult > 6:
                                                            for g in range(len(nums)):
                                                                if f<g:
                                                                    if mult == 7:
                                                                        multiples.append(nums[a]*nums[b]*nums[c]*nums[d]
                                                                        *nums[e]*nums[f]*nums[g])
                                                                        uniqes.append([a,b,c,d,e,f,g])




        for mult in multiples:
            if unit.count(mult) == mult:
                p = uniqes[multiples.index(mult)]
                for un in unit:
                    if un != mult:
                        for i in p:
                            if un & i == i:
                                unit[unit.index(un)] = un ^ i
                                found = True
        if found:
            return unit
        mult+=1
    return False

def Hidden_Triple(unit):
# same as Hidden_Pair, just for 3
    nums = [2**(i+4) for i in range(9)]
    inds = []
    for num in nums:
        inds.append([])

        for cell in range(len(unit)):
            if unit[cell] & num == num:
                inds[-1].append(cell)
    triple = []
    for ind in range(len(inds)):
        if len(inds[ind]) == 3:
            triple.append([nums[ind],inds[ind]])
    found = False
    if len(triple) > 2:
        for x in range(len(twos)):
            for y in range(len(twos)):
                for z in range(len(twos)):
                    if x < y < z:
                        if triple[x][1] == triple[y][1] == triple[z][1]:
                            n = triple[x][0]+triple[y][0]+triple[z][0]
                            for tw in triple[x][1]:
                                if unit[tw] != n:
                                    unit[tw] = n
                                    found = True
    if found:
        return unit
    return False

def Lines_2():
#This strategy is also called X-wing.
#If you find a particular candidate in the same two rows (i.e., positions)
#within two columns,
#you can remove that candidate from the other cells of those two rows.
    global grid

    nums = [2**(i+4) for i in range(9)]
    found = False
    for num in nums:
        rows =[]
        cols = []
        for x in range(9):
            r = [y for y in range(9) if grid[x][y] & num == num]
            c = [y for y in range(9) if grid[y][x] & num == num]
            rows.append(r) # rows[x][y]
            cols.append(c) # cols[y][x]
        rowind = []
        for r in rows:
            if len(r) == 2 and rows.count(r) == 2:
                s = [i for i in range(len(rows)) if rows[i] == r]
                if s not in rowind:
                    rowind.append(s) # rowind = [x,x]
        colind = []
        for c in cols:
            if len(c) == 2 and cols.count(c) == 2:
                s = [i for i in range(len(cols)) if cols[i] == c]
                if s not in colind:
                    colind.append(s) # colind = [y,y]
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
                            if grid[x][y] & num == num:
                                grid[x][y] = grid[x][y] ^ num
                                found = True
            for pair in colind:
                keep = []
                r = []
                for y in pair:
                    for x in cols[y]:
                        if [x,y] not in keep:
                            keep.append([x,y])
                            r.append(x)
                for x in r:
                    for y in range(9):
                        if [x,y] not in keep:
                            if grid[x][y] & num == num:
                                grid[x][y] = grid[x][y] ^ num
                                found = True
    return found

def Y_Wing():

    # NOTE! to be redone
#To apply the Y-wing strategy you need to look for cells that contain only two candidates each. Among
#those cells, you need to find three cells that satisfy the following two conditions:
#
#  • The arrangement of candidates in the cells is AB, AC, and BC. That is, no two cells
#    have the same pair of candidates.
#  • The cells are in two intersecting units. This is equivalent to say that the two wing cells
#    cannot share any unit, and it can only happen in two ways: row+column (one of the
#    cells shares the row with one of the other two cells and the column with the third one)
#    and line+box, where “line” stands for either “column” or “row” (one of the cells shares
#    the line (row or column) with one of the other two cells and the box with the third one).
    global grid
    nums = [2**(i+4) for i in range(9)]
    found = False
    pairs = []
    uniqes = []
    for a in range(len(nums)):
        for b in range(len(nums)):
            if a < b:
                pairs.append(nums[a]*nums[b])
                uniqes.append([a,b])
    cands = []
    for x in range(9):
        for y in range(9):
            if grid[x][y] in pairs:
                cands.append([x,y,uniqes[pairs.index(grid[x,y])]])
    if len(cands) > 2:
        used = []
        for can in cands:
            x = can[0] # int
            y = can[1] # int 
            nums = can[2] # [int,int]
            allvals = [i for i in nums]
            allcoords = [[x,y]]
            if can in used:
                continue
            for nd in cands:
                if nd != can and (nd not in used):
                    if (nd[0] == x or nd[1] == y) and ((nums[0] in nd[2]) or (nums[1] in nd[2])):
                        allcoords.append([nd[0],nd[1]])
                        allvals.extend[i for i in nd[2] if not in allvals]
                        havex = False
                        havey = False
                        have0 = False
                        have1 = False
                        if nd[0] == x:
                            havex = True
                        if nd[1] == y:
                            havey = True
                        if nums[0] in nd[2]:
                            have0 = True
                        if nums[1] in nd[2]:
                            have1 = True
                        lfval = 0 # looking for value .. 
                        if have0:
                            lfval = nums[1]
                            for v in nd[2]:
                                if v != nums[0]:
                                    lfval = lfval * v
                        elif have1:
                            lfval = nums[0]
                            for v in nd[2]:
                                if v != nums[1]:
                                    lfval = lfval * v
                        if havex:
                            yys = [nd[1],y]
                            third = []
                            for ind in cands:
                                if (not third )and ( (ind != nd and ind != can) and (ind not in used) ):
                                    if ((ind[0] != x) and (ind[1] in yys) and (ind[2][0]*ind[2][1] == lfval ) ) :
                                        # BINGO !
                                        used.extend[can,nd,ind]
                                        third = ind
                                        allcoords.append([ind[0],ind[1]])
                                        allvals.extend[i for i in ind[2] if not in allvals]

                            newx = third[0]
                            newyind = 0
                            while third[0] == yys[newyind]:
                                newyind+=1
                            newy = yys[newyind]
                        elif havey:
                            xxs = [nd[0],x]
                            third = []
                            for ind in cands:
                                if (not third )and ( (ind != nd and ind != can) and (ind not in used) ):
                                    if ((ind[1] != y) and (ind[0] in xxs) and (ind[2][0]*ind[2][1] == lfval ) ) :
                                        # BINGO !
                                        used.extend[can,nd,ind]
                                        third = ind
                                        allcoords.append([ind[0],ind[1]])
                                        allvals.extend[i for i in ind[2] if not in allvals]
                            newy = third[0]
                            newxind = 0
                            while third[0] == xxs[newxind]:
                                newxind+=1
                            newx = xxs[newxind]
                        # newx , newy = coords of target cell
                        # now to find out what num can't be in that cell
                        # find oposite corner of the sqr
                        #  value that is not there (out of a , b , c ),
                        # can't be in the last corner
                        notvalue = 0
                        for coord in coords:
                            if coord[0] != newx and coord[1] != newy:
                                for val in allalls:
                                    if grid[coord[0]][coord[1]] & val != val:
                                        notvalue = val
                        if notvalue:
                            # FOUND IT!
                            if grid[newx][newy] & val == val:
                                found = True
                                grid[newx][newy] = grid[newx][newy] ^ val
    return found

def pairs_find():
    # need to find out what to use
    global grid
    nums = [2**(i+4) for i in range(9)]
    found = False
    pairs = []
    uniqes = []
    for a in range(len(nums)):
        for b in range(len(nums)):
            if a < b:
                pairs.append(nums[a]*nums[b])
                uniqes.append([a,b])
    cands = []
    for x in range(9):
        modx = int(x/3)
        for y in range(9):
            mody = int(y/3)
            if grid[x][y] in pairs:
                cands.append([[x,y],[modx,mody],uniqes[pairs.index(grid[x,y])]])

    return cands

