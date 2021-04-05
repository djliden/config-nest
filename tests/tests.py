import unittest
import yaml
import pathlib
import os
from confignest.confignest import Config


class BasicFuntionality(unittest.TestCase):

    def setUp(self):
        path = pathlib.Path(__file__).parent
        self.test_file = pathlib.Path(path / 'test.yaml')

        self.cfg_dict = {
            'a': 1, 'b': {'c': 2, 'd': 3}, 'e': {'f': {'g': 4, 'h': 5}}
            }

        cfg_yaml = {
            'a': 2, 'b': {'c': 2, 'd': 3, 'x': 17},
            'e': {'f': {'g': 18, 'h': 5}, 'i': {'j': 10}}
            }

        with open(self.test_file, 'w') as stream:
            yaml.dump(cfg_yaml, stream, Dumper=yaml.SafeDumper)

        self.cfg = Config(self.cfg_dict)
        self.cfg.update_config(self.test_file)

    def tearDown(self):
        del self.cfg_dict
        os.remove(self.test_file)

    def test_access_to_outer_key(self):
        self.assertEqual(self.cfg.a, 2)

    def test_access_to_inner_key(self):
        self.assertEqual(self.cfg.b.c, 2)
        self.assertEqual(self.cfg.b.x, 17)
        self.assertEqual(self.cfg.e.i.config, {'j': 10})

    def test_nested_type(self):
        self.assertIsInstance(self.cfg.b, Config)
        self.assertIsInstance(self.cfg.b.config, dict)

    def test_frozen(self):
        with self.assertRaises(TypeError):
            self.cfg.z = 26
        with self.assertRaises(AttributeError):
            print(self.cfg.z)
        # with self.assertRaises(TypeError):
        #     self.cfg.a = 26


if __name__ == '__main__':
    unittest.main()
