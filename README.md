# Build Complex Synth Tones from Scratch with Python

Learn how to generate rich, custom sounds by combining basic sine waves. Just with Python and Numpy/SciPy (and SoundDevice for saving audio files).

Treat is as a starting template or an example. The [tone_example.py](./tone_example.py) file already has an exemplary voice ready to be modified or used as a WAV file:

<audio controls>
  <source src="./example.mp3" type="audio/mpeg">
Your browser does not support the audio element.
</audio>

Sine waves here are basically NumPy arrays that can be modified in various ways.

Try AI assist for explanations and troubleshooting when it comes to formatting array value ranges.
Usually you need to stay in the [-1, 1] range.
There's a function called *normalize* for that purpose.
