import numpy as np
from scipy.signal import convolve

rng = np.random.default_rng()
sample_rate = 44100


def reverb(wave, decay_time=1, tail=2):
    # '* 2 - 1' shiftes the rangefrom '0.0 to 0.1' into '-1.0 to 1.0'
    # reverb needs space on the end for the proper effect
    random_impulse_response = (
        rng.standard_normal(int(sample_rate * tail)) * 2 - 1
    ).astype(np.float32)

    # exponential decay
    random_impulse_response *= np.exp(
        -decay_time * np.arange(len(random_impulse_response)) / sample_rate
    )
    reverbed_signal = convolve(wave, random_impulse_response, mode="full")

    return reverbed_signal


def delay(wave, delay_time=0.5, wet_gain=1, tail_length=1, mix=0.2):
    # Convert delay time in seconds to number of samples.
    delay_samples = int(delay_time * sample_rate)

    # delay needs space on the end to be heard
    padding = np.zeros(int(sample_rate * tail_length))
    padded_signal = np.concatenate([wave, padding]).astype(np.float32)

    wet_signal = np.zeros_like(padded_signal)

    for i in range(len(padded_signal)):
        # The index of the sample we want to echo.
        # We want to echo something from the past,
        # according to the delay time converted to number of samples.
        delayed_sample_i = i - delay_samples

        # The value of the delayed signal.
        wet_sample = padded_signal[delayed_sample_i] if delayed_sample_i >= 0 else 0

        wet_signal[i] = wet_sample * wet_gain

    output_signal = (1 - mix) * padded_signal + mix * wet_signal

    return output_signal
