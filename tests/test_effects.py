import unittest

import numpy as np
from effects import delay, reverb


class TestEffects(unittest.TestCase):
    def test_reverb(self):
        wave = np.ones(100)
        reverbed_wave = reverb(wave, 0.5, 0.5)
        self.assertGreater(len(reverbed_wave), len(wave))
        self.assertTrue(np.any(reverbed_wave))

    def test_delay(self):
        wave = np.ones(100)
        delayed_wave = delay(wave, 0.5, 0.5, 0.5)
        self.assertGreater(len(delayed_wave), len(wave))
        self.assertTrue(np.any(delayed_wave))


if __name__ == "__main__":
    unittest.main()
