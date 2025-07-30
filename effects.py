import numpy as np
from scipy.signal import convolve

rng = np.random.default_rng()


def reverb(wave, decay_time=1, tail_length=2):
    sample_rate = 44100
    # '* 2 - 1' shiftes the rangefrom '0.0 to 0.1' into '-1.0 to 1.0'
    random_impulse_response = (
        rng.standard_normal(int(sample_rate * tail_length)) * 2 - 1
    ).astype(np.float32)

    # exponential decay
    random_impulse_response *= np.exp(
        -decay_time * np.arange(len(random_impulse_response)) / sample_rate
    )
    reverbed_signal = convolve(wave, random_impulse_response, mode="full")

    return reverbed_signal


def delay(wave, delay_time, wet_gain, tail_length, mix):
    sample_rate = 44100
    # Convert delay time in seconds to number of samples
    delay_samples = int(delay_time * sample_rate)

    # delay needs space on the end to be heard
    padding = np.zeros(int(sample_rate * tail_length))
    padded_signal = np.concatenate([wave, padding]).astype(np.float32)

    wet_signal = np.zeros_like(padded_signal)

    for i in range(len(padded_signal)):
        # The index of the sample we want to echo,
        # We want to echo something from the past,
        # according to delay time converted to number of samples
        delayed_sample_i = i - delay_samples

        # The value of the delayed signal.
        wet_sample = padded_signal[delayed_sample_i] if delayed_sample_i >= 0 else 0

        wet_signal[i] = wet_sample * wet_gain

    output_signal = (1 - mix) * padded_signal + mix * wet_signal

    return output_signal


def compressor(signal, threshold=-10, ratio=4, makeup_gain=6):
    """
    A simple audio compressor.
    - threshold: The level (in dB) above which compression is applied.
    - ratio: The amount of gain reduction. A ratio of 4 means for every 4dB
             the signal goes over the threshold, the output is only 1dB over.
    - makeup_gain: The amount of gain (in dB) to apply to the whole signal
                   after compression.
    """
    # Convert threshold and makeup_gain from dB to linear scale
    threshold_linear = 10 ** (threshold / 20)
    makeup_gain_linear = 10 ** (makeup_gain / 20)

    # Find where the signal exceeds the threshold
    above_threshold = np.abs(signal) > threshold_linear

    # Apply compression
    compressed_signal = np.copy(signal)
    compressed_signal[above_threshold] = (
        threshold_linear + (np.abs(signal[above_threshold]) - threshold_linear) / ratio
    ) * np.sign(signal[above_threshold])

    # Apply makeup gain
    return compressed_signal * makeup_gain_linear
