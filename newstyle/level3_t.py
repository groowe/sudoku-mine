# for unittest :
import unittest
from grid import basicgrid as bg
from grid import copyofgrid as cp
# logic of function:

# find cell where there are only two possibilities
# from that cell, go sqr/line/row where there is another cell 
# for function : 
from level2 import NT, NT_chains
def XY_chain(grid):
    found = False
    nakedtwos = NT(grid)
    if not nakedtwos:
        return [grid,found]
    nakedcells = [chaincell(nakedtwos[i][0],nakedtwos[i][1],nakedtwos[i][2],nakedtwos[i][3]) for i in range(len(nakedtwos))]
    chains = []
    for nt in nakedtwos:
        print(nt)
        for nc in nakedtwos:
            if nc != nt:
                sqrcolline = any(nc[i] == nt[i] for i in range(1,4))
                val =( (nc[0][0] in nt[0]) or ( nc[0][1] in nt[0] ) )
                if val and sqrcolline:
                    itt = nakedtwos.index(nt)
                    icc = nakedtwos.index(nc)
                    nakedcells[itt].add_neighbour(nakedcells[icc])

    for nc in nakedcells:
        print(nc)
        print(nc.call())
    return [grid,found]

class chaincell():
    def __init__(self,value,x,y,sqr):
        self.value = value
        self.x = x
        self.y = y
        self.sqr = sqr
        self.neighbours = []
        self.neighvals= []
    def values(self):
        return self.value
    def in_value(self,val):
        return (val in self.value)
    def add_neighbour(self,cell):
        if cell not in self.neighbours:
            self.neighbours.append(cell)
            self.neighvals.append(cell.values())
    def is_x(self,xx):
        return xx == self.x
    def is_y(self,yy):
        return yy == self.y
    def is_sqr(self,sqqr):
        return sqqr == self.sqr

    def __repr__(self):
        return f'{self.value} at [{self.x}][{self.y}] ({self.sqr})'

    def call(self,used = [],lastvalue = ''):
        self.used = used.append(self)
        self.avail = [ nei for nei in self.neighbours if nei not in used ]
        if self.avail:
            return [i.call(self.used) for i in self.avail]
        else:
            return [self.value, self.x,self.y,self.sqr]

#def XY_chain(grid):
#    found = False
#    nakedtwos = NT(grid)
#    if not nakedtwos:
#        return [grid,found]
##    for nt in nakedtwos:
##        print(nt)
#    chains = NT_chains(nakedtwos)
#    for c in range(len(chains)):
#        cc = chains[c]
#        if len(cc) > 1:
#            ct = nakedtwos[c]
#            print(ct,cc)
#            current = ct
#            used = [ct]
#            last = None
#            started = ct
#            for cell in cc:
#                if cell not in used:
#                    print(cell)
#                    last = current
#                    current = nakedtwos[cell[0]]
#                    used.append(current)
#                    
#
#
#    return [grid,found]
class Testlevel3(unittest.TestCase):
    def test_level3_XY_chain(self):
        basic = bg()
        cpbasic = cp(basic)
        XY = XY_chain
        XY1 = XY(basic)
        self.assertTrue(cpbasic == XY1[0])
        self.assertFalse(XY1[1])
        basic[0][0] = '12'
        basic[1][2] = '14'
        basic[1][7] = '34'
        basic[2][5] = '23'
        basic[2][7] = '23'
        basic[3][0] = '23'
        basic[4][5] = '23'
        basic[4][6] = '23'
        basic[5][1] = '23'
        basic[6][1] = '23'
        basic[7][4] = '23'
        basic[7][6] = '23'
        basic[8][2] = basic[8][3] = '23'
        cpbasic = cp(basic)
        XY = XY_chain
        XY1 = XY(basic)
        not1 =[ [0,1],[0,2],[1,0],[1,1],[2,0],[2,1],[2,2]]
        for n in not1:
            x= n[0]
            y= n[1]
            print(x,y)
            self.assertFalse('1' in XY1[0][x][y])




if __name__ == '__main__':
    unittest.main()

