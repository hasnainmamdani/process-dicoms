import numpy as np
import tensorflow as tf

import logging
logger = logging.getLogger(__name__)


def generate_batches_for_training(epochs, batch_size, buffer_size, features, labels):
    logger.info("loading batches of data for input to a deep learning model. \
    epochs:%d, batch_size:%d, buffer_size:%d", epochs, batch_size, buffer_size)
    dataset = tf.data.Dataset.from_tensor_slices((np.array(features), np.array(labels)))
    dataset = dataset.shuffle(buffer_size=buffer_size)
    dataset = dataset.batch(batch_size)
    dataset = dataset.repeat(epochs)
    logger.info("done")

    return dataset
