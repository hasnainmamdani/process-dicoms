import logging
from src.contour_mapper import generate_dicom_contour_map
from src.parser import parse_dicom_file, parse_contour_file, poly_to_mask

logger = logging.getLogger(__name__)


class ImageDataLoader:
    """To obtain dicom images and their corresponding contours"""

    def __init__(self, links_filename, dicom_path, contour_path):
        self.links_filename = links_filename
        self.dicom_path = dicom_path
        self.contour_path = contour_path

    def load_data(self):
        logger.info('Finding contours of dicom files. links_filename:%s, dicom_path:%s, contour_path:%s',
                    self.links_filename, self.dicom_path, self.contour_path)
        dicom_contour_file_map = generate_dicom_contour_map(self.links_filename, self.dicom_path, self.contour_path)
        logger.info('Found i-contour and o-contour files for %d dicoms', len(dicom_contour_file_map))

        logger.info("Parsing dicom and contour files")
        images = []
        icontours = []
        ocontours = []
        for k, v in dicom_contour_file_map.items():
            dicom = parse_dicom_file(k)
            icontour_coord = parse_contour_file(v['i-contour'])
            ocontour_coord = parse_contour_file(v['o-contour'])
            images.append(dicom)
            icontours.append(poly_to_mask(icontour_coord, dicom.shape[1], dicom.shape[0]))
            ocontours.append(poly_to_mask(ocontour_coord, dicom.shape[1], dicom.shape[0]))

        return images, icontours, ocontours
