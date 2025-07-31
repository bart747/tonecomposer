import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

import effects
import filters
from make_sine import make_sine
from normalize import normalize
from normalize_for_wav import normalize_for_wav

sample_rate = 44100  # Samples per second
duration = 2  # Seconds
amplitude = 0.5

# Generate time axis.
t = np.linspace(0, duration, int(sample_rate * duration))

# The exemplary sound will be combination of 3 different waves.
sine_wave_1 = make_sine("A1", amplitude, t)
sine_wave_2 = make_sine("E3", amplitude, t)
sine_wave_3 = make_sine("A4", amplitude, t)

# Let's add some effects and filters.
# Notice that sum of tails (from effects) for each sound is the same.
# Otherwise, we would need to add some extra zeros to arrays to make them equal in length.
sound_1a = filters.fade_in(filters.exponential_decay(sine_wave_1, t, 10), 300)
sound_1b = effects.delay(sound_1a, 0.2, 1, 1, 0.2)
sound_1c = effects.delay(sound_1b, 0.5, 1, 1, 0.1)
sound_1 = effects.reverb(sound_1c, 2, 5, 0.5)

sound_2a = filters.fade_in(filters.exponential_decay(sine_wave_2, t, 10), 500)
sound_2b = effects.delay(sound_2a, 0.1, 1, 2, 0.2)
sound_2 = effects.reverb(sound_2b, 1, 5, 0.5)

sound_3a = filters.fade_in(filters.exponential_decay(sine_wave_3, t, 10), 900)
sound_3b = effects.delay(sound_3a, 0.2, 1, 1, 0.5)
sound_3c = effects.delay(sound_3b, 0.3, 1, 1, 0.4)
sound_3 = effects.reverb(sound_3c, 2, 5, 0.5)

# By simple multiplication we can weight amplitudes ('volumes') of the waves.
sound_L = 1.8 * sound_1 + 1.2 * sound_2 + 2 * sound_3
sound_R = 1.7 * sound_1 + 1.3 * sound_2 + 1.9 * sound_3

sound_LR = np.column_stack((sound_L, sound_R))

# 'normalize' is needed to stay in the [-1, 1] range.
# After all the transformations above the signals are already not in the range.
sound_final = normalize(sound_LR)

if __name__ == "__main__":
    sd.play(sound_final, sample_rate)
    sd.wait()

    # Sine wave values are floating-point numbers between -1.0 and 1.0,
    # but 16-bit WAV files expect integers in the range -32768 to +32767.
    write("example.wav", sample_rate, normalize_for_wav(sound_final))
