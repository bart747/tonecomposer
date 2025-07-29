import effects
import filters
import numpy as np
import sounddevice as sd
from make_sine import make_sine
from normalize import normalize
from scipy.io.wavfile import write

sample_rate = 44100  # Samples per second
duration = 2  # Seconds
amplitude = 0.5

# Generate time axis.
t = np.linspace(0, duration, int(sample_rate * duration))

# The exemplary sound will be combination of 3 different waves.
sine_wave_1 = make_sine("E1", amplitude, t)
sine_wave_2 = make_sine("E3", amplitude, t)
sine_wave_3 = make_sine("E5", amplitude, t)

# Let's add some effects and filters.
sound_1a = filters.fade_in(filters.exponential_decay(sine_wave_1, t, 10), 300)
sound_1b = effects.delay(sound_1a, 2, 2, 0.7)
sound_1 = effects.reverb(sound_1b, 1, 3)

sound_2a = filters.fade_in(filters.exponential_decay(sine_wave_2, t, 10), 500)
sound_2b = effects.delay(sound_2a, 0.5, 0.6, 0.5)
sound_2 = effects.reverb(sound_2b, 1.2, 3)

sound_3a = filters.fade_in(filters.exponential_decay(sine_wave_3, t, 10), 900)
sound_3b = effects.delay(sound_3a, 2, 2, 0.7)
sound_3 = effects.reverb(sound_3b, 1.5, 3)

# By simple multiplication we can weight amplitudes ('volumes') of the waves.
# Normalization is needed to stay in the [-1, 1] range.
sound_L = normalize(sound_1 + 0.2 * sound_2 + 0.05 * sound_3)
sound_R = normalize(sound_1 + 0.1 * sound_2 + 0.1 * sound_3)

sound_final = np.column_stack((sound_L, sound_R)).astype(np.float32)

if __name__ == "__main__":
    sd.play(sound_final, sample_rate)
    sd.wait()

    # Sine wave values are floating-point numbers between -1.0 and 1.0,
    # but 16-bit WAV files expect integers in the range -32768 to +32767.
    sound_wav = (sound_final * 32767).astype(np.int16)
    write("example.wav", sample_rate, sound_wav)
