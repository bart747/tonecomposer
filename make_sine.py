import numpy as np
from notes import frequencies as f


def make_sine(note, amplitude, time_axis):
    return np.sin(2 * np.pi * f[note] * time_axis) * amplitude
