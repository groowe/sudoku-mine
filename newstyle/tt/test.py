import unittest
#from grid import basicgrid,standardize,done,validate_solution,copyofgrid
#from level0 import Cleanup,Naked_Single,Unique
#
def tt():
    return 10

class TestStringMethods(unittest.TestCase):
    def grid_basic(self):
        self.assertEqual(tt(),[['123456789' for i in range(9)] for i in range(9)])
    
if __name__ == '__main__':
    unittest.main()

