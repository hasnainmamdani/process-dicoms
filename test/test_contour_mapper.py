import unittest

from src.contour_mapper import map_dicom_contour, generate_dicom_contour_map

class TestContourMapper(unittest.TestCase):

    def test_map_dicom_contour(self):
        map = map_dicom_contour('test_data/dicoms/', 'SCD0000501', 'test_data/contourfiles/', 'SC-HF-I-6')
        self.assertEqual(len(map), 2)
        self.assertEqual(map['test_data/dicoms/SCD0000501/29.dcm'], 'test_data/contourfiles/SC-HF-I-6/i-contours/IM-0001-0029-icontour-manual.txt')
        self.assertEqual(map['test_data/dicoms/SCD0000501/9.dcm'], 'test_data/contourfiles/SC-HF-I-6/i-contours/IM-0001-0009-icontour-manual.txt')


    def test_generate_dicom_contour_map(self):
        map = generate_dicom_contour_map('test_data/link.csv', 'test_data/dicoms/', 'test_data/contourfiles/')
        self.assertEqual(len(map), 4)
        print(map)
        self.assertEqual(map['test_data/dicoms/SCD0000501/29.dcm'], 'test_data/contourfiles/SC-HF-I-6/i-contours/IM-0001-0029-icontour-manual.txt')
        self.assertEqual(map['test_data/dicoms/SCD0000501/9.dcm'], 'test_data/contourfiles/SC-HF-I-6/i-contours/IM-0001-0009-icontour-manual.txt')
        self.assertEqual(map['test_data/dicoms/SCD0000401/200.dcm'], 'test_data/contourfiles/SC-HF-I-5/i-contours/IM-0001-0200-icontour-manual.txt')
        self.assertEqual(map['test_data/dicoms/SCD0000401/187.dcm'], 'test_data/contourfiles/SC-HF-I-5/i-contours/IM-0001-0187-icontour-manual.txt')

if __name__ == '__main__':
    unittest.main()
