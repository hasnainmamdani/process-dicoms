import unittest
import numpy as np
import tensorflow as tf
from tensorflow.python.framework.errors_impl import OutOfRangeError

from src.model_trainer import generate_batches_for_training

class TestModelTrainer(unittest.TestCase):
    def test_generate_batches_for_training(self):
        dataset = generate_batches_for_training(2, 3, 10, np.arange(12), np.arange(12))
        iterator = dataset.make_one_shot_iterator()
        next_batch = iterator.get_next()

        #iterate over the batches
        sess = tf.Session()
        print("epoch 1")
        for _ in range(4):
            print(sess.run(next_batch))
        print("epoch 2")
        for _ in range(4):
            print(sess.run(next_batch))

        # all batches completed
        with self.assertRaises(OutOfRangeError) as context:
            sess.run(next_batch)

        self.assertTrue('OutOfRangeError' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
