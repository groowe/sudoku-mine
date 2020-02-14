import unittest
from grid import basicgrid,standardize,done,validate_solution,copyofgrid


class TestGrid(unittest.TestCase):
    def test_grid_basic(self):
        self.assertEqual(basicgrid(),[['123456789' for i in range(9)] for i in range(9)])
    
    def test_grid_standardize(self):
        bg = basicgrid()
        self.assertEqual(standardize(bg),basicgrid())
        bg[1][2] = 0
        self.assertEqual(standardize(bg),basicgrid())
        bg[1][2] = None
        self.assertEqual(standardize(bg),basicgrid())
        bg[1][2] = '0'
        self.assertEqual(standardize(bg),basicgrid())
        bg[1][2] = '32'
        self.assertNotEqual(standardize(bg),basicgrid())
        bg[1][2] = 3
        self.assertNotEqual(standardize(bg),basicgrid())

    def test_grid_done(self):
        self.assertFalse(done(basicgrid())[0])
        g = [[1,2,3,5,4,6,8,9,8] for i in range(9)]
        self.assertTrue(done(g)[0])
        self.assertFalse(done(g)[1])

    def test_validate_solution(self):
        g =[ [0,2,5,3,5,6,7,8,9] for i in range(9)]
        self.assertFalse(validate_solution(g))
        g = [[1,2,3,4,5,6,7,8,9] for i in range(9)]
        self.assertFalse(validate_solution(g))
        g = [[1,None,3,4,5,6,7,8,9] for i in range(9)]
        self.assertFalse(validate_solution(g))

    def test_copyofgrid(self):
        self.assertFalse(basicgrid() is copyofgrid(basicgrid()))
        self.assertTrue(basicgrid() == copyofgrid(basicgrid()))

from level0 import Cleanup,Naked_Single,Unique   
class Testlevel0(unittest.TestCase):

    def test_level0_cleanup(self):
        cp = copyofgrid
        a =[ ['123456789' for i in range(9)] for i in range(9)]
        b = cp(a)
        cu = Cleanup(b)
        self.assertEqual(cu[0],a)
        self.assertFalse(cu[1])
        a[1][2] = 3
        b = cp(a)
        cu = Cleanup(b)
        self.assertFalse(cu[0] == a)
        self.assertTrue(cu[1])
    def test_level0_Naked_Single(self):
        cp = copyofgrid
        a = basicgrid()
        b = cp(a)
        NSA = Naked_Single(a)
        self.assertTrue(NSA[0] == b)
        self.assertFalse(NSA[1])

        a[1][2] = '3'
        b = cp(a)
        NSA = Naked_Single(a)
        self.assertTrue(NSA[1])
        self.assertFalse(NSA[0] == b)
        self.assertTrue(NSA[0][1][2] == 3)

    def test_level0_Unique(self):

        cp = copyofgrid
        unit = ['12356789' for i in range(9)]
        unit[0] = '123456789'
        cpunit = cp(unit)
        unique = Unique(unit)
        self.assertTrue(unique[1])
        self.assertTrue(unique[0][0] == 4)
        self.assertFalse(cpunit == unit)
        final_unit = ['12356789' for i in range(9)]
        final_unit[0] = 4
        self.assertTrue(final_unit == unit)

from level1 import Naked_Pair,Hidden_Pair,Box_Line,Pointing_Line

class Testlevel1(unittest.TestCase):
    def test_level1_Naked_Pair(self):
        cp = copyofgrid
        base = ['123456789' for i in range(9)]

        cpbase = cp(base)
        naked_pair = Naked_Pair(base)
        self.assertTrue(naked_pair[0] == cpbase)
        self.assertFalse(naked_pair[1])
        base[0] = base[5] = '24'
        cpbase = cp(base)
        naked_pair = Naked_Pair(base)
        self.assertTrue(naked_pair[1])
        self.assertFalse(naked_pair[0] == cpbase)

    def test_level1_Hidden_Pair(self):
        cp = copyofgrid
        base = ['1236789' for i in range(9)]
        base[0] = base[3] = '123456789'
        cpbase = cp(base)
        wanted = cp(base)
        wanted[0] = wanted[3] = '45'
        fullbase = ['123456789' for i in range(9)]
        cpfull = cp(fullbase)
        HP = Hidden_Pair(base)
        HP_Full = Hidden_Pair(fullbase)
#        wanted = ['1236789' for i in range(9)]

        self.assertTrue(HP[1])
        self.assertFalse(HP_Full[1])

        self.assertFalse(HP[0] == cpbase)
        self.assertTrue(HP_Full[0] == cpfull)
        
        self.assertTrue(wanted == HP[0])

    
    def test_level1_Box_Line(self):
        cp = copyofgrid
        basic = basicgrid()
        basic[0] = ['12345689' for i in range(9)]
        basic[0][1] = basic[0][0] = '123456789'
        cpbasic = cp(basic)
        BL = Box_Line(basic)

        self.assertFalse(basic == cpbasic)
        self.assertTrue(basic[1][0] == '12345689')

    def test_level1_Pointing_Line(self):
        cp = copyofgrid
        basic = basicgrid()
        cpbasic = cp(basic)
        PL = Pointing_Line(basic)

        self.assertFalse(PL[1])
        self.assertTrue(PL[0] == cpbasic)
        basic[0][0:3] = ['12346789' for i in range(3)]
        basic[2][0:3] = ['12346789' for i in range(3)]
#        print(basic[0])
        cpbasic = cp(basic)

        PL = Pointing_Line(basic)
        self.assertTrue(PL[1])
        self.assertFalse(PL[0] == cpbasic)
        target = ['12346789' for i in range(6)]
        self.assertTrue(PL[0][1][3:] == target)

from level2 import Naked_Multiple,Hidden_Multiple,Lines_2,NT,NT_chains,Y_Wing
class Testlevel2(unittest.TestCase):
    def test_level2_Naked_Multiple(self):
        cp = copyofgrid
        basic = ['123456789' for i in range(9)]
        cpbasic = cp(basic)
        NM = Naked_Multiple
        NM1 = Naked_Multiple(basic)
        self.assertTrue(NM1[0] == cpbasic)
        self.assertFalse(NM1[1])
        basic[0] = basic[2] = basic[5] = '235'
#        print(basic)
        cpbasic = cp(basic)
        NM1 = Naked_Multiple(basic)

        self.assertFalse(NM1[0] == cpbasic)
        self.assertTrue(NM1[1])
        cc = ['235', '146789', '235', '146789', '146789', '235', '146789', '146789', '146789']

#        print(basic)
        self.assertTrue(cc == basic)

#        print(basic)
    def test_level2_Hidden_Multiple(self):
        cp = copyofgrid
        HP = Hidden_Multiple

        basic = ['123456789' for i in range(9)]
        cpbasic = cp(basic)
        HP1 = HP(basic)
        self.assertTrue(HP1[0] == cpbasic)
        self.assertFalse(HP1[1])
        
        basic = ['123789' for i in range(9)]
        basic[0] = basic[2] = basic[5] = '123456789'

        cpbasic = cp(basic)
        HP1 = HP(basic)
        self.assertFalse(HP1[0] == cpbasic)
        self.assertTrue(HP1[1])
        cpbasic[0] = cpbasic[2] = cpbasic[5] = '456'
        self.assertTrue(HP1[0] == cpbasic)

    def test_level2_Lines_2(self):
        cp = copyofgrid
        L2 = Lines_2
        basic = basicgrid()
        cpbasic = cp(basic)
        L2_1 = L2(basic)
        self.assertTrue(L2_1[0] == cpbasic)
        basic[0][1:-1] = basic[3][1:-1] = ['12345789' for i in range(7)]
        cpbasic = cp(basic)
        L2_1 = L2(basic)
        self.assertFalse(L2_1[0] == cpbasic)
        self.assertTrue(L2_1[1])
        tt = '12345789'
        self.assertTrue(L2_1[0][2][0] == tt)

    def test_level2_NT(self):
#        cp = copyofgrid
        twins = NT
        basic = basicgrid()
#        cpbasic = cp(basic)
        twins1 = twins(basic)
        self.assertTrue(twins1 == [])
        for i in range(8):
            basic[i][i+1] = f'{i+1}{i+2}'

        twins1 = twins(basic)
#        print(twins1)
        target = [['12', 0, 1, '00'], ['23', 1, 2, '00'],
                ['34', 2, 3, '01'], ['45', 3, 4, '11'],
                ['56', 4, 5, '11'], ['67', 5, 6, '12'],
                ['78', 6, 7, '22'], ['89', 7, 8, '22']]
        self.assertTrue(target == twins1)

    def test_level2_NT_chains(self):
        twos = [['12', 0, 1, '00'], ['23', 1, 2, '00'],
                ['34', 2, 3, '01'], ['45', 3, 4, '11'],
                ['56', 4, 5, '11'], ['67', 5, 6, '12'],
                ['78', 6, 7, '22'], ['89', 7, 8, '22']]
        NTC = NT_chains
        NTC1 = NTC(twos)
        target = [[[1, False, True, False, False, True]],
                [[0, True, False, False, False, True]],
                [],
                [[4, False, True, False, False, True]],
                [[3, True, False, False, False, True]],
                [],
                [[7, False, True, False, False, True]],
                [[6, True, False, False, False, True]]]
#        print(NTC1)
        self.assertTrue(NTC1 == target)
        twos = [ ['12',0,1,'00'] , ['23',0,7,'02'] , ['13',7,7,'22'] ]
        NTC1 = NTC(twos)

#        print(NTC1)

        target = [[[1, False, True, True, False, False]], [[0, True, False, True, False, False], [2, False, True, False, True, False]], [[1, False, True, False, True, False]]]
        self.assertTrue(NTC1 == target)

    def test_level2_Y_Wing(self):
#        chains = [[[1, False, True, True, False, False]], [[0, True, False, True, False, False], [2, False, True, False, True, False]], [[1, False, True, False, True, False]]]
        YW = Y_Wing
        cp = copyofgrid
        basic = basicgrid()
        cpbasic = cp(basic)
        YW1 = YW(basic)
        self.assertTrue(YW1[0] == cpbasic)
        self.assertFalse(YW1[1])

        basic[0][1] = '12'
        basic[0][7] = '23'
        basic[7][7] = '13'
        cpbasic = cp(basic)
        YW1 = YW(basic)       
        self.assertTrue(YW1[1])
        self.assertFalse(YW1[0] == cpbasic)
#        print(YW1[0][7][0])
        self.assertTrue(YW1[0][7][0] == '23456789')
        basic = basicgrid()
        basic[0][0] = '12'
        basic[2][2] = '13'
        basic[0][6] = '23'
        cpbasic = cp(basic)
        YW1 = YW(basic)   
        self.assertTrue(YW1[1])
        cpbasic[0][2] = '12456789'
        cpbasic[2][6:] = ['12456789' for i in range(3)]
#        print('*'*30)
#        print(basic[0][2])
#        print(basic[2])
#        print(cpbasic[2])
        self.assertTrue(cpbasic[2] == basic[2])

from level3 import XY_chain,Rectangle

class Testlevel3(unittest.TestCase):
    def test_level3_XY_chain(self):
        cp = copyofgrid

        XY = XY_chain
        basic = basicgrid()
        cpbasic = cp(basic)
        XY1 = XY_chain(basic)
        self.assertTrue(XY1[0] == cpbasic)
        self.assertFalse(XY1[1])
        basic[4][4] = '12'
        basic[4][7] = '23'
        basic[1][7] = '34'
#        basic[4][7] = '34'
        basic[1][0] = '45'
        basic[6][0] = '56'
        basic[8][2] = '67'
        basic[8][5] = '78'
        basic[6][4] = '81'
        cpbasic = cp(basic)
        XY1 = XY_chain(basic)
        self.assertTrue(XY1[1])
        self.assertFalse(cpbasic == basic)

        basic = basicgrid()
        basic[0][0] = '12'
        basic[1][2] = '41'
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
        XY1 = XY_chain(basic)

        self.assertTrue(XY1[1])
if __name__ == '__main__':
    unittest.main()

