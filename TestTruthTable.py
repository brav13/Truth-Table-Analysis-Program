from TruthTable import *
import unittest

class Test(unittest.TestCase):
    def test1(self):
        
        premises = ['if p then q', 'if q then r']
        conclusion = 'if p then r'
        
        assert(find_validity(premises, conclusion) == 'The argument is valid.')
        
        
    def test2(self):   
        
        
        
        premises2 = ['p or q', 'if p then r', 'if q then r']
        conclusion2 = 'r'
        
        assert(find_validity(premises2, conclusion2) == 'The argument is valid.')
        
        
    def test3(self):   
            
        premises3 = ['if p then q', 'q']
        conclusion3 = 'p'
        
        assert(find_validity(premises3, conclusion3) == 'The argument is not valid.')
        
    def test4(self):
        
        premises4 = ['if p then q', 'not p']
        conclusion4 = 'not q'
        
        assert(find_validity(premises4, conclusion4) == 'The argument is not valid.')

    def test5(self):   
        
        premises5 = ['p', 'not q', 'q or r']
        conclusion5 = 'if p then r'
        
        assert(find_validity(premises5, conclusion5) == 'The argument is valid.')

    def test6(self):
        
        premises6 = ['p if and only if q', 'q and r']
        conclusion6 = 'p'
        
        assert(find_validity(premises6, conclusion6) == 'The argument is valid.')

    def test8(self):
        
        premises7 = ['not p']
        conclusion7 = 'p'
        
        assert(find_validity(premises7, conclusion7) == 'The argument is not valid.')
        
        
if __name__ == '__main__':
    unittest.main()