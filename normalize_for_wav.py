import numpy as np


def normalize_for_wav(wave):
    # Sine wave values are floating-point numbers between -1.0 and 1.0,
    # but 16-bit WAV files expect integers in the range -32768 to +32767.
    return (wave * 32767).astype(np.int16)
