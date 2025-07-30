import unittest
import numpy as np
from normalize import normalize

class TestNormalize(unittest.TestCase):

    def test_positive_normalization(self):
        signal = np.array([1, 2, 3, 4, 5])
        normalized_signal = normalize(signal)
        self.assertAlmostEqual(np.max(np.abs(normalized_signal)), 1.0)

    def test_negative_normalization(self):
        signal = np.array([-1, -2, -3, -4, -5])
        normalized_signal = normalize(signal)
        self.assertAlmostEqual(np.max(np.abs(normalized_signal)), 1.0)

    def test_zero_signal(self):
        signal = np.array([0, 0, 0, 0, 0])
        normalized_signal = normalize(signal)
        self.assertTrue(np.array_equal(signal, normalized_signal))

if __name__ == '__main__':
    unittest.main()
