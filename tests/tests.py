import unittest

class BasicFuntionality(unittest.TestCase):

    def setUp(self):
        self.cfg_dict = {
            'a':1, 'b':{'c':2, 'd':3}, 'e':{'f':{'g':4, 'h':5}}
            }
    def tearDown(self):
        del self.cfg_dict
        
