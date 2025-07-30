import unittest
import numpy as np
from filters import fade_in, fade_out, exponential_decay

class TestFilters(unittest.TestCase):

    def test_fade_in(self):
        wave = np.ones(100)
        faded_wave = fade_in(wave, 50)
        self.assertLess(faded_wave[0], faded_wave[49])
        self.assertEqual(faded_wave[50], 1)

    def test_fade_out(self):
        wave = np.ones(100)
        faded_wave = fade_out(wave, 50)
        self.assertLess(faded_wave[-1], faded_wave[-50])
        self.assertEqual(faded_wave[-51], 1)

    def test_exponential_decay(self):
        wave = np.ones(100)
        time_axis = np.arange(100)
        decayed_wave = exponential_decay(wave, time_axis, 0.1)
        self.assertLess(decayed_wave[50], decayed_wave[0])

if __name__ == '__main__':
    unittest.main()
