import numpy as np


def fade_in(wave, nsamples):
    new_wave = wave
    r = 0
    for i in range(nsamples):
        r += 1 / nsamples
        new_wave[i] = new_wave[i] * (r)
    return new_wave


def fade_out(wave, nsamples):
    new_wave = wave
    r = 0
    for i in range(nsamples):
        r += 1 / nsamples
        i = i * -1
        new_wave[i] = new_wave[i] * (r)
    return new_wave


def exponential_decay(wave, time_axis, ratio):
    return wave * np.exp(-time_axis * ratio)
