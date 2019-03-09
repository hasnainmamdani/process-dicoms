import logging
from src.contour_mapper import generate_dicom_contour_map
from src.parser import parse_dicom_file, parse_contour_file, poly_to_mask

logger = logging.getLogger(__name__)


class ImageDataLoader:
    """To obtain dicom images and their corresponding i-contours"""

    def __init__(self, links_filename, dicom_path, contour_path):
        self.links_filename = links_filename
        self.dicom_path = dicom_path
        self.contour_path = contour_path

    def load_data(self):
        logger.info('Finding contours of dicom files. links_filename:%s, dicom_path:%s, contour_path:%s',
                    self.links_filename, self.dicom_path, self.contour_path)
        dicom_contour_file_map = generate_dicom_contour_map(self.links_filename, self.dicom_path, self.contour_path)
        logger.info('Found contour files for %d dicoms', len(dicom_contour_file_map))

        logger.info("Parsing dicom and contour files")
        images = []
        targets = []
        for k, v in dicom_contour_file_map.items():
            dicom = parse_dicom_file(k)
            contour_coord = parse_contour_file(v)
            mask = poly_to_mask(contour_coord, dicom.shape[1], dicom.shape[0])
            images.append(dicom)
            targets.append(mask)

        return images, targets
