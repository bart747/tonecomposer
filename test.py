import unittest

import normalize as normalize
import numpy as np
from make_sine import make_sine

t = np.linspace(0, 1, int(44100 * 1))
sine_wave = make_sine("E1", 0.5, t)

arr = np.array([1, 2, 3, -1, -2, -3])


class TestNormalize(unittest.TestCase):
    def test_range(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


if __name__ == "__main_":
    unittest.main()
