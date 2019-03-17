import matplotlib.pyplot as plt
import random

def visualize_images(dicoms, icontours, ocontours):
    """"
    Plot 10 images randomly along with their i and o-contours.

    :param dicoms: list of DICOM images
    :param icontours: list of i-contour masks of the corresponding DICOM images
    :param ocontours: list of o-contour masks of then corresponding DICOM images
    """

    for r in range(10):
        i = random.randint(0, len(dicoms))

        plt.figure(figsize=(12, 4))
        plt.subplot(1,2,1)
        plt.title('Original DICOM')
        plt.imshow(dicoms[i], cmap="hot")
        plt.clim(0,1000)
        plt.colorbar()

        plt.subplot(1,2,2)
        plt.title('DICOM with i and o-contours')
        plt.imshow(dicoms[i] + icontours[i]*255 + ocontours[i]*255, cmap="hot")
        plt.clim(0,1000)
        plt.colorbar()

    plt.show()




