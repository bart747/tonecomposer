import numpy as np
from scipy.io.wavfile import write
from scipy.signal import convolve


def apply_reverb(signal, impulse_response):
    """Applies reverb to a signal using convolution."""
    reverbed_signal = convolve(signal, impulse_response, mode="full")
    return reverbed_signal


def generate_sine_wave(frequency, duration, sample_rate=44100):
    """Generates a sine wave."""
    t = np.linspace(0.0, duration, int(sample_rate * duration))
    amplitude = np.iinfo(np.int16).max * 0.5
    data = amplitude * np.sin(2.0 * np.pi * frequency * t)
    return data.astype(np.int16)


def generate_impulse_response(decay, length, sample_rate=44100):
    """Generates a simple impulse response."""
    # Generate random noise
    ir = np.random.rand(int(sample_rate * length)) * 2 - 1
    # Apply an exponential decay
    ir *= np.exp(-decay * np.arange(len(ir)) / sample_rate)
    return ir


if __name__ == "__main__":
    # Parameters
    sample_rate = 44100
    sine_frequency = 440  # A4 note
    sine_duration = 2.0
    reverb_decay = 2.0  # How quickly the reverb fades
    reverb_length = 2.5  # Length of the reverb tail in seconds

    # 1. Generate a dry sine wave
    sine_wave = generate_sine_wave(sine_frequency, sine_duration, sample_rate)

    # 2. Generate a synthetic impulse response
    impulse_response = generate_impulse_response(
        reverb_decay, reverb_length, sample_rate
    )

    # 3. Convolve the two signals to apply reverb
    reverbed_sine_wave = apply_reverb(sine_wave, impulse_response)

    # Normalize the output to 16-bit integer range to prevent clipping
    reverbed_sine_wave *= np.iinfo(np.int16).max / np.max(np.abs(reverbed_sine_wave))
    reverbed_sine_wave = reverbed_sine_wave.astype(np.int16)

    # Write the result to a WAV file
    write("reverb_sine.wav", sample_rate, reverbed_sine_wave)

    print("Generated reverb_sine.wav")
