import csv
import glob
import os
import logging
logger = logging.getLogger(__name__)


def map_dicom_contour(dicom_path, dicom_id, contour_path, contour_id):
    """Creates a mapping of patient's DICOM files and their corresponding contour files if they exist

    :param dicom_path: path of all directories that contain dicom files
    :param dicom_id: directory to look for DICOM files
    :param contour_path: path of all directories that contain contours
    :param contour_id: directory to look for contour files
    :return: dictionary of DICOM files mapped to corresponding contour files
    """

    patient_dicoms_dir = dicom_path + dicom_id
    patient_contours_dir = contour_path + contour_id

    if not os.path.isdir(patient_dicoms_dir):
        logger.error("Directory %s does not exist. Unable to load patient's dicom files.", patient_dicoms_dir)

    if not os.path.isdir(patient_contours_dir):
        logger.error("Directory %s does not exist. Unable to load patient's contour files.", patient_contours_dir)

    patient_dict = {}

    files = glob.glob(patient_dicoms_dir + "/*")
    for dicom_file in files:
        base = os.path.basename(dicom_file)
        name = os.path.splitext(base)[0]

        #TODO maybe fine for now but need a better heuristic to the map dicom filename with corresponding contour file
        contour_file = patient_contours_dir + "/i-contours/IM-0001-" + name.zfill(4) + "-icontour-manual.txt"

        if os.path.exists(contour_file):
            patient_dict[dicom_file] = contour_file

    return patient_dict


def generate_dicom_contour_map(links_filename, dicom_path, contour_path):
    """Creates mapping of all the patient's DICOM files and their corresponding contour files if they exist
    :param links_filename: path of the file to use to link up the appropriate dicoms and contour files
    :param dicom_path: path of all directories that contain dicom files
    :param contour_path: path of all directories that contain contours
    :return: dictionary of DICOM files mapped to corresponding contour files
    """
    if not os.path.exists(links_filename):
        logger.error("File %s does not exist. Unable to links between dicom files and contour files.", links_filename)
        return

    with open(links_filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)
        dicom_contour_map = {}
        for row in csv_reader:
            assert len(row)==2, "Incorrect link format. Each link should have two arguments"
            dicom_contour_map.update(map_dicom_contour(dicom_path, row[0], contour_path, row[1]))

    return dicom_contour_map
