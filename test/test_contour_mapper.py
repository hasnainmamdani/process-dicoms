import unittest

from src.contour_mapper import map_dicom_contour, generate_dicom_contour_map

class TestContourMapper(unittest.TestCase):

    def test_map_dicom_contour(self):
        map = map_dicom_contour('test_data/dicoms/', 'SCD0000501', 'test_data/contourfiles/', 'SC-HF-I-6')
        self.assertEqual(len(map), 2)
        self.assertEqual(map['test_data/dicoms/SCD0000501/59.dcm']['i-contour'], 'test_data/contourfiles/SC-HF-I-6/i-contours/IM-0001-0059-icontour-manual.txt')
        self.assertEqual(map['test_data/dicoms/SCD0000501/59.dcm']['o-contour'], 'test_data/contourfiles/SC-HF-I-6/o-contours/IM-0001-0059-ocontour-manual.txt')
        self.assertEqual(map['test_data/dicoms/SCD0000501/79.dcm']['i-contour'], 'test_data/contourfiles/SC-HF-I-6/i-contours/IM-0001-0079-icontour-manual.txt')
        self.assertEqual(map['test_data/dicoms/SCD0000501/79.dcm']['o-contour'], 'test_data/contourfiles/SC-HF-I-6/o-contours/IM-0001-0079-ocontour-manual.txt')


    def test_generate_dicom_contour_map(self):
        map = generate_dicom_contour_map('test_data/link.csv', 'test_data/dicoms/', 'test_data/contourfiles/')
        self.assertEqual(len(map), 3)
        self.assertEqual(map['test_data/dicoms/SCD0000501/59.dcm']['i-contour'], 'test_data/contourfiles/SC-HF-I-6/i-contours/IM-0001-0059-icontour-manual.txt')
        self.assertEqual(map['test_data/dicoms/SCD0000501/59.dcm']['o-contour'], 'test_data/contourfiles/SC-HF-I-6/o-contours/IM-0001-0059-ocontour-manual.txt')
        self.assertEqual(map['test_data/dicoms/SCD0000501/79.dcm']['i-contour'], 'test_data/contourfiles/SC-HF-I-6/i-contours/IM-0001-0079-icontour-manual.txt')
        self.assertEqual(map['test_data/dicoms/SCD0000501/79.dcm']['o-contour'], 'test_data/contourfiles/SC-HF-I-6/o-contours/IM-0001-0079-ocontour-manual.txt')
        self.assertEqual(map['test_data/dicoms/SCD0000401/200.dcm']['i-contour'], 'test_data/contourfiles/SC-HF-I-5/i-contours/IM-0001-0200-icontour-manual.txt')
        self.assertEqual(map['test_data/dicoms/SCD0000401/200.dcm']['o-contour'], 'test_data/contourfiles/SC-HF-I-5/o-contours/IM-0001-0200-ocontour-manual.txt')

if __name__ == '__main__':
    unittest.main()
