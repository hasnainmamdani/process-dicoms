import unittest

from src.data_loader import ImageDataLoader

class TestImageDataLoader(unittest.TestCase):
    def test_load_data(self):
        dicoms, targets = ImageDataLoader('test_data/link.csv', 'test_data/dicoms/', 'test_data/contourfiles/').load_data()
        self.assertEqual(len(dicoms), 4, "Should be 4")
        self.assertEqual(len(targets), 4, "Should be 4")
        self.assertEqual(dicoms[2].shape, (256, 256), "Should be (256, 256")
        self.assertEqual(targets[2].shape, (256, 256), "Should be (256, 256")


if __name__ == '__main__':
    unittest.main()
