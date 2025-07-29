import numpy as np
from scipy.signal import convolve

from normalize import normalize

# Parameters
sample_rate = 44100
reverb_decay = 1.5  # How quickly the reverb fades
reverb_length = 5  # Length of the reverb tail in seconds

rng = np.random.default_rng()


def reverb(signal):
    # Weibull distribution is common for in wind speed analysis
    # '* 2 - 1' shiftes the rangefrom '0.0 to 0.1' into '-1.0 to 1.0'
    random_impulse_response = rng.weibull(1, int(sample_rate * reverb_length)) * 2 - 1
    # exponential decay
    random_impulse_response *= np.exp(
        -reverb_decay * np.arange(len(random_impulse_response)) / sample_rate
    )
    reverbed_signal = convolve(signal, random_impulse_response, mode="full")

    # Normalize the output to 16-bit integer range to prevent clipping
    reverbed_signal *= np.iinfo(np.int16).max / np.max(np.abs(reverbed_signal))
    reverbed_signal = reverbed_signal.astype(np.int16)

    return normalize(reverbed_signal)
