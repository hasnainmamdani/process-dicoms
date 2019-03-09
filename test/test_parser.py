import unittest

from src.parser import parse_contour_file

class TestParser(unittest.TestCase):
    def test_parse_contour_file(self):
        coord = parse_contour_file('test_data/contourfiles/basic.txt')
        self.assertEqual(len(coord), 4, "Should be 4")
        self.assertEqual(coord, [(110.5, 114.5), (111.0, 114.0), (111.5, 114.0), (110.0, 114.5)])


if __name__ == '__main__':
    unittest.main()
