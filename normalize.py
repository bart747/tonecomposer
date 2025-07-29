import numpy as np


# stay in the [-1, 1] range
def normalize(signal):
    max_val = np.max(np.abs(signal))
    if max_val > 0:
        normalized_signal = signal / max_val
    else:
        normalized_signal = signal

    return normalized_signal
