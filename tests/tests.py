import unittest
import yaml
import pathlib
import os

class BasicFuntionality(unittest.TestCase):

    def setUp(self):
        path = pathlib.Path(__file__).parent
        self.test_file = pathlib.Path(path / 'test.yaml')

        self.cfg_dict = {
            'a':1, 'b':{'c':2, 'd':3}, 'e':{'f':{'g':4, 'h':5}}
            }

        cfg_yaml = {
            'a':2, 'b':{'c':2, 'd':3, 'x':17}, 'e':{'f':{'g':18, 'h':5}, 'i':{'j':10}}
            }
        
        stream = open(self.test_file, 'w')
        yaml.dump(cfg_yaml, stream, Dumper=yaml.SafeDumper)
        stream.close()
        

    def tearDown(self):
        del self.cfg_dict
        os.remove(self.test_file)

    def test_access_to_outer_key():
        cfg = 
        

    
        
