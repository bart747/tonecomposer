import numpy as np
import sounddevice as sd

def apply_feedback_delay(signal, sample_rate, delay_time, feedback=0.5, mix=0.5):
    """
    Applies a feedback delay (echo) effect to a signal.

    Args:
        signal (np.array): The input audio signal (should be float).
        sample_rate (int): The sample rate of the audio.
        delay_time (float): The delay time in seconds.
        feedback (float): The feedback gain (0 to 1). Controls how many echoes.
        mix (float): The mix between the dry and wet signal (0=dry, 1=wet).

    Returns:
        np.array: The signal with the delay effect.
    """
    # Convert delay time in seconds to number of samples
    delay_samples = int(delay_time * sample_rate)

    # Create a new array for the output signal
    output_signal = np.zeros_like(signal)

    # The core of the feedback delay algorithm
    for i in range(len(signal)):
        # The index of the sample we want to echo
        delayed_index = i - delay_samples

        # The value of the original signal at the current time
        dry_sample = signal[i]

        # The value of the delayed signal.
        # If the delayed_index is negative, it means we are at the beginning
        # of the signal where no echo has occurred yet.
        # We use the output_signal itself for feedback.
        wet_sample = output_signal[delayed_index] if delayed_index >= 0 else 0

        # The new sample is a mix of the dry signal and the delayed signal with feedback
        output_signal[i] = dry_sample + feedback * wet_sample

    # Mix the original (fully dry) signal with the generated (fully wet) signal
    final_signal = (1 - mix) * signal + mix * output_signal

    return final_signal


def generate_ping(frequency, duration, sample_rate=44100):
    """Generates a short sine wave burst as a float32 array."""
    t = np.linspace(0., duration, int(sample_rate * duration), endpoint=False)
    # A simple attack-decay envelope to make it sound more like a "ping"
    envelope = np.exp(-t * 15)
    amplitude = 0.7
    data = amplitude * np.sin(2. * np.pi * frequency * t) * envelope
    
    # Pad with silence to allow the delay tail to be heard
    padding = np.zeros(int(sample_rate * 2)) # 2 seconds of silence
    return np.concatenate([data, padding]).astype(np.float32)


if __name__ == '__main__':
    # Parameters
    sample_rate = 44100
    note_frequency = 880  # A5 note, a clear pitch
    note_duration = 0.1   # A very short "ping" to make the echoes distinct

    delay_time = 0.25      # seconds
    feedback_amount = 0.6  # 60% feedback, creates several echoes
    mix_amount = 0.5       # 50% dry, 50% wet

    # Generate a short sound
    ping_sound = generate_ping(note_frequency, note_duration, sample_rate)

    # Apply the feedback delay effect
    delayed_signal = apply_feedback_delay(ping_sound, sample_rate, delay_time, feedback=feedback_amount, mix=mix_amount)

    # Normalize for playback to prevent clipping
    max_val = np.max(np.abs(delayed_signal))
    if max_val > 0:
        normalized_signal = delayed_signal / max_val
    else:
        normalized_signal = delayed_signal

    # Play the sound
    print("Playing signal with feedback delay...")
    sd.play(normalized_signal, samplerate=sample_rate)
    sd.wait()
    print("Playback finished.")
