import argparse
import logging

from src.data_loader import ImageDataLoader
from src.model_trainer import generate_batches_for_training
from src.visualization_utils import visualize_images

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(threadName)s %(levelname)s %(message)s')


def main(args):

    dicoms, icontours, ocontours = ImageDataLoader(args.links_filename, args.dicom_path, args.contour_path).load_data()
    #dataset = generate_batches_for_training(args.epochs, args.batch_size, args.buffer_size, dicoms, targets)
    visualize_images(dicoms, icontours, ocontours)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = 'load dicom files along with their corresponding contours')
    parser.add_argument('--links_filename', default = '../final_data/link.csv',
                        help = 'path of the file to use to link up the appropriate dicoms and contour files')
    parser.add_argument('--dicom_path', default = '../final_data/dicoms/',
                        help = 'path of all directories that contain the dicom files')
    parser.add_argument('--contour_path', default = '../final_data/contourfiles/',
                        help = 'path of all directories that contain the contour files')

    parser.add_argument('--epochs', default = 2,
                        help = 'number of times to repeat the dataset. Use -1 or None for repeating indefinitely')
    parser.add_argument('--batch_size', default = 8,
                        help = 'number of elements to combine in a single batch')
    parser.add_argument('--buffer_size', default = 10,
                        help = 'the number of elements from the dataset from which the new dataset will sample. \
                        For perfect shuffling, a buffer size greater than or equal to the full size of the dataset is required.')

    args = parser.parse_args()

    main(args)
