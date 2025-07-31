import unittest

import numpy as np

from effects import delay, reverb, reverb_laplace


class TestEffects(unittest.TestCase):
    def test_reverb(self):
        wave = np.ones(100)
        reverbed_wave = reverb(wave, 1, 0.5)
        self.assertGreater(len(reverbed_wave), len(wave))
        self.assertTrue(np.any(reverbed_wave))
        self.assertFalse(np.array_equal(wave[10:50], reverbed_wave[10:50]))

    def test_reverb_laplace(self):
        wave = np.ones(100)
        reverbed_wave = reverb_laplace(wave, 1, 0.5)
        self.assertGreater(len(reverbed_wave), len(wave))
        self.assertTrue(np.any(reverbed_wave))
        self.assertFalse(np.array_equal(wave[10:50], reverbed_wave[10:50]))

    def test_delay(self):
        wave = np.ones(100)
        delayed_wave = delay(wave, 0.5, 1, 0.5, 0.5)
        self.assertGreater(len(delayed_wave), len(wave))
        self.assertTrue(np.any(delayed_wave))
        self.assertFalse(np.array_equal(wave[0:100], delayed_wave[0:100]))


if __name__ == "__main__":
    unittest.main()
